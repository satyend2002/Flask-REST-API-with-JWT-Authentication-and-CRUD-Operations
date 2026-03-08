import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app_one.config import Config
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config) # load config ..

# connections ...
db = SQLAlchemy(app) # flask service to database/sql ...
api = Api(app)  # here we are making connection from flask_restful service to the flask service ....
jwt = JWTManager(app)

from views.item_views import ItemsResource, ItemListResource
from views.register_views import RegisterResource
from views.login_views import LoginResource

api.add_resource(ItemsResource, '/items')# endpoint --> here now this class is mapped with it ....
api.add_resource(ItemListResource, '/items/<id>') # so url is going to diff -- here we are creating diff class becoz we can't defines all methods in a single class we need parameters for deletig , updating , fetching at all
# this add_resource() fn will take care of routing mechanism , like we create @app.route ....
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')


