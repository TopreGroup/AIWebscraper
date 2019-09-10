package Tagging;

// Import the necessary module
import edu.stanford.nlp.ie.crf.CRFClassifier;

// Class to automatically identify named entities from unseen text
public class CRFTagging {
	
	// Create object of CRFModel class
	CRFModel crf = new CRFModel();
	
	// Use object to retrieve the trained CRF Classifier
	CRFClassifier crfmodel = crf.getModel("ner-model.ser.gz");
	
	// Method to identify named entities from unseen text
	public void doTagging(CRFClassifier model, String input) {
		  input = input.trim();
		  System.out.println(input + "=>"  +  model.classifyToString(input));
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// Create object of CRFTagging class
		CRFTagging crftag = new CRFTagging();
		
		// Specify unseen text 
		String[] tests = new String[] {"Lenovo ThinkPad X1 Carbon 20KH 8GB 14\" Ultrabook\r\n" + 
				"Price: $849% Free shipping Today!\r\n" + 
				"40977145\r\n" + 
				"ADD EXTRA PROTECTION\r\n" + 
				"Lenovo Priority - Technical support - phone consulting - 3 years - 24x7 - for ThinkPad P40 Yoga; P50; P51; P70; X1 Carbon; X1 Tablet; X1 Yoga; ThinkPad\r\n" + 
				"‘Yoga 260; 460 (SWS0E97113)$69.00\r\n" + 
				"Lenovo 3-Yr Next Business Day Onsite with Premier Support Service for ThinkPad E440; E46X; E47X; E540; ES6X; E57X; ThinkPad Edge E145; £445;\r\n" + 
				"E545 (SWS0M90348)$69.00\r\n" + 
				"Lenovo ThinkPad X1 Carbon 20KH Ultrabook - Intel Core i5-8250U\r\n" + 
				"1.6GHz, 8GB LPDDR3, 256GB SSD, 14\" LED FHD 1920x1080, UHD\r\n" + 
				"Graphics 620, 2x Thunderbolt 3, BT 4.1, Win 10 Pro 64-bit -\r\n" + 
				"20KH002SUS\r\n" + 
				"Item#: 40977143 | Model#: 20KHOO2SUS\r\n" + 
				"List Price:\r\n" + 
				"$1,699.99\r\n" + 
				"Instant Savings:\r\n" + 
				"- $850.00 (50%)\r\n" + 
				"Price:\r\n" + 
				"58495°Free Shipping Today!\r\n" + 
				"In Stock. Usually ships next business day."};
		
		// Identify named entities from unseen text
		for (String item : tests) {
		  crftag.doTagging(crftag.crfmodel, item);
		}
	}
}
