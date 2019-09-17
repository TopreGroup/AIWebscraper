package Tagging;

//Import the necessary modules
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Connection;
//import java.sql.ResultSet;
//import java.sql.SQLException;
import java.sql.Statement;

// Class to store extracted named entities in database
public class CRFStorage {
	
	// Method to store extracted named entities in database
	public void storeEntity(int id, String brand, String model, String price, String availability, String condition) {
		
		Connection conn = null;
		PreparedStatement stmt = null;
		
		String dbUrl = "jdbc:sqlserver://DESKTOP-1P8QTPD;user=Sanchit12;password=GSWarrior02;database=CRFTest";
		
		try {
			// Setting up connection to database
			
			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver").newInstance();
            conn = DriverManager.getConnection(dbUrl);
			conn.setAutoCommit(false);
		
			// Inserting extracted named entities into entities table of database
			
			String sql = "UPDATE ENTITIES SET brand = ?, model = ?, price = ?, stock = ?, condition = ? WHERE entity_id = ?;";
			stmt = conn.prepareStatement(sql);
			stmt.setString(1, brand);
			stmt.setString(2, model);
			stmt.setString(3, price);
			stmt.setString(4, availability);
			stmt.setString(5, condition);
			stmt.setInt(6, id);
			stmt.executeUpdate();
			stmt.close();

			// Committing changes made
			conn.commit();

			// Closing database connection
			conn.close();
		} catch (Exception e) {
			System.err.println(e.getClass().getName() + ": " + e.getMessage());
			System.exit(0);
		}
	}
}
