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


public class Encrypt_AES {
    public  void encryptedFile(Path fileInputPath, Path fileOutPath, String secretKey,String file_name)
            throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IOException,
            IllegalBlockSizeException, BadPaddingException

    {
        try{
        var key = new SecretKeySpec(secretKey.getBytes(), "AES");
        var cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, key);

        var fileInput = new File(String.valueOf(fileInputPath));
        var inputStream = new FileInputStream(fileInput);
        var inputBytes = new byte[(int) fileInput.length()];
        inputStream.read(inputBytes);

        var outputBytes = cipher.doFinal(inputBytes);

        var fileEncryptOut = new File(String.valueOf(fileOutPath));
        var outputStream = new FileOutputStream(fileEncryptOut);
        outputStream.write(outputBytes);

        inputStream.close();
        outputStream.close();
        String get_file_name = file_name.split("\\.")[0];
        System.out.println("Done! File " + file_name +" is encrypted using AES-192" +" Successfully encrypted! " +
                "... New Name is -> "+ get_file_name + ".encrypted");
        }
        catch (Exception e){
            System.out.println("File " + file_name +" is NOT encrypted using AES-192 ..it is a folder..");
        }
    }


}
