from flask_app.controllers import ninjas
from flask_app import app

if __name__=="__main__":
    app.run(debug=True, port = 5001) 
    

#Notes on Review Setup

#1. mkdir dojos_and_ninjas
#2. cd dojos_and_ninjas
#3. touch server.py && pipenv install flask pymysql flask-bcrypt, double check pipfile to verify installs.
#4. from dojos_and_ninjas directory mkdir flask_app
#5. cd flask_app && mkdir config controllers models static templates
#6. touch __init__.py
#7. add code to server and init files.
#8. mysqlconnection file import 

#----Notes----

# -- our initializer file or __init__ is where we bring in an instance of flask
# 1. from flask import Flask. 2. app = flask(__name__). 3. app.secret_key = "secret_word"

# -- our server.py file imports controllers and flask instance, being app. We also include our footer
# 1. from flask_app.controllers import ____. 2. from flask_app import app
# 3. footer - if the name of our app is equal to the main instance in our app, we'll run our app pn port 5001
# 4 if __name__=='__main__':
#       app.run(debug=True, port- 5001)

#-- mysqlconnection.py --
#1. INSERT queries will return the ID NUMBER of the row inserted
#2. SELECT queries will return the data from the database as a LIST OF DICTIONARIES
#3. UPDATE and DELETE queries will return nothing
#4. If the query fails the method will return FALSE


#-- MODELS --
#1. import connection to mysql file and other models if neccessary
#2. Define your DB as a class or global variable and build out class from MySQL

#--------Methods in Models ---

# -----Save-
### parameters = cls, data
#1. Save method we dont need to include created_at or updated_at because we took care of that in MySQL when building the ERD by right clicking on_update
#2. Save method is an insert query, returning the ID of the row inserted with...
#2b. return connectToMySQL(cls.DB).query_db(query, data)
#3. query_db is a function that takes in (self, query, and data=None, that's why we pass data so it can be overwritten)

# -----Get_All- W/O Join
### parameters = cls
#### requires a query, variable of DB, variable to capture each object from DB, for loop to loop each instance and append and a return statement returning our objects
#1. Select query, returning a list of dictionaries of objects
#2. Create Variable of DB
#3. Creat Variable to capture all objects from DB. 
#3. For loop over our objects, append each instance to our variable that houses them, by append(cls(instance)).
#4. Append with cls, for example) dojos.append(cls(dojo)) dojo being 'i' in this instance
#5. Return list of objects to loop on front end

#-------Get_One- w/o Join
### parameters = cls, data
#### what do we need to return? Only 1 row from the database
#1. requires our query
#2. requires returning that specific row from the database

#--------Update w/o join and Delete w/o join 
#### parameters = cls, data
# update and delete queries return nothing so we just return the DB
#1. Query = select on id

#----Get_one or Get_all w join
### parameters = cls, data
#1a. Create query
#1b. Create variable of DB
#2. print your variable for assurance
#3. create a variable for each row of the db
#3b. Ex) row = cls(results[0])
#4. Print your results[0] to ensure the data is coming back joined and in 1 row
#5. Loop over the DB, creating instances of each ninja
####Because we are in the dojo model, we are creating instances of each ninja, from SQL class setup, that has a reference to which djo_id its apart of
#6. Because we have an empty list in each instance created, we are just appending the ninja variable just created to the list
#7. Return each row to loop on front end


#-- Controllers-
#1. We must call on flask itself to bring in our render_template, redirect, request and session objects and variables
#2. import app from flask_app
#3. import models
#3b. Create variables of our methods to pass to the front end in our render template fucntions
#4. When we need access to id's in routes we must pass them in like so..
#5. @app.route('/edit_page/<int:ninja_id>') 
###Note - in the the display_ninja.html  we are rendering our info based off of each ninja object, that's why our route takes in <int:ninja_id>, because that's what it's called on the front end.
#6. If I see that syntax on the back end I know on the front end we use jinja.. like so..
#7. form action="/update/{{ninja_id}}"

#8. On update in controller,  returning a redirect to a route needing that ID as well looks like this..)
#8b. Requires f statement 
#9.return redirect (f"/show/{ninja.dojo_id}"), with single brackets
#10. On a post method we always redirect
