from flask_restful import Resource, reqparse
from models.user_model import UserModel
#creating a endpoint to register a user
class UserRegister(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('username',
        type = str,
        required = True,
        help = "This field cannot be blank"
    )

    parse.add_argument('password',
        type = str,
        required = True,
        help = "This field cannot be blank"
    )

    def post(self):
        data = UserRegister.parse.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "A User with that name already exists!"}, 400

        user = UserModel(**data) #similary to: data['username'], data['password']
        user.save_to_db()

        return {'message':"User created successfully"}, 201
