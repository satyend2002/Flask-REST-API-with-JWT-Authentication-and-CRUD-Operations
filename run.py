from app_one import app
from app_one import db


if __name__ == '__main__':
    with app.app_context():
        db.create_all() #prevoiusly we used function to define table that's why, we import model but here we have created one class ,
        # that is inherited from db.Model for table, so when creat_all() will execute it will  automatically call that class which is inheriting from db.Model
        # and then automatically it is going to create the table .....
    app.run(debug=True)

