from app_one import db
class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False, unique = True)
    quantity = db.Column(db.Integer, nullable = False)
