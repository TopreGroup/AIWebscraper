""" Import the necessary modules """
import pytds
import subprocess
import glob
import os
from google.cloud import storage

def storeProdURL(name):

    business_id = 0

    """ Specify the inputted business name """
    business_name = name
    
    """ Establish connection to microsoft sql server """
    conn = conn = pytds.connect('devdb.trunked.com.au', 'trunkedproject', 'trunkedproject', 'rmitProject@trunked')

    cur = conn.cursor()
    
    bucket_name = "crfmodel"
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    """ Reading lines from working product urls text file """
    file_lines = []
    
    with open("working_product_urls.txt", "r") as fs:
        for line in fs:
            currentLine = line.rstrip().split(',')
            file_lines.append(currentLine)

    """ Extracting and storing working product urls """
    urls = []
    for fl in file_lines:
        urls.append(fl[0])

    """ Converting working product urls list to set """
    urls = sorted(set(urls), key=urls.index)

    """ Retrieve business id for the inputted business name """
    cur.execute("SELECT business_id from BUSINESSES WHERE CONVERT(varchar, business_name) = " + "'" + business_name + "'" + ";")
    business_id = cur.fetchone()[0]

    """ Loop through all working product urls and store them in the database """
    for url in urls:
        postgres_insert_query = """SET ANSI_WARNINGS OFF; INSERT INTO ENTITIES (brand, model, price, stock, producturl, condition, category, business_id) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s); SET ANSI_WARNINGS ON; """
        record_to_insert = ('', '', '', '', url, '', '', business_id)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    """ Close the connection """
    conn.close()
    
    blob = bucket.blob("ner-model.ser.gz")
    blob.download_to_filename("ner-model.ser.gz")
    
    subprocess.call(['/opt/java-jdk/jdk1.8.0_221/bin/java', '-jar', '/home/sanchitsh0211/AIWebscraper/crf.jar', "/home/sanchitsh0211/ner-model.ser.gz", "/home/sanchitsh0211/working_product_urls.txt"])
    
    files = glob.glob('./extracted_data/*')
    for f in files:
        os.remove(f)
    
    files = glob.glob('./tagged_data/*')
    for f in files:
        os.remove(f)
    
    os.remove('allurls.txt')
    os.remove('producturl.txt')
    os.remove('working_product_urls.txt')
    print("flow complete.")