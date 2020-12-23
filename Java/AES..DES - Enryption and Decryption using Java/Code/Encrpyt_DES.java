package com.pkg;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class Encrpyt_DES {
    public  void encryptedFile(Path fileInputPath, Path fileOutPath, String secretKey, String file_name)
            throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IOException,
            IllegalBlockSizeException, BadPaddingException

    {
        try{
            var key = new SecretKeySpec(secretKey.getBytes(), "DES");
            var cipher = Cipher.getInstance("DES");
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
            System.out.println("Done! File " + file_name +" is encrypted using DES-64" +" Successfully encrypted! " +
                    "... New Name is -> "+ get_file_name + ".encrypted");
        }
        catch (Exception e){
            System.out.println("File " + file_name +" is NOT encrypted using DES-64 ..it is a folder..");
            System.out.println(e.getMessage());
        }
    }


}
