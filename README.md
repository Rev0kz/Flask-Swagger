# Flask-Connexion

This project shows how to use Connexion, an OpenAPI framework built on flask to generate write OpenAPI specification and 
generate swagger documentation.  

In this project, we built a library datastore using sqlite3, created an api for it and generated a swagger documentation using 
Connexion.

You can try it out to learn and understand more about Connexion frameowrk.

## Getting Started 

You need the following to run this project

- [Connexion](https://connexion.readthedocs.io/en/latest/) :  to write OPenAPI specification and generate swagger documentation
- [Curl](https://curl.haxx.se/):  to request and retrieve data from hard disk
- [sqlite3](https://www.sqlite.org/index.html): to create a datastore for our library

You can install them via the following command:  

`pip install connexion[ui-swagger]`
`pip install json`
`pip install flask`

## How to Create Database and Tables Using Sqlite3    

Inside your virtual envrionment, type the following to create a database and initiate sqlite3 prompt afterwards

`sqlite3 library.db`               

The command below show available or current databases..

`sqlite>  .database` 

Create a table for authors using the following syntax

```
CREATE TABLE authors ( 
author varchar2(30) NOT NULL,
country varchar2(30) NOT NULL,
city  varchar2(30) NOT NULL,
newbook varchar2(30),
id integer primary key autoincrement);
```

Create a table for `apiinfo` using the following syntax  

```
CREATE TABLE  apiinfo (
buildtime date, 
version varchar2(30),
methods varchar2(30));
```

