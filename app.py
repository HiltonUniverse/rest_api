from flask import Flask
from flask_restful import Api

from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store,StoreList

app = Flask(__name__)
#notifying the sql_alchemy where it can find the data.db. sqlite:///data.db means look at the current directory.
#NOTE: it doesn't have to be "sqlite", it can be "mysql, pastro sql, oracle, it can be anything" and it will still work.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#In order to know when an object has been changed but not saved to the database. The "flask"_sqlalchemy has a tracker that
# tracks every change that we made to the sql_alchemy session and that takes resources. so we turn off  the "flask"_sqlalchemy
# tracker. The main library of the "SqlAlchemy" itself has a tracker that is better than the tracker.
#So this turns off the flask_sqlalchemy tracker but not the SQLAlchemy's tracker.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hilton'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth, path is generated automatically

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register') #calls the post method of the class UserRegister
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

#the file that runs has the name __main__, so if we run user.py, user.py has the name __main__
# So if the __name__ is main, then we want to run this app! If not then we are sure that we are importing app.py form somewhere.
if __name__ == '__main__': #prevents running when importing app.py
#we import it here because of circular imports, Item models and others will also import db. So if we import db at the top and also
# the models at the top, will import it and we have circular dependencies.
    from db import db #Import sql_alchemy object
    db.init_app(app)#pass in our flask app.
    app.run(port = 5000, debug = True)
