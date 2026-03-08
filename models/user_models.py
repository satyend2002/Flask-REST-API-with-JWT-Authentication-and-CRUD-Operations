from werkzeug.security import generate_password_hash, check_password_hash
from app_one import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    """class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(405), nullable=False, unique=True)
    password = db.Column(db.String(455), nullable=False)

    def generate_pass_hash(self, raw_password):
        self.password = generate_password_hash(raw_password) # password hashed ....

    def check_pass_hash(self, raw_password):
        return check_password_hash(self.password, raw_password) # self.password -- hashed password"""