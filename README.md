# Flask-Swagger

This project shows how to use Swagger, an OpenAPI framework built on flask to generate write OpenAPI specification and 
generate swagger documentation.  

In this project, we built a library datastore using sqlite3, created an api for it and generated a swagger documentation using the swagger editor.

![image](recent:///0f3b0e48001f30282feb5c645c8d8874)

## Getting Started 

You need the following to run this project

- [docker engine](https://www.docker.com/) : to run a container of swagger-editor image
- [Curl](https://curl.haxx.se/):  to request and retrieve data from hard disk
- [sqlite3](https://www.sqlite.org/index.html): to create a datastore for our library   


##   Install Docker on Debian 

Install packages which allows `apt` to use packages over https.      

`apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common`      

Then add GPG Key for docker repo to your system  

`curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -`   

Add Docker repo to apt source 

`add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable`

Finally execute the following commands to install docker community edition     

`apt-cache policy docker-ce`

` apt install docker-ce`

`

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
The apiinfo table will contain information such as version type, build date about the library application programming interface.

You can use the following command to insert values into the `apiinfo` table

```
Insert into apiinfo values ( '2019-02-08 12:00:00', "v1",  "get");
```
