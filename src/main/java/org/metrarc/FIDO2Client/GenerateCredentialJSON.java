package org.metrarc.FIDO2Client;

public class GenerateCredentialJSON {
    private String clientDataHash;
    private String rp_id;
    private String user_name;
    private String user_id;

    public String getClientDataHash() {
        return clientDataHash;
    }

    public String getUser_id() {
        return user_id;
    }

    public String getUser_name() {
        return user_name;
    }

    public String getRp_id() {
        return rp_id;
    }

    public void setClientDataHash(String clientDataHash) {
        this.clientDataHash = clientDataHash;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }

    public void setUser_name(String user_name) {
        this.user_name = user_name;
    }

    public void setRp_id(String rp_id) {
        this.rp_id = rp_id;
    }

    public GenerateCredentialJSON(String clientDataHash, String rp_id, String user_name, String user_id) {
        this.clientDataHash = clientDataHash;
        this.rp_id = rp_id;
        this.user_name = user_name;
        this.user_id = user_id;
    }
}
