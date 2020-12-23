package com.pkg;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.nio.file.Path;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class Decrypt_DES {
    public  void decryptedFile(Path fileInputPath, Path fileOutPath, String secretKey, String file_name)
            throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IOException,
            IllegalBlockSizeException, BadPaddingException, FileNotFoundException

    {
        try {
            //String secretKey = "jackrutorial.com";
            var key = new SecretKeySpec(secretKey.getBytes(), "DES");
            var cipher = Cipher.getInstance("DES");
            cipher.init(Cipher.DECRYPT_MODE, key);

            var fileInput = new File(String.valueOf(fileInputPath));
            var inputStream = new FileInputStream(fileInput);
            var inputBytes = new byte[(int) fileInput.length()];
            inputStream.read(inputBytes);

            byte[] outputBytes = cipher.doFinal(inputBytes);

            var fileEncryptOut = new File(String.valueOf(fileOutPath));
            var outputStream = new FileOutputStream(fileEncryptOut);
            outputStream.write(outputBytes);

            inputStream.close();
            outputStream.close();
            String get_file_name = file_name.split("\\.")[0];
            System.out.println("Done! File " + file_name +" is Decrypted using DES-64" +" Successfully Decrypted! " +
                    "... New Name is -> "+ get_file_name + ".txt");
        }
        catch (Exception e) {
            System.out.println("File " + file_name +" is NOT decrypted using DES-64 ..it is a folder..");
        }

    }
}
