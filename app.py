from flask import Flask



@app.route('/api/v2/info', methods=["GET"])
def get_info():
  conn = sqlite3.connect('library.db')
  print("connected to library the database")
  api_release = []
  cursor = conn.execute("SELECT buildtime, version, methods from apiinfo")
  for row in cursor:
    api_info = {}
    api_info['buildtime'] = row[0]
    api_info['version'] = row[1]
    api_info['methods'] = row[2]
  conn.close()
  return jsonify({'api_release': api_info}), 200




@app.route('/api/v2/authors' methods=['GET'])
def list_authors():
  return show_authors() 


def show_authors()
conn = sqlite3.connect('library.db')
print ("database connected successfully")
authors_list=[]
cursor = conn.execute("SELECT name, country, email, books, from Author")
for row in cursor:
data_dict = {}
data_dict["name"] = row[0]
data_dict["country"] = row[1]
data_dict["email"] = row[2]
data_dict["book"] = row[3]
authors_list.append(data_dict)
conn.close()
  return jsonify({'show_authors': authors_list})



@app.route('/api/v2/author<author_name>', method=['GET'])
def get_author(author_name):
  return author_info(author_name)


def author_info(author_name):
conn = sqlite3.connect("library.db")
author_data = []
cursor = conn.execute(SELECT * from Author where name=?", (author_name,))
data = cursor.fetchall()
if len(data) == 0:
    abort(404) 
else: 
  author = {}
  author['name'] = data[0][0]
  author['country'] = data[0][1]
  author['email'] = data[0][2]
  author['book'] = data[0][3]
      conn.close()
      return jsonify({a_dict})
                      
                      


      author['email'] = data[0][2]
      author['book'] = data[0][3]
          conn.close()
          return jsonify({a_dict})


@app.errorhandler(404)
def author_not_found(error):
      return make_response(jsonify({'error': 'author not available!'}), 404) 
                      
 
@app.route('/api/v2/author', methods=['POST'])
def newauthors():
   if not request.json or 'name' not in request.json:
      abort(400)
   user = { 
        'name' = request.json['name'],
        'country' = request. json['country'],
        'email' = request.json['email'],
        'book' = request.json['book']
        }
    return jsonify({    })
                      
                      

def include_author():
     conn = connect.sqlite3("library.db")
     print("database connected")
     author_data = []
     cursor = conn.cursor()
     cursor.execute(SELECT * from Author where name=?,  (new_author['name'])) 
     data = cursor.fetchall()
        if len(data) != 0: 
                abort(400)
        else:
          cursor.execute("insert into library (author, country, book) values(?,?,?)", (new_author['name'], new_author['country'], new_author['email'], new_author['books']))
          conn.commit()
          return "created"
       conn.close()
       return jsonify(a_dict)
                      
                      
 
@app.route('/api/v2/authors', methods=['DELETE'])
def del():  
    if not request.json or 'name' not in request.json: 
          abort(400)
    author = request.json['name']
    return jsonify({'status': delete_user(author)}), 200 

def delete_user(delete_user): 
    conn = connect.sqlite3("library.db")
    print("database connected successfully");
    cursor = conn.cursor()
    cursor.execute("SELECT * from Author where name=? ", (delete_user,)) 
    details = cursor.fetchall()
    print("Details", details)
    if len(details) == 0:  
        abort(400);
    else:
      cursor.execute("delete from Author where name=?", (delete_user,))
      conn.commit()
      return "author successfully deleted"                 
                      
                      
