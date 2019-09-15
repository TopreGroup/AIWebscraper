package Tagging;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.*;

// Import the necessary module
import edu.stanford.nlp.ie.crf.CRFClassifier;

// Class to automatically identify named entities from unseen text
public class CRFTagging {

	// Create object of CRFModel class
	CRFModel crf = new CRFModel();

	// Use object to retrieve the trained CRF Classifier
	CRFClassifier crfmodel = crf.getModel("ner-model.ser.gz");

	// Method to identify named entities from unseen text
	public String doTagging(CRFClassifier model, String input) {
		input = input.trim();
		return (model.classifyToString(input));
	}

	// public String extractBrand(File file) throws FileNotFoundException {
	// String brand = "";
	// boolean brandFound = false;
	// Scanner sc = new Scanner(file);
	//
	// while (sc.hasNextLine()) {
	// if (brandFound != true) {
	// String currentLine = sc.nextLine();
	// if (currentLine.contains("/brand")) {
	// String[] tags = currentLine.split(" ");
	// tags = new LinkedHashSet<String>(Arrays.asList(tags)).toArray(new String[0]);
	// for (int i = 0; i < tags.length; i++) {
	// if (tags[i].split("/")[1].contains("brand")) {
	// brand = tags[i].split("/")[0];
	// brandFound = true;
	// break;
	// }
	// }
	// }
	//
	// }
	//
	// else {
	// break;
	// }
	// }
	//
	// return brand;
	// }
	//

	public String extractEntity(File file, String entityName) throws FileNotFoundException {
		String entity = "";
		boolean entityFound = false;
		Scanner sc = new Scanner(file);

		if (entityName == "brand") {
			while (sc.hasNextLine()) {
				if (entityFound != true) {
					String currentLine = sc.nextLine();
					if (currentLine.contains("/brand")) {
						String[] tags = currentLine.split(" ");
						tags = new LinkedHashSet<String>(Arrays.asList(tags)).toArray(new String[0]);
						for (int i = 0; i < tags.length; i++) {
							if (tags[i].split("/")[1].contains("brand")) {
								entity = tags[i].split("/")[0];
								entityFound = true;
								break;
							}
						}
					}

				}

				else {
					break;
				}
			}

		}

		else {
			while (sc.hasNextLine()) {
				if (entityFound != true) {
					String currentLine = sc.nextLine();
					if (currentLine.contains("/" + entityName)) {
						String[] tags = currentLine.split(" ");
						tags = new LinkedHashSet<String>(Arrays.asList(tags)).toArray(new String[0]);
						for (int i = 0; i < tags.length; i++) {
							if (tags[i].split("/")[1].contains(entityName)) {
								entity += tags[i].split("/")[0] + " ";

							}
						}

						entityFound = true;
					}

				}

				else {
					break;
				}
			}
		}

		return entity;
	}

	public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException {
		// TODO Auto-generated method stub

		// Create object of CRFTagging class
		CRFTagging crftag = new CRFTagging();
		String taggedString = "";
		PrintWriter writer = new PrintWriter("sample.txt", "utf-8");

		// Specify unseen text
		String[] tests = new String[] {
				"‘YOUR SHOPPING CART IS EMPTY. ADD ITEMS TO YOUR CART AND THEY WILL APPEAR HERE.\r\n"
						+ "APPLE IPHONE 8 64GB SPACE GREY UNLOCKED SMARTPHONE | B-GRADE 6MTH\r\n" + "WTY\r\n"
						+ "SKU: 59002-B\r\n" + "$609.00\r\n" + "RRP $749.00\r\n" + "SAVE $140.00\r\n" + "IN STOCK\r\n"
						+ "FEATURES\r\n"
						+ "PROFESSIONALLY REFURBISHED 6MTH WARRANTY 64GB/SPACE GREY 64GB SPACE GREY UNLOCKED ADAPTER AND CABLE INCLUDED (AFTERMARKET) FREE SHIPPING 3 MTH\r\n"
						+ "WARRANTY\r\n" + "AVAILABLE OPTIONS\r\n" + "EXTEND WARRANTY (12MTHS)\r\n" + "QUANTITY:\r\n"
						+ "SHARE:\r\n" + "NOTIFY ME WHEN BACK IN STOCK\r\n"
						+ "ASK US ABOUT ‘APPLE IPHONE 8 64GB SPACE GREY UNLOCKED SMARTPHONE | B-GRADE 6MTH WTY’\r\n"
						+ "FREE\r\n" + "UNLIMITED TECHNICAL SUPPORT ON ALL ITEMS\r\n" + "FAST\r\n"
						+ "AUSTRALIA WIDE SHIPPING\r\n" + "WARRANTY\r\n" + "ON EVERY ITEM FOR YOUR PEACE OF MIND\r\n"
						+ "APPLE IPHONE 8 MODELS HAVE A 4.7\" (DIAGONAL) WIDESCREEN MULTITOUCH \"TRUE TONE” LED-BACKLIT 1334X750 NATIVE RESOLUTION\r\n"
						+ "“RETINA HD\" DISPLAY (326 PPI, 625 CD/M2) AND A TAPTIC-ENGINE POWERED SOLID STATE \"CLICKLESS\" HOME BUTTON. IT HAS DUAL CAMERAS -\r\n"
						+ "- A REAR 12-MEGAPIXEL 4K CAMERA WITH OPTICAL IMAGE STABILIZATION, A F/1.8 APERTURE, A 6-ELEMENT LENS AND WIDE COLOR CAPTURE -- AS\r\n"
						+ "WELL AS A FRONT 7-MEGAPIXEL \"FACETIME HD\" CAMERA WITH SUPPORT FOR 1080P VIDEO. THE CAMERAS SUPPORT MOTION TRACKING AND OFFER\r\n"
						+ "AUGMENTED REALITY SUPPORT, TOO.\r\n"
						+ "THE IPHONE 8 USES AN \"AEROSPACE-GRADE\" ALUMINUM ALLOY CASE REINFORCED BY STEEL AND HAS A GLASS FRONT AND BACK. IT IS SPLASH, WATER, AND DUST-\r\n"
						+ "- GOLD, SILVER, OR A DARK \"SPACE GRAY\", BUT ON APRIL 9, 2018, APPLE ALSO ADDED A (PRODUCT) RED SPECIAL EDITION MODEL TO THE LINEUP WITH A\r\n"
						+ "BLACK FRONT AND A RED BACK. INTERNALLY, THE IPHONE 8 IS POWERED BY A 64-BIT \"APPLE A11 BIONIC\" PROCESSOR WITH SIX CORES -- TWO PERFORMANCE\r\n"
						+ "CORES AND FOUR HIGH-EFFICIENCY CORES -- AND HAS 2 GB OF RAM, AS WELL AS 64 GB OR 256 GB OF FLASH STORAGE.\r\n"
						+ "IT ALSO SUPPORTS 802.11AC WI-FI WITH MIMO, BLUETOOTH 5.0, LTE (4G), AND NFC FOR APPLE PAY. APPLE ESTIMATES THAT THE IPHONE 8 PROVIDES \"UP\r\n"
						+ "DEVICE'S GLASS BACK, THE BATTERY CAN BE CHARGED WIRELESSLY USING A CHARGING MAT THAT SUPPORTS THE QI STANDARD.\r\n"
						+ "NOTE: THIS ITEM IS CLASSIFIED AS B-GRADE DUE TO COSMETIC IMPERFECTIONS. THIS ITEM WILL HAVE SOME MINOR\r\n"
						+ "SRATCHES ON THE SCREEN AND/OR CASING.\r\n" + "GENERAL\r\n" + "BRAND\r\n" + "MODEL\r\n"
						+ "STYLE SMARTPHONE\r\n" + "STORAGE CAPACITY 64GB\r\n" + "SCREEN SIZE AR\r\n"
						+ "MAX. RESOLUTION 750X1334\r\n" + "OTHER\r\n" + "LOCK STATUS UNLOCKED\r\n" + "SOFTWARE\r\n"
						+ "OPERATING SYSTEM\r\n" + "PHYSICAL\r\n" + "DIMENSIONS 138 4MMX67.3MMX7.3MM\r\n"
						+ "WEIGHT 148KGS\r\n" + "WE ALSO RECOMMEND\r\n" + "$19.95 20% OFF RRP\r\n"
						+ "$29.95 23% OFF RRP\r\n" + "$29.00 77% OFF RRP\r\n" + "OTHERS ALSO BOUGHT\r\n"
						+ "$769.00 4% OFF RRP\r\n" + "$749.00 6% OFF RRP\r\n" + "$349.00 13% OFF RRP\r\n"
						+ "$399.00 13% OFF RRP\r\n" + "$519.00 13% OFF RRP\r\n" + "$359.00 28% OFF RRP\r\n"
						+ "MORE FROM THIS CATEGORY\r\n" + "$389.00 22% OFF RRP\r\n" + "$285.00 18% OFF RRP\r\n"
						+ "$1,039.00 13% OFF RRP\r\n"
						+ "WE PAY A LOT OF ATTENTION TO DETAIL AROUND HERE. EVERY SINGLE ITEM IS INDIVIDUALLY INSPECTED, ACCURATELY GRADED, CLEANED AS NEEDED AND CAREFILLY PACKED AND SHIPPED\r\n"
						+ "‘PROMPTLY. IF YOU EVER FEEL THAT SOMETHING WAS EITHER NOT PORTRAYED ACCURATELY OR ARRIVES IN A CONDITION OTHER THAN YOU EXPECTED, PLEASE CONTACT US IMMEDIATELY! WE\r\n"
						+ "ALWAYS/ WANT YOU TO BE HAPPY WITH YOUR PURCHASE AND OFFER A 100% SATISFACTION GUARANTEE.\r\n"
						+ "STAY IN TOUCH\r\n" + "SUBSCRIBE TO OUR NEWSLETTER TO GET EXCLUSIVE DEALS AND UPDATES!\r\n"
						+ "STAY CONNECTED\r\n" + "PAYMENT OPTIONS\r\n" + "SERVICE\r\n" + "ABOUT US\r\n"
						+ "INFORMATION\r\n" + "REBOOT IT" };

		for (int i = 0; i < tests.length; i++) {
			tests[i] = tests[i].replace("$", "$ ");
		}

		// Identify named entities from unseen text
		for (String item : tests) {

			taggedString = crftag.doTagging(crftag.crfmodel, item);

		}

		writer.print(taggedString);
		writer.close();

		File file = new File("sample.txt");
		String brand = crftag.extractEntity(file, "brand");
		String model = crftag.extractEntity(file, "model");
		String availability = crftag.extractEntity(file, "availability");
		String price = crftag.extractEntity(file, "price").replace(" ", "");
		System.out.println(brand);
		System.out.println(model);
		System.out.println(availability);
		System.out.println(price);

	}
}
