package Tagging;

//Import the necessary modules
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

// Class to store extracted named entities in database
public class CRFStorage {

	// Method to store extracted named entities in database
	public void storeEntity(int id, String brand, String model, String price, String availability) {

		Connection conn = null;
		Statement stmt = null;
		try {
			// Setting up connection to database
			Class.forName("org.postgresql.Driver");
			conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/CRFTest", "postgres", "SanSak12$");
			conn.setAutoCommit(false);

			// Inserting extracted named entities into entities table of database
			stmt = conn.createStatement();
			String sql = "INSERT INTO ENTITIES (Entity_ID, Brand , Model, Price, Availability)" + "VALUES (" + id + ","
					+ "'" + brand + "'" + "," + "'" + model + "'" + "," + "'" + price + "'" + "," + "'" + availability
					+ "'" + ");";
			stmt.executeUpdate(sql);
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
