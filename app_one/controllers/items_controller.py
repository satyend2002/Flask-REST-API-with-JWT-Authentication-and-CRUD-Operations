from app_one import db
from models.item_models import Item
class ItemController:
    @staticmethod
    def insert_item_controller(data):
        obj = Item(name = data['name'], quantity = data['quantity'])
        db.session.add(obj)
        db.session.commit()
        return  {"id": obj.id, "name": obj.name, "quantity": obj.quantity}


    @staticmethod
    def get_all():
        obj = Item.query.all() # it will return list of objects ....
        res = [{"id": each.id, "name": each.name, "quantity": each.quantity} for each in obj]
        print("GET ALL TYPE:", type(res), res)
        return {"Items": res}


    @staticmethod
    def get_one(id):
        obj = Item.query.get(id)
        return obj

    @staticmethod
    def update_one(data):
        #here first we need id if data present means update it, otherwise return not present
        res = ItemController.get_one(data['id'])
        if res:
            res.name = data['name']
            res.quantity = data['quantity']
            db.session.add(res)
            db.session.commit()
            return {"id": res.id, "name": res.name, "quantity": res.quantity}
        return res

    @staticmethod
    def delete_one(id):
        res = ItemController.get_one(id)
        if res:
            db.session.delete(res)
            db.session.commit()
            return {"msg": f"Item with item id {id} deleted successfully"}
        print("DELETE TYPE:", type(res), res)
        return res

