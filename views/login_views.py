from flask_restful import Resource, reqparse
from models.user_models import User
from flask_jwt_extended import create_access_token

class LoginResource(Resource):
    def post(self):
        req_p = reqparse.RequestParser()  # obj
        req_p.add_argument(name='username', type=str, required=True)
        req_p.add_argument(name='password', type=str, required=True, )
        data = req_p.parse_args()

        # here not only we are going to check username , we need to check either password is same or not -- check_password_hash...
        obj = User.query.filter_by(username=data['username']).first()
        if obj and obj.check_password(data['password']):
            # if both username and password are true then we need to generate access token-- pip install Flask-JWT-Extended ...
            return {"access token": create_access_token(identity=data['username'])}
        return {'message': 'provide valid credentials'}


