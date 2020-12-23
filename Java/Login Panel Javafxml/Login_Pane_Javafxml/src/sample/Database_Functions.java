package sample;

import javafx.fxml.FXML;

import java.sql.*;

public class Database_Functions {

    //--->variables
    private Connection cn;
    private Statement s;

    //--->Function
    public boolean Login_User(String username , String pswd){
        try {
            String db_username = null;
            String db_password = null;
            cn = DriverManager.getConnection("jdbc:mysql://localhost:3306/loginpanel?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC","root","");
            String login_Query = "SELECT * FROM login WHERE username= ? and pswd = ?";
            PreparedStatement statement = cn.prepareStatement(login_Query);
            statement.setString(1, username);
            statement.setString(2, pswd);
            ResultSet result = statement.executeQuery();
            if (result.next()) { return true; }
            else{
                String login_sec_Query = "SELECT * FROM login WHERE email= ? and pswd = ?";
                PreparedStatement statement_2 = cn.prepareStatement(login_sec_Query);
                statement_2.setString(1, username);
                statement_2.setString(2, pswd);
                ResultSet result_2 = statement_2.executeQuery();
                if (result_2.next()) {return true;}
            }
        }
        catch(SQLException e){
            e.printStackTrace();
        }
        return false;
    }

    @FXML
    public boolean create_acount(String username,String pswd,String email,String phno) {
        try {
            cn = DriverManager.getConnection("jdbc:mysql://localhost:3306/loginpanel?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC","root","");
            String Inert_Query = "INSERT into login VALUES('"+username+"','"+pswd+"','"+email+"','"+phno+"')";
            s= cn.createStatement();
            s.execute(Inert_Query);
            return true;
        }
        catch(SQLException e){
            e.printStackTrace();
        }
        return false;
    }


}
