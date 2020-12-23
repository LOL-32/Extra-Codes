package com.pkg;

import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class Call_Aes_Enc_Dec {

    Encrypt_AES encrypt_aes = new Encrypt_AES();
    Decrypt_AES decrypt_aes = new Decrypt_AES();
    Scanner input = new Scanner(System.in);

    public String[] get_files_name(Path path) {
        String[] pathnames;
        File f = new File(String.valueOf(path));
        return f.list();
    }

    //ENCYPTION AES -192
    public void encrypt_aes(int option_3) throws NoSuchPaddingException, NoSuchAlgorithmException, IOException, BadPaddingException, IllegalBlockSizeException, InvalidKeyException {
        Path file_path;
        String key;
        String files;
        if (option_3 == 1) {
            label_1:
            while (true) {
                System.out.println("Enter Path of File to Encrypt : ");
                file_path = Path.of(input.nextLine());
                if (Files.exists(file_path)) {
                    break;
                } else {
                    continue label_1;
                }
            }
            label_2:
            while (true) {
                System.out.println("Enter Key : (length 24 else it will not be accepted) ");
                key = input.nextLine();
                if (key.length() == 24) {
                    break;
                } else {
                    continue label_2;
                }
            }
            Path file_name = file_path.getFileName();
            String string_file_name = file_name.toString();
            String get_file_name = string_file_name.split("\\.")[0];
            String new_file_name = get_file_name+".encrypted";
            Path folder_path = file_path.getParent();
            Path output_path = Path.of(folder_path + "\\" + new_file_name );
            encrypt_aes.encryptedFile(file_path, output_path, key,string_file_name);
        }
        else if (option_3 == 2) {
            label_1:
            while (true) {
                System.out.println("Enter Path of Folder : ");
                file_path = Path.of(input.nextLine());
                if (Files.exists(file_path)) { break; }
                else { continue label_1; }
            }
            label_2:
            while (true) {
                System.out.println("Enter Key : (length 24 else it will not be accepted) ");
                key = input.nextLine();
                if (key.length() == 24) {
                    break;
                } else {
                    System.out.println("length must be 24 for AES");
                    continue label_2;
                }
            }
            String[] file_list = get_files_name(file_path);
            String encrypted_files_out = String.valueOf(file_path + "\\" + "Encrpyted Files Using AES");
            //Files.deleteIfExists(Path.of(encrypted_files_out));

            new File(String.valueOf(encrypted_files_out)).mkdir();
            Path folder_path = file_path.getParent();
            for (int i =0; i < file_list.length ; i++){
                String get_file_name = file_list[i].split("\\.")[0];
                String new_file_name = get_file_name+".encrypted";
                Path input_path  = Path.of(file_path +"\\"+ file_list[i]);
                Path output_path = Path.of(encrypted_files_out+ "\\" + new_file_name );
                encrypt_aes.encryptedFile(input_path, output_path, key,file_list[i]);
            }
        }
    }
    //DECRYPTION AES -192
    public void decrypt_aes(int option_3) throws NoSuchPaddingException, NoSuchAlgorithmException, IOException, BadPaddingException, IllegalBlockSizeException, InvalidKeyException {
        Path file_path;
        String key;
        String files;
        if (option_3 == 1) {
            label_1:
            while (true) {
                System.out.println("Enter Path of File to Decrypt : ");
                file_path = Path.of(input.nextLine());
                if (Files.exists(file_path)) {
                    break;
                } else {
                    System.out.println("length must be 24 for AES");
                    continue label_1;
                }
            }
            label_2:
            while (true) {
                System.out.println("Enter Key : (length 24 else it will not be accepted) ");
                key = input.nextLine();
                if (key.length() == 24) {
                    break;
                } else {
                    System.out.println("length must be 24 for AES");
                    continue label_2;
                }
            }
            Path file_name = file_path.getFileName();
            String string_file_name = file_name.toString();
            String get_file_name = string_file_name.split("\\.")[0];
            String new_file_name = get_file_name+".txt";
            Path folder_path = file_path.getParent();
            Path output_path = Path.of(folder_path + "\\" + new_file_name );
            //encrypt_aes.encryptedFile(file_path, output_path, key,string_file_name);
            decrypt_aes.decryptedFile(file_path, output_path, key,string_file_name);
        }
        else if (option_3 == 2) {
            label_1:
            while (true) {
                System.out.println("Enter Path of Folder : ");
                file_path = Path.of(input.nextLine());
                if (Files.exists(file_path)) { break; }
                else { continue label_1; }
            }
            label_2:
            while (true) {
                System.out.println("Enter Key : (length 24 else it will not be accepted) ");
                key = input.nextLine();
                if (key.length() == 24) {
                    break;
                } else {
                    System.out.println("length must be 24 for AES");
                    continue label_2;
                }
            }
            String[] file_list = get_files_name(file_path);
            String encrypted_files_out = String.valueOf(file_path + "\\" + "Decrpyted Files Using AES");
            //Files.deleteIfExists(Path.of(encrypted_files_out));
            new File(String.valueOf(encrypted_files_out)).mkdir();
            Path folder_path = file_path.getParent();
            for (int i =0; i < file_list.length ; i++){
                String get_file_name = file_list[i].split("\\.")[0];
                String new_file_name = get_file_name+".txt";
                Path input_path  = Path.of(file_path +"\\"+ file_list[i]);
                Path output_path = Path.of(encrypted_files_out+ "\\" + new_file_name );
                decrypt_aes.decryptedFile(input_path, output_path, key,file_list[i]);
            }
        }
    }


}



