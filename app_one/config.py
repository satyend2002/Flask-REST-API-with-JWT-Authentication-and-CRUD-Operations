from datetime import timedelta
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost/project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=80) # after every 40 seconds access token will expire ...
    JWT_SECRET_KEY = "jwt secret key"

