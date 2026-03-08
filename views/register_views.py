from flask_restful import Resource, reqparse
from models.user_models import User
from app_one import db

class RegisterResource(Resource):
    def post(self):
        req_p = reqparse.RequestParser()  # obj
        req_p.add_argument(name='username', type=str, required=True)
        req_p.add_argument(name='password', type=str, required=True, )
        data = req_p.parse_args()
        # here first we need to check if user already registered with us ...
        obj = User.query.filter_by(username=data['username']).first()
        if obj:
            return {'message': f'Username with username {data['username']} already exists'}, 400
        db_obj = User(username=data['username'])
        db_obj.set_password(data['password'])
        db.session.add(db_obj)
        db.session.commit()
        return {'message': f'User with username {data['username']} registered successfully!'}, 201

    # now registration is done - now login ...