from db import db

# UserModel extends the db.Model, This will tell the sql alchemy object/entity that this usermodel is what we are going to be
# saving to the database and retrieving. Sql_alchemy creates a mapping between database and these object.
class UserModel(db.Model):
# After extending we have to tell the sql_alchemy the table name of where these models are going to be stored.
# From the query we can see it's (user) table
    __tablename__ = 'users'
# we also have to tell the sql alchemy what columns the table contains.
# so we have columns called id,username and password in the database. and The id has it's type is Integer and is a primary key
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username #we don't need id, as it's auto incrementing in our case
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod #doing this will make this method be callable like a static method. Class.method()
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
