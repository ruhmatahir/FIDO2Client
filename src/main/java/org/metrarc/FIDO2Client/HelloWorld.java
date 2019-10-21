package org.metrarc.FIDO2Client;

import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

public class HelloWorld {
    private static Logger logger = LogManager.getLogger(HelloWorld.class);
    public static void main(String[] args) {
        System.out.println("Hello!");
        logger.debug("Debug log message");
        logger.info("Info log message");
        logger.error("Error log message");
    }
}
