//
//  ErrorListener.java
//  TestXSLT
//
//  Created by Marc Liyanage on Sun Jun 08 2003.
//  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
//

package ch.entropy.testxslt;

import javax.xml.transform.*;


public class StringErrorListener implements ErrorListener {

	String errorString;
	
	public void warning(TransformerException exception) throws TransformerException {

		errorString = exception.toString();
		System.err.println("captured warning");

	}

	public void error(TransformerException exception) throws TransformerException {

		errorString = exception.toString();
		System.err.println("captured error");

	}

	public void fatalError(TransformerException exception) throws TransformerException {

		errorString = exception.toString();
		System.err.println("captured fatalError");

	}

	
	public String getErrorString() {

		return errorString;
	}

	

	

	
}
