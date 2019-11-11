package org.metrarc.FIDO2Client;

import java.io.IOException;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter PIN: ");
        String s = in.nextLine();
        System.out.println("You entered string " + s);

        String name = System.console().readLine();
        System.out.println(name);
    }
}
