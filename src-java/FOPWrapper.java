
import java.io.*;

import org.xml.sax.*;
import com.apple.cocoa.foundation.NSData;

//Avalon
import org.apache.avalon.framework.ExceptionUtil;
import org.apache.avalon.framework.logger.Logger;
import org.apache.avalon.framework.logger.ConsoleLogger;

//FOP
import org.apache.fop.apps.Driver;
import org.apache.fop.apps.FOPException;
import org.apache.fop.messaging.MessageHandler;

/**
 * This class helps calling FOP from the Obj-C side.
 * Based on "ExampleFO2PDF.java" from the FOP project.
 */
public class FOPWrapper {

    String error;
    boolean errorOccurred = false;
	
	public NSData convert(NSData foData) throws IOException, FOPException {
        
		//Construct driver
        System.setProperty("java.awt.headless", "true");
		Driver driver = new Driver();
		
		//Setup logger
		Logger logger = new ConsoleLogger(ConsoleLogger.LEVEL_INFO);
		driver.setLogger(logger);
		MessageHandler.setScreenLogger(logger);
		
		//Setup Renderer (output format)        
		driver.setRenderer(Driver.RENDER_PDF);
        
		//Setup output
		ByteArrayOutputStream out = new java.io.ByteArrayOutputStream();
		try {
			driver.setOutputStream(out);
			
			//Setup input
			InputStream in = new java.io.ByteArrayInputStream(foData.bytes(0, foData.length()));
			try {
				driver.setInputSource(new InputSource(in));
				
				//Process FO
				driver.run();
			} catch (Exception e) {
				error = e.toString();
				errorOccurred = true;
			} finally {
				in.close();
			}
			
		} finally {
			out.close();
		}
		
		if (errorOccurred) {
			return null;
		}
		return new NSData(out.toByteArray());
		
	}
	
	public String getErrorMessage() {
		return error;
	}
	
	public boolean errorOccurred() {
		return errorOccurred;
	}
	
	
	/*
    public static void main(String[] args) {
        try {
            System.out.println("FOP ExampleFO2PDF\n");
            System.out.println("Preparing...");
            
            //Setup directories
            File baseDir = new File(".");
            File outDir = new File(baseDir, "out");
            outDir.mkdirs();
			
            //Setup input and output files            
            File fofile = new File(baseDir, "xml/fo/helloworld.fo");
            File pdffile = new File(outDir, "ResultFO2PDF.pdf");
			
            System.out.println("Input: XSL-FO (" + fofile + ")");
            System.out.println("Output: PDF (" + pdffile + ")");
            System.out.println();
            System.out.println("Transforming...");
            
            FOPWrapper app = new FOPWrapper();
            app.convertFO2PDF(fofile, pdffile);
            
            System.out.println("Success!");
        } catch (Exception e) {
            System.err.println(ExceptionUtil.printStackTrace(e));
            System.exit(-1);
        }
    }
	 
	 */
	
}
