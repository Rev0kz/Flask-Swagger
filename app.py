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
