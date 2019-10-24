package Tagging;

//Import the necessary modules
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Connection;

// Class to store extracted named entities in database
public class CRFStorage {

	public String safeChar(String first) {

		String result = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";

		if (result.contains(first)) {

			return first;

		}

		return "";
	}

	// Method to store extracted named entities in database
	public void storeEntity(String brand, String model, String price, String availability, String condition,
			String category, String prodURL) {

		System.out.println("brand" + brand);
		System.out.println("model" + model);
		System.out.println("price" + price);
		System.out.println("availability" + availability);
		System.out.println("condition" + condition);
		System.out.println("category" + category);
		System.out.println("prodURL" + prodURL);
		System.out.println("-_-_-_-");

		Connection conn = null;
		PreparedStatement pstmt = null;

		String dbUrl = "jdbc:sqlserver://devdb.trunked.com.au;user=trunkedproject;password=rmitProject@trunked;database=trunkedproject";// "jdbc:sqlserver://DESKTOP-1P8QTPD;user=Sanchit12;password=GSWarrior02;database=CRFTest";

		try {
			// Setting up connection to database

			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver").newInstance();
			conn = DriverManager.getConnection(dbUrl);
			conn.setAutoCommit(false);

			// Inserting extracted named entities into entities table of database
			String sql = "UPDATE ENTITIES SET brand = ?, model = ?, price = ?, stock = ?, condition = ?, category = ? WHERE producturl = ?;";
			pstmt = conn.prepareStatement(sql);
//			pstmt.setString(1, brand);
//			pstmt.setString(2, model);
//			pstmt.setString(3, price);
//			pstmt.setString(4, availability);
//			pstmt.setString(5, condition);
//			pstmt.setString(6, category);
//			pstmt.setString(7, prodURL);
//			pstmt.executeUpdate();
//			pstmt.close();

			if (brand.length() > 1) {
				pstmt.setString(1, safeChar((brand.replace(brand.substring(1), ""))) + (brand.substring(1)));
			} else {
				pstmt.setString(1, brand);
			}

			if (model.length() > 1) {
				pstmt.setString(2, safeChar((model.replace(model.substring(1), ""))) + (model.substring(1)));
			} else {
				pstmt.setString(2, model);
			}

			pstmt.setString(3, price);

			if (availability.length() > 1) {
				pstmt.setString(4,
						safeChar((availability.replace(availability.substring(1), ""))) + (availability.substring(1)));
			} else {
				pstmt.setString(4, availability);
			}

			if (condition.length() > 1) {
				pstmt.setString(5,
						safeChar((condition.replace(condition.substring(1), ""))) + (condition.substring(1)));
			} else {
				pstmt.setString(5, condition);
			}

			if (category.length() > 1) {
				pstmt.setString(6, safeChar((category.replace(category.substring(1), ""))) + (category.substring(1)));
			} else {
				pstmt.setString(6, category);
			}

			pstmt.setString(7, prodURL);

			pstmt.executeUpdate();
			pstmt.close();

			// Committing changes made
			conn.commit();

			// Closing database connection
			conn.close();
		} catch (Exception e) {
			e.printStackTrace();
//			System.exit(0);
		}
	}
}
