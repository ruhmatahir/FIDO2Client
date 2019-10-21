package org.metrarc.FIDO2Client;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class JSONManager {
    public static void main(String[] args) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();

//        GenerateCredentialJSON genCred = new GenerateCredentialJSON("YS7vEspph7MWwGGLOiQhpDx+WYyKmS86ROGFPD99AnE=",
//                "metrarc.com", "ruhma", "5JCyQJlKQW0yB0xwNIf/J5fpHhqks8bAT95Rs5Rp7xk=");
//        objectMapper.writeValue(new File("target/cred_param.json"), genCred);

        // Read JSON from file
//        GenerateCredentialJSON genCred = objectMapper.readValue(new File("target/cred_param.json"), GenerateCredentialJSON.class);
//        String credRequestAsString = objectMapper.writeValueAsString(genCred);
//        System.out.println(credRequestAsString);

        byte[] mapCredRequest = Files.readAllBytes(Paths.get("target/cred_param.json"));
        Map<String,String> credRequestMap = new HashMap<String, String>();
        credRequestMap = objectMapper.readValue(mapCredRequest, HashMap.class);
        System.out.println("username : " + credRequestMap.get("user_name"));
    }
}
