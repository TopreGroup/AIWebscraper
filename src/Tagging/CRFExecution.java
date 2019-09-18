package Tagging;

// Import necessary modules
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

// Class containing main method
public class CRFExecution {

	// Main method
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		// Create object of CRFTagging class
		CRFTagging crftag = new CRFTagging();

		// Create object of CRFStorage class
		CRFStorage crfstore = new CRFStorage();

		// Define arraylist to store unseen text
		List<String> texts = new ArrayList<String>();

		// Define arraylist to store tagged text
		List<String> taggedStrings = new ArrayList<String>();

		// Retrieving unseen text files from path specified
		String path = "./extracted_data";
		File folder = new File(path);
		File[] listFiles = folder.listFiles();

		// Iterating through all unseen text files and storing content of each text file in texts arraylist
		for (int i = 0; i < listFiles.length; i++) {
			StringBuilder builder = new StringBuilder();
			BufferedReader br = new BufferedReader(new FileReader(listFiles[i]));
			String st;
			while ((st = br.readLine()) != null) {
				builder.append(st + "\n");
			}

			texts.add(builder.toString().replace("$", "$ "));

			br.close();
		}

		// Iterating through items in texts arraylist and automatically tagging named entities
		for (String item : texts) {

			taggedStrings.add(crftag.doTagging(crftag.crfmodel, item));

		}

		// Writing tagged text to text files
		for (int i = 0; i < listFiles.length; i++) {
			PrintWriter writer = new PrintWriter("./tagged_data/tagged_text" + (int) (i + 1) + ".txt");
			writer.print(taggedStrings.get(i));
			writer.close();
		}

		// Retrieving tagged text files from path specified
		String taggedPath = "./tagged_data";
		File taggedFolder = new File(taggedPath);
		File[] taggedFiles = taggedFolder.listFiles();

		// Iterating through tagged text files
		// Calling extractEntity and storeEntity methods to extract and store named entities from each tagged file in database
		for (int i = 0; i < taggedFiles.length; i++) {
			String brand = crftag.extractEntity(taggedFiles[i], "brand");
			String model = crftag.extractEntity(taggedFiles[i], "model");
			String availability = crftag.extractEntity(taggedFiles[i], "availability");
			String price = crftag.extractEntity(taggedFiles[i], "price").replace(" ", "");
			String condition = crftag.extractEntity(taggedFiles[i], "condition");
			String category = crftag.extractEntity(taggedFiles[i], "category");
			crfstore.storeEntity(i + 1, brand, model, price, availability, condition, category);

		}

	}

}
