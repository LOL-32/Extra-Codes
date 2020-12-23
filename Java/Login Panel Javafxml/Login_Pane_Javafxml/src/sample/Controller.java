package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;

public class Controller {

    //----->Variables
    @FXML
    private StackPane stackpane;
    @FXML
    private Pane Signup_pane;
    @FXML
    private TextField signup_username;
    @FXML
    private PasswordField signup_pswd;
    @FXML
    private TextField signup_email;
    @FXML
    private TextField signup_phno;
    @FXML
    private Pane Signin_Pane;
    @FXML
    private TextField signin_username;
    @FXML
    private PasswordField signin_pswd;
    //Class Object
    Database_Functions obj = new Database_Functions();
    //Msg Box
    Alert msg_box = new Alert(Alert.AlertType.NONE);
    //-----> Functions
    //->Switching Panes
    @FXML
    void Signup_mouse_function(ActionEvent event) {
        signup_username.clear();
        signup_pswd.clear();
        stackpane.getChildren().setAll(Signup_pane);
    }

    @FXML
    void back_button(ActionEvent event) {
        signin_pswd.clear();
        signin_username.clear();
        stackpane.getChildren().setAll(Signin_Pane);
    }
    //->Get Functions
    private String signup_get_username(ActionEvent event){
        String username = signup_username.getText();
        return username;
    }
    private String signup_get_password(ActionEvent event){
        String password = signup_pswd.getText();
        return password;
    }
    private String signup_get_email(ActionEvent event){
        String email = signup_email.getText();
        return email;
    }
    private String signup_get_phno(ActionEvent event){
        String phno = signup_phno.getText();
        return phno;
    }
    private String signin_get_username(ActionEvent event){
        String username = signin_username.getText();
        return username;
    }
    private String signin_get_password(ActionEvent event){
        String password = signin_pswd.getText();
        return password;
    }
    //Mouse Event
    @FXML
    void login(ActionEvent event) {
        String name = signin_get_username(null);
        String pswd = signin_get_password(null);
        boolean result = obj.Login_User(name,pswd);
        if(result == true){
            msg_box.setAlertType(Alert.AlertType.INFORMATION);
            msg_box.setContentText("Successfully Login ... !!!");
            msg_box.showAndWait();
            signin_pswd.clear();
            signin_username.clear();
        }
        else{
            msg_box.setAlertType(Alert.AlertType.ERROR);
            msg_box.setContentText("Invalid Credentials  ... !!!");
            msg_box.showAndWait();
            signin_pswd.clear();
            signin_username.clear();
        }
    }

    @FXML
    void create_acount(ActionEvent event) {
        String name = signup_get_username(null);
        String pswd = signup_get_password(null);
        String email= signup_get_email(null);
        String phno = signup_get_phno(null);
        boolean result = obj.create_acount(name,pswd,email,phno);
        if(result == true){
            msg_box.setAlertType(Alert.AlertType.INFORMATION);
            msg_box.setContentText("Account Successfully Created ... !!!");
            msg_box.showAndWait();
            back_button(null);
        }
        else{
            msg_box.setAlertType(Alert.AlertType.ERROR);
            msg_box.setContentText("Error Account Created  ... !!!");
            msg_box.showAndWait();
            signup_username.clear();
            signup_pswd.clear();
        }

    }




}


