package Tagging;

//Import the necessary modules
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

// Import the necessary module
import edu.stanford.nlp.ie.crf.CRFClassifier;

// Class to automatically identify and extract named entities from unseen text
public class CRFTagging {

	private CRFModel crf;
	private CRFClassifier crfmodel;

	public CRFTagging(String myModelPath) {

		// Create object of CRFModel class
		crf = new CRFModel();

		// Use object to retrieve the trained CRF Classifier
		crfmodel = crf.getModel(myModelPath);

	}

	// Method to identify named entities from unseen text
	public String doTagging(CRFClassifier model, String input) {
		input = input.trim();
		return (model.classifyToString(input));
	}

	// Method to extract named entities from tagged files
	public String extractEntity(File file, String entityName) throws FileNotFoundException {
		String entity = "";
		boolean entityFound = false;
		Scanner sc = new Scanner(file);

		// Code to extract brand
		// Parses tagged file line by line and checks if current line contains string
		// tagged as brand
		// If string is tagged as brand, it is stored in entity variable and returned
		if (entityName == "brand") {
			while (sc.hasNextLine()) {
				try {
					if (entityFound != true) {
						String currentLine = sc.nextLine();
						if (currentLine.contains("/brand")) {
							String[] tags = currentLine.split(" ");
							tags = new LinkedHashSet<String>(Arrays.asList(tags)).toArray(new String[0]);
							for (int i = 0; i < tags.length; i++) {
								if (tags[i].split("/").length > 1) {
									if (tags[i].split("/")[1].contains("brand")) {
										entity = tags[i].split("/")[0];
										entityFound = true;
										break;
									}
								}
							}
						}

					}

					else {
						break;
					}
				} catch (Exception e) {
					e.printStackTrace();

				}
			}

		}

		// Code to extract named entities other than brand
		// Parses tagged file line by line and checks if current line contains strings
		// tagged as the named entity to be extracted
		// If string is tagged as the named entity to be extracted, it is stored in
		// entity variable and returned
		// If multiple strings in the line are tagged as the named entity to be
		// extracted, they are concatenated, stored in the entity variable and returned
		else {
			while (sc.hasNextLine()) {
				try {
					if (entityFound != true) {
						String currentLine = sc.nextLine();
						if (currentLine.contains("/" + entityName)) {
							String[] tags = currentLine.split(" ");
							tags = new LinkedHashSet<String>(Arrays.asList(tags)).toArray(new String[0]);
							for (int i = 0; i < tags.length; i++) {
								if (tags[i].split("/").length > 1) {
									if (tags[i].split("/")[1].contains(entityName)) {
										entity += tags[i].split("/")[0] + " ";

									}
								}
							}

							entityFound = true;
						}

					}

					else {
						break;
					}
				} catch (Exception e) {
					e.printStackTrace();

				}
			}
		}

		return entity;
	}

	public CRFModel getCrf() {
		return crf;
	}

	public void setCrf(CRFModel crf) {
		this.crf = crf;
	}

	public CRFClassifier getCrfmodel() {
		return crfmodel;
	}

	public void setCrfmodel(CRFClassifier crfmodel) {
		this.crfmodel = crfmodel;
	}

}
