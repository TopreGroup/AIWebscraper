package Tagging;
//Import necessary modules

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

// Class containing main method
public class CRFExecution {

	// Main method
	public static void main(String[] args) throws IOException {

		String modelName = args[0];// "/home/sanchitsh0211/ner-model.ser.gz";
		String working_product_urls = args[1];// "/home/sanchitsh0211/working_product_urls.txt";

		Scanner scanner = new Scanner(new File(working_product_urls));

		ArrayList<String> working_product_urls_list = new ArrayList<String>();
		String lastLine = "";
		while (scanner.hasNextLine()) {
			lastLine = scanner.nextLine();
			working_product_urls_list.add(lastLine.replaceFirst(".$", ""));
		}

		if (working_product_urls_list.size() < 1) {
			System.out.println("No Product URLs");
			System.exit(0);

		}

		working_product_urls_list.remove(working_product_urls_list.size() - 1);

		working_product_urls_list.add(lastLine);

		for (String test : working_product_urls_list) {

			System.out.println("working_product_urls_list : " + test);

		}

		// Create object of CRFTagging class
		CRFTagging crftag = new CRFTagging(modelName);

		// Create object of CRFStorage class
		CRFStorage crfstore = new CRFStorage();

		// Define arraylist to store unseen text
		ArrayList<String> texts = new ArrayList<String>();

		// Define arraylist to store tagged text
		ArrayList<String> taggedStrings = new ArrayList<String>();

		// Retrieving unseen text files from path specified
		String path = "./extracted_data";
		File folder = new File(path);
		File[] listFiles = folder.listFiles();

		Arrays.sort(listFiles, new Comparator<File>() {

			public int compare(File o1, File o2) {
				int n1 = extractNumber(o1.getName());
				int n2 = extractNumber(o2.getName());
				return n1 - n2;
			}

			private int extractNumber(String name) {
				int i = 0;
				try {
					int s = name.indexOf('_') + 1;
					int e = name.lastIndexOf('.');
					String number = name.substring(s, e);
					i = Integer.parseInt(number);
				} catch (Exception e) {
					i = 0;
				}
				return i;
			}
		});

		// Iterating through all unseen text files and storing content of each text file
		// in texts arraylist
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

		// Iterating through items in texts arraylist and automatically tagging named
		// entities
		for (int i = 0; i < texts.size(); i++) {

			try {
//		for (String item : texts) {
				String temp = crftag.doTagging(crftag.getCrfmodel(), texts.get(i));
				taggedStrings.add(temp);
				System.out.println("tagged : " + temp);
			} catch (Exception e) {
				e.printStackTrace();

			}
		}

		// Writing tagged text to text files
		for (int i = 0; i < listFiles.length; i++) {

			PrintWriter writer = new PrintWriter("./tagged_data/taggedtext_" + (int) (i + 1) + ".txt");
			System.out.println("./tagged_data/taggedtext_" + (int) (i + 1) + ".txt" + " : " + taggedStrings.get(i));
			writer.print(taggedStrings.get(i));
			writer.close();
		}

		// Retrieving tagged text files from path specified
		String taggedPath = "./tagged_data";
		File taggedFolder = new File(taggedPath);
		File[] taggedFiles = taggedFolder.listFiles();

		Arrays.sort(taggedFiles, new Comparator<File>() {

			public int compare(File o1, File o2) {
				int n1 = extractNumber(o1.getName());
				int n2 = extractNumber(o2.getName());
				return n1 - n2;
			}

			private int extractNumber(String name) {
				int i = 0;
				try {
					int s = name.indexOf('_') + 1;
					int e = name.lastIndexOf('.');
					String number = name.substring(s, e);
					i = Integer.parseInt(number);
				} catch (Exception e) {
					i = 0;
				}
				return i;
			}
		});

		// Iterating through tagged text files
		// Calling extractEntity and storeEntity methods to extract and store named
		// entities from each tagged file in database
		for (int i = 0; i < taggedFiles.length; i++) {
			try {
				String brand = "";
				brand = crftag.extractEntity(taggedFiles[i], "brand");
				String model = "";
				model = crftag.extractEntity(taggedFiles[i], "model");
				String availability = "";
				availability = crftag.extractEntity(taggedFiles[i], "availability");
				String price = "";
				price = crftag.extractEntity(taggedFiles[i], "price").replace(" ", "");
				String condition = "";
				condition = crftag.extractEntity(taggedFiles[i], "condition");
				String category = "";
				category = crftag.extractEntity(taggedFiles[i], "category");
				crfstore.storeEntity(brand, model, price, availability, condition, category,
						working_product_urls_list.get(i));
			} catch (Exception e) {
				e.printStackTrace();

			}
		}

	}

}