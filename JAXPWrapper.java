//
//  JAXPWrapper.java
//  TestXSLT
//
//  Created by Marc Liyanage on Mon Aug 04 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

//package ch.entropy.testxslt;

import java.io.*;
import java.util.*;
import java.util.regex.*;
import javax.xml.transform.*;
import javax.xml.transform.stream.*;
import javax.xml.*;
import javax.xml.parsers.*;
import org.xml.sax.*;

/**
 * JAXPWrapper is a helper class to make it easier to access JAXP transformers
 * from the Obj-C code.
 * 
 * @author    Marc Liyanage
 * @version   $Id$
 */
public class JAXPWrapper {
	
	StringWriter resultWriter;
	Exception transformException;
	String errorMessage = "(no errors)";
	int errorSource = 0;
	int errorLine = 0;

	public static final int XSLT_ERROR_SOURCE_XML = 1;
	public static final int XSLT_ERROR_SOURCE_XSLT = 2;

	
	
	
	public String getResult() {

		return resultWriter.toString();
		
	}
	
	/** 
	* Does something really useful.
	 * <p>
	 * Blah blah {@link AnotherClass} blah blah.
	 *
	 * @param arg1    the first parameter
	 * @param arg2    the second parameter
	 * @return        <code>true</code> if something,  
	 *                <code>false</code> otherwise.
	 */
	public boolean transform(String processorClassName, String xml, String xslt, String parameters, String baseUri) {

		java.lang.System.setProperty("javax.xml.transform.TransformerFactory", processorClassName);
		
		System.err.println("java reached: xml: " + xml + " xsl: " + xslt + " param: " + parameters + " baseuri: " + baseUri);

		try {
			
			TransformerFactory tf = TransformerFactory.newInstance();
			Transformer t = tf.newTransformer(new StreamSource(new StringReader(xslt), baseUri));

			
			if (parameters.length() > 0) {
				/*
				 * evil in-band separator tricks...
				 */
				Pattern pairDelimiter = Pattern.compile("--_-!-_--");
				Pattern keyValueDelimiter = Pattern.compile("==_=!=_==");
				
				String [] pairs = pairDelimiter.split(parameters);
				
				for (int i = 0; i < pairs.length; i++) {
					System.err.println("after1");
					String [] keyValue = keyValueDelimiter.split(pairs[i]);
					
					if (keyValue.length > 0) {
						System.err.println("after2");
						String key = keyValue[0];
						String value;
						
						if (keyValue.length > 1) {
							value = keyValue[1];
						} else {
							value = "";
						}
						
						t.setParameter(key, value);
					}
				}
			}
			
			resultWriter = new StringWriter();
			t.transform(new StreamSource(new StringReader(xml)), new StreamResult(resultWriter));

		} catch (TransformerConfigurationException e) {
			
			errorSource = XSLT_ERROR_SOURCE_XSLT; /* That's the assumption anyway */
			errorMessage = getDeepestException(e).getMessage();
			errorLine = getLineNumber(getDeepestException(e));
			transformException = e;
			
			return false;
			
		} catch (TransformerException e) {
			
			errorSource = XSLT_ERROR_SOURCE_XML; /* That's the assumption anyway */
			errorMessage = getDeepestException(e).getMessage();
			errorLine = getLineNumber(getDeepestException(e));
			transformException = e;
			return false;
			
		} catch (Exception e) {

			System.err.println("Exception: " + e);
			transformException = e;
			errorMessage = e.getMessage();
			return false;
		}
		
		return true;
	}

	
	
	protected static Throwable getDeepestException(Throwable t) {
		
		Throwable next = t;
		
		while (t.getCause() != null) {
			t = t.getCause();
			System.err.println("found nested throwable: " + t);
		}
		
		return t;
	}
	
	protected static int getLineNumber(Throwable t) {
		
		if (t instanceof TransformerException) {
			
			TransformerException te = (TransformerException)t;
			SourceLocator sl = te.getLocator();
			if (sl != null) {
				return sl.getLineNumber();
			}
			
			
		} else if (t instanceof SAXParseException) {
			SAXParseException spe = (SAXParseException)t;
			return spe.getLineNumber();
		}
		
		return 0;
		
	}
	
	

	public String getErrorMessage() {
		return errorMessage;
	}
	
	public int getErrorLine() {
		return errorLine;
	}
	
	public int getErrorSource() {
		return errorSource;
	}
	
		
	
	/** 
	 * Main method for command-line invocation.
	 *
	 * @param argv    the argument String array
	 */
	public static void main (String argv[]) {
		
		JAXPWrapper ref = new JAXPWrapper();
		System.out.println("ref: " + ref);
		String processorImpl = "com.icl.saxon.TransformerFactoryImpl";

		System.out.println("\nParam Test\n");
		String xml = "<?xml version='1.0'?>\n\n\n\n<root/>";
		String xslt = "<?xml version='1.0' encoding='iso-8859-1'?>\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'><xsl:param name='param1' select=\"'wrong1'\"/><xsl:param name='param2' select=\"'wrong2'\"/><xsl:template match='/'>-<xsl:value-of select='$param1'/>--<xsl:value-of select='$param2'/>-</xsl:template></xsl:stylesheet>";
		String parameters = "param1==_=!=_==right1--_-!-_--param2==_=!=_==right2";
		ref.transform(processorImpl, xml, xslt, parameters, null);
		System.out.println(ref.getResult());
		System.out.println("source: " + ref.getErrorSource() + " line: " + ref.getErrorLine() + " msg: " + ref.getErrorMessage());

		System.out.println("\nEmpty param test\n");
		xml = "<?xml version='1.0'?>\n\n\n\n<root/>";
		xslt = "<?xml version='1.0' encoding='iso-8859-1'?>\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'><xsl:param name='param1' select=\"'wrong1'\"/><xsl:param name='param2' select=\"'wrong2'\"/><xsl:template match='/'>-<xsl:value-of select='$param1'/>--<xsl:value-of select='$param2'/>-</xsl:template></xsl:stylesheet>";
		parameters = "";
		ref.transform(processorImpl, xml, xslt, parameters, null);
		System.out.println(ref.getResult());
		System.out.println("source: " + ref.getErrorSource() + " line: " + ref.getErrorLine() + " msg: " + ref.getErrorMessage());
		
		System.out.println("\nsystem-property() test\n");
		xml = "<?xml version='1.0'?>\n\n\n<root/>";
		xslt = "<?xml version='1.0' encoding='iso-8859-1'?>\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'><xsl:template match='/'>vendor: <xsl:value-of select=\"system-property('xsl:vendor')\"/></xsl:template></xsl:stylesheet>";
		ref.transform(processorImpl, xml, xslt, parameters, null);
		System.out.println(ref.getResult());
		System.out.println("source: " + ref.getErrorSource() + " line: " + ref.getErrorLine() + " msg: " + ref.getErrorMessage());
		
		System.out.println("\nBroken XML Test\n");
		xml = "<?xml version='1.0'?>\n\n\n<root>\n\n\n</xyz>";
		xslt = "<?xml version='1.0' encoding='iso-8859-1'?>\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'><xsl:template match='/'>match!</xsl:template></xsl:stylesheet>";
		ref.transform(processorImpl, xml, xslt, parameters, null);
		System.out.println("source: " + ref.getErrorSource() + " line: " + ref.getErrorLine() + " msg: " + ref.getErrorMessage());
		
		System.out.println("\nBroken XSLT Test\n");
		xml = "<?xml version='1.0'?>\n<root/>";
		xslt = "<?xml version='1.0' encoding='iso-8859-1'?>\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'><xsl:template match='/'>match!</xsl:template></xsl:xyz>";
		ref.transform(processorImpl, xml, xslt, parameters, null);
		System.out.println("source: " + ref.getErrorSource() + " line: " + ref.getErrorLine() + " msg: " + ref.getErrorMessage());
		
		System.out.println("\nBroken XML and XSLT Test\n");
		xml = "<?xml version='1.0'?>\n<root></xyz>";
		xslt = "<?xml version='1.0' encoding='iso-8859-1'?>\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'><xsl:template match='/'>match!</xsl:template></xsl:xyz>";
		ref.transform(processorImpl, xml, xslt, parameters, null);
		System.out.println("source: " + ref.getErrorSource() + " line: " + ref.getErrorLine() + " msg: " + ref.getErrorMessage());
		
		System.out.println("\nBroken XML and XSLT Test 2\n");
		xml = "<?xml version='1.0'?>\n<root></xyz>";
		xslt = "<?xml version='1.0' encoding='iso-8859-1'?>\n\n<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>\n\n\n<xsl:value-of select='1'/>\n\n\n<xsl:template match='/'>match!</xsl:template>\n\n\n</xsl:stylesheet>";
		ref.transform(processorImpl, xml, xslt, parameters, null);
		System.out.println("source: " + ref.getErrorSource() + " line: " + ref.getErrorLine() + " msg: " + ref.getErrorMessage());

		
		
	}
	
}
