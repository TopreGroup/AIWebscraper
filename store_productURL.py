""" Import the necessary modules """
import pytds
from google.cloud import storage

def storeProdURL(name):
    id = 0

    business_id = 0

    """ Specify the inputted business name """
    business_name = name

    client = storage.Client()
    
    bucket_name = "trunkedfilestorage"
    
    bucket = client.get_bucket(bucket_name)

    """ Establish connection to microsoft sql server """
    conn = conn = pytds.connect('devdb.trunked.com.au', 'trunkedproject', 'trunkedproject', 'rmitProject@trunked')

    cur = conn.cursor()

    """ Reading lines from working product urls text file """  
    file_lines = []
    blob = bucket.get_blob('producturl.txt')
    out_file = open("producturl.txt", 'wb')
    file_content = blob.download_as_string()
    out_file.write(file_content)
    out_file.close()
    
    with open("producturl.txt", "r") as fs:
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
        id = id + 1
        postgres_insert_query = """SET ANSI_WARNINGS OFF; INSERT INTO ENTITIES (entity_id, brand, model, price, stock, producturl, condition, business_id, category) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s); SET ANSI_WARNINGS ON; """
        record_to_insert = (str(id), '', '', '', '', url, '', business_id, '')
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    """ Close the connection """
    conn.close()
