package org.metrarc.FIDO2Client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Client {
    private void initialAPITests(String pythonScript) throws IOException, InterruptedException {
        ProcessBuilder pb = new ProcessBuilder("python3", pythonScript);
        pb.redirectErrorStream(true);
        Process process = pb.start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        int exitCode = process.waitFor();
        System.out.println("\nExited with error code : " + exitCode);
    }

    private void register(String pythonScript, String userName, String displayName) {
        try {
            Scanner in = new Scanner(System.in);
            System.out.print("Enter PIN: ");
            String pin = in.nextLine();

            ProcessBuilder pb = new ProcessBuilder("python3", pythonScript, userName, displayName, pin);
            pb.redirectErrorStream(true);
            Process process = pb.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            int exitCode = process.waitFor();
            System.out.println("\nExited with error code : " + exitCode);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void authenticate(String pythonScript, String userName, String pass, String uid) {
        try {
            Scanner in = new Scanner(System.in);
            System.out.print("Enter PIN: ");
            String pin = in.nextLine();

            System.out.println("Touch your authenticator device if it is blinking ...");
            ProcessBuilder pb = new ProcessBuilder("python3", pythonScript, userName, pass, uid, pin);
            pb.redirectErrorStream(true);
            Process process = pb.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            int exitCode = process.waitFor();
            System.out.println("\nExited with error code : " + exitCode);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
//        System.out.println("Working Directory = " + System.getProperty("user.dir"));
//
//        ProcessBuilder pb = new ProcessBuilder("ping", "-c", "3", "google.com");
//        Process process = pb.start();
//
//        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
//        String line;
//        while ((line = reader.readLine()) != null) {
//            System.out.println(line);
//        }
//        int exitCode = process.waitFor();
//        System.out.println("\nExited with error code : " + exitCode);

        Client client = new Client();
//        client.initialAPITests("Initial_API_Tests.py");
//        client.register("VCHolder_Registration.py", "ruhma@metrarc.com", "Ruhma Tahir", "1234");
        client.authenticate("VCHolder_Authentication.py", "ruhma@metrarc.com", "password", "p46z2WUSAqwC6nqlQgEpCgvycMiWUMI2OVQeCYojGZY8XB1ITSiiyQDnnbv566kA_Ch-eejt54DDSg8_VR8_vg");
    }
}
