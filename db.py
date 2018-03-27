from flask_sqlalchemy import SQLAlchemy

# This sql alchemy object is going to link to our flask app and it's going to look at all of the objects that we tell it to.
#  and then it's going to allow us to map those objects to rows in the database.
# Example: if we create an object of item_model that has fields/col: name and price, it's going to allow us to very easily put
# that object into our database. Putting object into the database basically means, we are saving the properties of the object in the database
#sql alchemy excells at this and makes it easy.
db = SQLAlchemy()
