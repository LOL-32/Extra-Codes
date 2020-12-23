package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("fxml//LoginPanel(fxml).fxml"));
        primaryStage.setTitle("Login Panel | https://www.rohanfarooqui.wordpress.com | Github : /LOL-32");
        primaryStage.setResizable(false);
        Image icon = new Image(getClass().getResourceAsStream("images/icon.png"));
        primaryStage.getIcons().add(icon);
        primaryStage.setScene(new Scene(root, 951, 517));
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
