package org.metrarc.FIDO2Client;

import java.io.*;

public class Test {
    public static void main(String[] args) {
        try {
            String s;
            ProcessBuilder pb = new ProcessBuilder("sh", "-c", "ssh", "ali@localhost", ">/dev/tty");
            pb.redirectInput(ProcessBuilder.Redirect.INHERIT);
            pb.redirectOutput(ProcessBuilder.Redirect.INHERIT);

            Process ssh = pb.start();

//            BufferedReader stdOut = new BufferedReader(new InputStreamReader (ssh.getInputStream()));
            OutputStream stdIn = ssh.getOutputStream ();
            stdIn.write ("ali\n".getBytes ("US-ASCII"));
            stdIn.flush();
            stdIn.close();

//            while ((s = stdOut.readLine()) != null)
//                System.out.println("Line: " + s);
//
//            if(s==null)
//                System.out.println("No FIDO device detected");
//
//            stdIn.write ("ali\n".getBytes ("US-ASCII"));
//            stdIn.flush ();

            ssh.waitFor();
            System.out.println ("Exit: " + ssh.exitValue());
            ssh.destroy();
        } catch (Exception e) { e.printStackTrace(); }
        String s = "bEVJZGWheX4eh-9JcjEdX_tGNub5tqDmNA7iHeKGAfwJ-jsJ27qOOtTy90noX7QL5chjfn8Rj9rEatYPze_RKg";
        System.out.println(s.length());
    }
}
