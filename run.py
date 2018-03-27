from app import app
from db import db

db.init_app(app)

# Before the first user request runs, This decorator will run the create_tables() method and
# we will create a data.db with all the tables, unless they exist they exist already.
@app.before_first_request
def create_tables():
    db.create_all()
