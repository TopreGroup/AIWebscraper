package Tagging;

// Import the necessary module
import edu.stanford.nlp.ie.crf.CRFClassifier;

// Class to retrieve trained model 
public class CRFModel {
	
	// Method to retrieve trained model
	public CRFClassifier getModel(String modelPath) {
	    return CRFClassifier.getClassifierNoExceptions(modelPath);
	}

}
