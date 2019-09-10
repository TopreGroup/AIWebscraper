//Import necessary modules
import java.util.Properties;

import edu.stanford.nlp.ie.crf.CRFClassifier;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.sequences.SeqClassifierFlags;
import edu.stanford.nlp.util.StringUtils;

// Class to train CRF classifier using properties defined in NER.prop
// Trained model is saved as a ser.gz file 
public class CRFImplementation {
	
	public static void main(String [] args) {
		// Define the properties file to be used to train the CRF classifier
		args = new String[] {"-props", "NER.prop"};
		try {
			// Train the CRF classifier
			CRFClassifier.main(args);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}