""" Import the necessary modules """
import pyodbc

def storeProdURL(name):
	id = 0

	business_id = 0

	""" Specify the inputted business name """
	business_name = name

	""" Establish connection to microsoft sql server """
	conn = conn = pyodbc.connect('Driver={SQL Server};'
						  'Server=DESKTOP-1P8QTPD;'
						  'Database=CRFTest;'
						  'UID=Sanchit12;'
						  'PWD=GSWarrior02;'
						  'Trusted_Connection=yes;')

	cur = conn.cursor()

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
	cur.execute("SELECT business_id from BUSINESSES WHERE CONVERT(varchar, business_name) = ?", business_name)
	business_id = cur.fetchone()[0]

	""" Loop through all working product urls and store them in the database """
	for url in urls:
		id = id + 1
		postgres_insert_query = """SET ANSI_WARNINGS OFF; INSERT INTO ENTITIES (entity_id, brand, model, price, stock, producturl, condition, business_id, category) \
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?); SET ANSI_WARNINGS ON; """
		record_to_insert = (str(id), '', '', '', '', url, '', business_id, '')
		cur.execute(postgres_insert_query, record_to_insert)
		conn.commit()

	""" Close the connection """
	conn.close()
