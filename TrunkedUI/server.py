from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField
from wtforms import validators, StringField, SubmitField
import json
import pytds
from urllib.parse import urlparse
import id

DEBUG = True
app = Flask(__name__, static_folder='assets')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'letsAgreeToDisagree'


@app.route("/", methods=['GET', 'POST'])
def trance():
    if request.method == 'POST':
        if request.data:
            uiobjs = ""
            uiobjs = (json.loads(request.data.decode("utf-8")))
            print(uiobjs)
            for uiobj in uiobjs:
                if(uiobj["bname"] and uiobj["burl"] and uiobj["btitle"]):
                    try:
                        parsed_uri = urlparse(uiobj["burl"])
                        bdomain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                        id.flowStart(uiobj["bname"], uiobj["burl"], uiobj["btitle"], bdomain)
                        conn = pytds.connect('devdb.trunked.com.au', 'trunkedproject', 'trunkedproject', 'rmitProject@trunked')
                        cur = conn.cursor()
                        postgres_insert_query = """SET ANSI_WARNINGS OFF; INSERT INTO BUSINESSES (business_name, business_url) \
                        VALUES (?, ?); SET ANSI_WARNINGS ON; """
                        record_to_insert = (uiobj["bname"], uiobj["burl"])
                        cur.execute(postgres_insert_query, record_to_insert)
                        conn.commit()
                        conn.close()
                        return jsonify({'myModaladd': "myModaladd", 'modalMesage': "Extraction Job Completed"})
                    except:
                        print("except")
                        return jsonify({'myModaladd': "myModaladd", 'modalMesage': "Inernal Error"})
                else:
                    print("else")
                    return jsonify({'myModaladd': "myModaladd", 'modalMesage': "Incorrect data provided"})
    else:
        print("outer else")
        return render_template('index.html')


@app.route("/keyword", methods=['POST'])
def keySearch():
    if request.method == 'POST':
        if request.data:
            uiobjs = ""
            uiobjs = (json.loads(request.data.decode("utf-8")))
            if(uiobjs["keyword"]):
                # try:
                print(uiobjs["keyword"])
                rowList = []
                conn = pytds.connect('devdb.trunked.com.au', 'trunkedproject', 'trunkedproject', 'rmitProject@trunked')
                cur = conn.cursor()
                print("1")
                selectQ = "select * from ENTITIES where brand like %s or model like %s or producturl like %s ;"
                postgres_insert_query = "SET ANSI_WARNINGS OFF; " + selectQ + " SET ANSI_WARNINGS ON; "
                print("2")
                record_to_insert = ("%"+uiobjs["keyword"]+"%", "%"+uiobjs["keyword"]+"%", "%"+uiobjs["keyword"]+"%")
                cur.execute(postgres_insert_query, record_to_insert)
                print("3")
                for row in cur:
                    print(row)
                    rowList.append(row)
                conn.commit()
                conn.close()
                print("4")
                if len(rowList) > 0:
                    return jsonify({'result': rowList})
                else:
                    return jsonify({'myModaladd': "myModaladd", 'modalMesage': "No relevant product"})
                # except:
                    # print("except")
                    # return jsonify({'myModaladd': "myModaladd", 'modalMesage': "Inernal Error"})
            else:
                print("else")
                return jsonify({'myModaladd': "myModaladd", 'modalMesage': "Incorrect data provided"})
    else:
        print("outer else")
        return render_template('index.html')


# @app.route("/viz", methods=['GET'])
# def showViz():
#     if request.method == 'GET':
#         try:
#             rowList = []
#             conn = pytds.connect('devdb.trunked.com.au', 'trunkedproject', 'trunkedproject', 'rmitProject@trunked')
#             cur = conn.cursor()

#             selectQ = "SELECT DISTINCT category,  COUNT(  category ) AS Count FROM entities GROUP BY category"
#             postgres_insert_query = "SET ANSI_WARNINGS OFF; " + selectQ + " SET ANSI_WARNINGS ON; "

#             cur.execute(postgres_insert_query)

#             for row in cur:
#                 rowList.append(row)
#             conn.commit()
#             conn.close()

#             rowList2 = []
#             conn = pytds.connect('devdb.trunked.com.au', 'trunkedproject', 'trunkedproject', 'rmitProject@trunked')
#             cur = conn.cursor()
# # """

# # select CAST(count(brand) AS float)/CAST((select count(*) from ENTITIES) AS float)*100 as brand from ENTITIES where len(brand) >1 ;
# # select CAST(count(model) AS float)/CAST((select count(*) from ENTITIES) AS float)*100 as model from ENTITIES where len(model) >1 ;
# # select CAST(count(price) AS float)/CAST((select count(*) from ENTITIES) AS float)*100 as price from ENTITIES where len(price) >1 ;
# # select CAST(count(stock) AS float)/CAST((select count(*) from ENTITIES) AS float)*100 as stock from ENTITIES where len(stock) >1 ;
# # select CAST(count(condition) AS float)/CAST((select count(*) from ENTITIES) AS float)*100 as condition from ENTITIES where len(condition) >1 ;
# # select CAST(count(category) AS float)/CAST((select count(*) from ENTITIES) AS float)*100 as category from ENTITIES where len(category) >1 ;

# # """

#             selectQ = "select count(brand)/count(*), count(model)/count(*), count(price)/count(*), count(stock)/count(*), count(producturl)/count(*), count(condition)/count(*), count(category)/count(*) from ENTITIES;"
#             postgres_insert_query = "SET ANSI_WARNINGS OFF; " + selectQ + " SET ANSI_WARNINGS ON; "

#             cur.execute(postgres_insert_query)

#             for row in cur:
#                 rowList2.append(row)
#             conn.commit()
#             conn.close()
#             return jsonify({'category': rowList, 'entity': rowList2})
#         except:
#             print("except")
#             return jsonify({'myModaladd': "myModaladd", 'modalMesage': "Inernal Error"})
#     else:
#         print("outer else")
#         return "error"


if __name__ == "__main__":
    app.run()
