package com.pkg;

/*

Author  : M.ROHAN FAROOQUI ©2020
Website : rohanfarooqui.wordpress.com
Blog    : rohanfarooqui.blogpsot.com
Youtube : https://www.youtube.com/channel/UCfhrKxBa0qB6-doJVzKsI8Q/ 

*/
import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.swing.plaf.synth.SynthTextAreaUI;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;



public class Main {

    static Call_Aes_Enc_Dec call_aes_enc_dec= new Call_Aes_Enc_Dec();
    static Call_Des_Enc_Dec call_des_enc_dec= new Call_Des_Enc_Dec();

    public static void main(String[] args) throws NoSuchPaddingException, NoSuchAlgorithmException, IOException, BadPaddingException, IllegalBlockSizeException, InvalidKeyException, URISyntaxException {
        Scanner input = new Scanner(System.in);
        int option_1;
        int option_2;
        int option_3;
        label_1:
        while (true) {
            System.out.println("                     A SYMMETRIC CRYPTO SYSTEM");
            System.out.println("==========================================================================");
            System.out.println("                              MAIN MENU");
            System.out.println("                        ----------------------");
            System.out.println("                              1. Encrypt");
            System.out.println("                              2. Decrypt");
            System.out.println("                              3. Exit");
            System.out.println("                        ----------------------");
            System.out.println("Enter your option : ");
            option_1 = input.nextInt();
            if (option_1 > 0 && option_1 < 3) {
                break;
            }
            else if (option_1 == 3){
                System.exit(0);
            }
            else {
                System.out.println("Invalid Choice .. !!");
                continue label_1;
            }
        }
        label_2:
        while (true) {
            System.out.println("                        ----------------------");
            System.out.println("                           Choose Algorithm");
            System.out.println("                        ----------------------");
            System.out.println("                                (1) AES");
            System.out.println("                                (2) DES");
            System.out.println("                        ----------------------");
            System.out.println("Enter your option : ");
            option_2 = input.nextInt();
            if (option_2 > 0 && option_2 < 3) {
                break;
            } else {
                System.out.println("Invalid Choice .. !!");
                continue label_2;
            }
        }
        label_3:
        while (true) {
            System.out.println("                        ----------------------");
            System.out.println("                           Enter Your Choice");
            System.out.println("                        ----------------------");
            System.out.println("                                (1) File");
            System.out.println("                               (2) Folder");
            System.out.println("                        ----------------------");
            System.out.println("Enter your option : ");
            option_3 = input.nextInt();
            if (option_3 > 0 && option_3 < 3) {
                break;
            } else {
                System.out.println("Invalid Choice .. !!");
                continue label_3;
            }
        }
        if(option_1 == 1 && option_2 == 1){
            call_aes_enc_dec.encrypt_aes(option_3);
        }
        else if(option_1 == 2 && option_2 == 1){
            call_aes_enc_dec.decrypt_aes(option_3);
        }
        else if(option_1 == 1 && option_2 == 2){
            call_des_enc_dec.encrypt_des(option_3);
        }
        else if(option_1 == 2 && option_2 == 2){
            call_des_enc_dec.decrypt_des(option_3);
        }
        

    }

}
