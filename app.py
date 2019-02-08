import connexion 
import json 
from flask import jsonify 
import sqlite3 

#route handler for apiversion
@app.route("/api/version/info", method=["GET", "POST"])
def api_info():
  conn = sqlite3.connect('lib.db')
  print("opened database successfully");
  api_info = []
  cursor = conn.execute("SELECT buildtime, version, links, methods from apiversion")
for row in cursor:
  a_dict = {}
  a_dict = ['version'] = row[0]
  a_dict = ['buildtime'] = row[1]
  a_dict = ['links'] = row[2]
  a_dict = ['methods'] = row[3]
  api_list.append(a_dict)
conn.close()
return jsonify({'api_info' : api_list})      


#route handler to retrieve a list of authors in the authors table"
@app.route("api/v1/authors", method=["GET"])
def list_author():
    return get_author
  
#logic to retrieve list of authors from the authors table
def get_author():
  conn = sqlite3.connect("library.db")
  authors = []
  cursor = conn.execute("SELECT name, country, email, books, id from authors")
  for row in cursor:
  author_data = {}
  a_dict['name'] = row[0]
  a_dict['country'] = row[1]
  a_dict['email'] = row[2]
  a_dict['book'] = row[3]
  a_dict['id'] = row[4]
  authors.append(author_data)
  conn.close()
      return jsonify({'list_of_authors': authors))
                      
                      
