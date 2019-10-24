# AI Product Information Extractor

The **AI Product Information Extractor** implements **Named Entity Recognition** to extract key entities from product webpages of electronics websites using the **CRF Classifer** machine learning model. The entities extracted are:

* Brand
* Model
* Price
* Availability
* Condition 
* Category

## Python Dependencies

* Flask (Version 1.1.1)
* WTForms (Version 2.2.1)
* python-tds (Version 1.9.1)
* bs4 (Version 0.0.1)
* lxml (Version 4.4.1)
* google-api-python-client (Version 1.7.11)
* google-api-core (Version 1.14.3)
* google-api-python-client (Version 1.7.11)
* google-auth (Version 1.6.3)
* google-auth-httplib2 (Version 0.0.3)
* google-cloud (Version 0.34.0)
* google-cloud-core (Version 1.0.3)
* google-cloud-storage (Version 1.20.0)
* google-compute-engine (Version 2.8.16)
* google-resumable-media (Version 0.4.1)
* googleapis-common-protos (Version 1.6.0)

## Java Dependencies

Execution of the java code contained within the **src** folder requires the following jar files:

* stanford-corenlp-3.9.2.jar
* stanford-corenlp-models-current.jar
* stanford-english-corenlp-models-current.jar
* stanford-english-kbp-corenlp-models-current.jar

The above jar files can be downloaded from the following link: https://drive.google.com/drive/folders/1kCyrHp7X9sWqdx9QnLN6Q6ssVFD1Ii8-?usp=sharing

**Note:** After adding these jar files to the build path, the java code within the **src** folder must be converted into a jar file called **crf.jar** to allow for the integration with Python. 

