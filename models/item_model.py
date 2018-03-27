from db import db

# ItemModel extends the db.Model, This will tell the sql alchemy object/entity that this itemmodel is what we are going to be
# saving to the database and retrieving. Sql_alchemy creates a mapping between database and these object
class ItemModel(db.Model):
# After extending we have to tell the sql_alchemy the table name of where these models are going to be stored.
# From the query we can see it's (items) table
    __tablename__ = 'items'
# we also have to tell the sql alchemy what columns the table contains.
# so we have columns called id,username and password in the database. and The id has it's type is Integer and is a primary key
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))

    #define [stores] tables id column as foreigh key for the [items] talbe
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    # this finds a store that matched the store_id
    store = db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

#returns a json representation of a model
    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod #class method because it returns object of this class.
    def find_by_name(cls,name):
        #ItemModel.query notifies the sql_alchemy that we are going to query on it.
        #NOTE: ItemModel is a db.Model
        #We don't have to connect,disconnect, iterate! everything is done by the sql_alchemy!
        # we do: SELECT * FROM items WHERE name=name LIMIT 1.
        # Then it is converted to object of ItemModel
        return cls.query.filter_by(name=name).first()

#self because it inserts itself, It saves a ItemModel to the database. SQLAlchemy can directly translate object to row directly
# in the database. So we don't have to tell it what row to insert in the db. As we are dealing with self object. We can directly
# insert it.
    def save_to_db(self): # does both insert and update
        db.session.add(self) # we can add multiple objects at once, but in this case we are only adding one object
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
