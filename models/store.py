#copy of item_model and edited
from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    # Back reference, this helps store to know what items in the items table has store_id on it.
    # So it knows what items are linked to the store.
    #NOTE: when storeModel is created, it also creates object for each iteam that matches this relationship.
    #If we have fiew item it's okay, but for large number of items it can be expensive.
    # So we use " lazy='dynamic' ", to say to sql_alchemy to not go inside the item table and create items' objects.
    # Doing this will precent self.items to return a list of iteam, so we have to use self.items.all().
    # NOTE: The problem now is the speed, every time we call def json(self), we have to go into the table.
    # So if we want speed this approach is not good. If we don't use lazydynamic then we create a table of related objects once,
    # and access then as many times as we want.
    # So there is a trade off between speed of creation of the store and the speed of calling the json method.
    items = db.relationship('ItemModel',lazy = 'dynamic') #defines many-to-one Relationship

    def __init__(self,name):
        self.name = name

#returns a json representation of a model
    def json(self):
        return {'name':self.name,'items': [item.json() for item in self.items.all()]}

    @classmethod #class method because it returns object of this class.
    def find_by_name(cls,name):
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
