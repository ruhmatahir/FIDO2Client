package org.metrarc.FIDO2Client;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.io.FileWriter;

public class CTA {
    public static void main(String[] args) {

        String yubikey_path = getAuthenticatorPath();
        System.out.println("YubKey is located at device path: " + yubikey_path);

//        ArrayList<String> res = generateCredential("target/cred_param.json", "12345678");
//        for (String i : res) {
//            System.out.println(i);
//        }
        ArrayList<String> res = verifyCredential("target/cred_response.json");
    }
    private static String getAuthenticatorPath() {
        String s;
        Process p;
        String device_path = new String();
        try {
            p = Runtime.getRuntime().exec("fido2-token -L");
            BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while ((s = br.readLine()) != null)
                device_path = s.split(":")[0];
                System.out.println("Device Path: " + device_path);
            p.waitFor();
            System.out.println ("Exit: " + p.exitValue());
            p.destroy();

        } catch (Exception e) { e.printStackTrace(); }
        return device_path;
    }

    private static ArrayList<String> generateCredential(String jsonFile, String pin) {
        String s = "";
        Process p = null;
        String yubikey_path = getAuthenticatorPath();
        ArrayList<String> credResponseList = new ArrayList<String>();
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            // Read Credential Request from the JSON file
            byte[] credRequest = Files.readAllBytes(Paths.get(jsonFile));
            Map<String,String> credRequestMap = new HashMap<String, String>();
            credRequestMap = objectMapper.readValue(credRequest, HashMap.class);

            // Write Credential Request to file in INPUT format
            FileWriter fileWriter = new FileWriter("cred_param");
            fileWriter.write(credRequestMap.get("clientDataHash") + "\n");
            fileWriter.write(credRequestMap.get("rp") + "\n");
            fileWriter.write(credRequestMap.get("userName") + "\n");
            fileWriter.write(credRequestMap.get("userID"));
            fileWriter.flush();
            fileWriter.close();

            // Create the 'expect' script to overcome the manual PIN input problem
            FileWriter fw = new FileWriter("expect.sh");
            fw.write("#!/usr/bin/expect -f" + "\n");
            fw.write("spawn fido2-cred -M -i cred_param " + yubikey_path + "\n");
            fw.write("expect \"Enter PIN for " + yubikey_path + ":\" { send \"" + pin + "\\r\" }" + "\n");
            fw.write("interact" + "\n");
            fw.flush();
            fw.close();

            p = Runtime.getRuntime().exec("expect -f expect.sh");
            BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while ((s = br.readLine()) != null) {
                // System.out.println(s);
                credResponseList.add(s);
            }
            p.waitFor();
            System.out.println ("Exit: " + p.exitValue());
            p.destroy();

            // Write the Registration Response to a JSON file
            FileWriter writer = new FileWriter("cred_response.json");
            writer.write("{" + "\n");

            writer.write("  \"clientDataHash\":" + "\"" + credResponseList.get(2) + "\"," + "\n");
            writer.write("  \"rp\":" + "\"" + credResponseList.get(3) + "\"," + "\n");
            writer.write("  \"credentialFormat\":" + "\"" + credResponseList.get(4) + "\"," + "\n");
            writer.write("  \"authenticatorData\":" + "\"" + credResponseList.get(5) + "\"," + "\n");
            writer.write("  \"credentialID\":" + "\"" + credResponseList.get(6) + "\"," + "\n");
            writer.write("  \"attestationSignature\":" + "\"" + credResponseList.get(7) + "\"," + "\n");
            writer.write("  \"attestationCertificate\":" + "\"" + credResponseList.get(8) + "\"" + "\n");

            writer.write("}" + "\n");

            writer.flush();
            writer.close();

        } catch (Exception e) { e.printStackTrace(); }
        return credResponseList;
    }

    private static ArrayList<String> verifyCredential(String jsonFile) {
        String s;
        Process p;
        String yubikey_path = getAuthenticatorPath();
        ArrayList<String> verifyResponseList = new ArrayList<String>();
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            // Read Verify Request from the JSON file
            byte[] credRequest = Files.readAllBytes(Paths.get(jsonFile));
            Map<String,String> verifyRequestMap = new HashMap<String, String>();
            verifyRequestMap = objectMapper.readValue(credRequest, HashMap.class);

            // Write Verify Request to file in INPUT format
            FileWriter fileWriter = new FileWriter("verify_param");
            fileWriter.write(verifyRequestMap.get("clientDataHash") + "\n");
            fileWriter.write(verifyRequestMap.get("rp") + "\n");
            fileWriter.write(verifyRequestMap.get("credentialFormat") + "\n");
            fileWriter.write(verifyRequestMap.get("authenticatorData") + "\n");
            fileWriter.write(verifyRequestMap.get("credentialID") + "\n");
            fileWriter.write(verifyRequestMap.get("attestationSignature") + "\n");
            fileWriter.write(verifyRequestMap.get("attestationCertificate"));
            fileWriter.flush();
            fileWriter.close();

            // Don't need 'expect' script as manual PIN input is not required for Verify

            p = Runtime.getRuntime().exec("fido2-cred -V -i verify_param");
            BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while ((s = br.readLine()) != null) {
                System.out.println(s);
                verifyResponseList.add(s);
            }
            p.waitFor();
            System.out.println ("Exit: " + p.exitValue());
            p.destroy();

            // Write the Verify Response to a file
            FileWriter writer = new FileWriter("verify_response.json");
            writer.write("{" + "\n");

            writer.write("  \"credentialID\":" + "\"" + verifyResponseList.get(0) + "\"," + "\n");
            // This Public Key is not in proper PEM format, the header and footer are missing due to JSON multi-line
            // limitations
            writer.write("  \"publicKey\":" + "\"" + verifyResponseList.get(2));
            for (int i = 2; i < verifyResponseList.size()-1; i++) {
                writer.write(verifyResponseList.get(i));
            }
            writer.write("\"" + "\n");
            writer.write("}" + "\n");

            writer.flush();
            writer.close();

        } catch (Exception e) { e.printStackTrace(); }
        return verifyResponseList;
    }
}
