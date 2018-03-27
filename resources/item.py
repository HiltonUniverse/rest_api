#NOTE: Resource normally uses the MODEL classes to extract data from the db. But the MODEL classes stands on it's own.
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item_model import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required  = True,
    help = "This field cannot be left blank"
    )

    parser.add_argument('store_id',
    type = int,
    required  = True,
    help = "Every items needs a store id."
    )
    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': "An error occurred when retriving data from the database!"}, 500

        if item:
            return item.json() #ecause item is an object, we can't return it directly.
        return {'message': "Item not found"}

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)} , 400

        data = Item.parser.parse_args()

        new_item = ItemModel(name,**data) #data['price'],data['store_id']

        try:
            new_item.save_to_db() #inserts itself into the db
        except:
            return {'message':"An error occurred when inserting"}, 500 #internal server error
        return new_item.json(), 201 # 201 is for created

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'Item has been deleted!'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data) #data['price'],data['store_id'] is same as **data
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()


#Return list of items
class ItemList(Resource):
    def get(self):
        # ItemModel.query.all() gives all the elements in the item table.
        # Then we iterate over it and convert them to json
        # then we have a list of jason. We convert it to dictionary and return it.
        return {'items': [item.json() for item in ItemModel.query.all()]}

        #with lambda: list(map(lambda x: x.json(),ItemModel.query.all()))
