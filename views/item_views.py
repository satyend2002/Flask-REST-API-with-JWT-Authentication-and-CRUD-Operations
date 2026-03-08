
from flask_restful import Resource,reqparse
# instead of request --> it reduced the validation code -- like after get_json - again we are sending (silent =true) -- if user not sending data -return none, we rae not validating data also there like integer , floate etc
#but  In flask_restful we have ---> reqparse -- this is for validation, fetching, conversions everything it will do ...
from app_one.controllers.items_controller import ItemController
from flask_jwt_extended import jwt_required

class ItemsResource(Resource): # class mapped to the endpoint
    @jwt_required()
    def post(self):
        req_p = reqparse.RequestParser()  # obj
        req_p.add_argument(name='name', type = str, required = True, help = 'enter your name') # required = true -- means its mandatory - means it should be sent by user
        req_p.add_argument(name='quantity', type = int, required = True, help = 'enter item quantity/valid item quantity') # here-> help='enter item quantity' this is only for custom message if user not provide qty
        data = req_p.parse_args()
        print(data)
        # we got the data now send to the controller ....
        res = ItemController.insert_item_controller(data)
        return res

    def get(self):
        res = ItemController.get_all()  # here we don't require anything from the user so we can call directly...
        return {"Items": res}


 # here we are creating another class becoz we can't define all methods in a single class we need parameter for deletig , updating , fetching at all ...
class ItemListResource(Resource):
    def get(self,id):  # get_one
        res = ItemController.get_one(id)
        if res:
            return {"id": res.id, "name": res.name, "quantity": res.quantity}
        return {"msg": f"for the given id {id}, no item found"},404

    @jwt_required()
    def put(self,id):
        req_p = reqparse.RequestParser()  # obj
        req_p.add_argument(name='name', type=str, required=True, help='enter your name')
        req_p.add_argument(name='quantity', type=int, required=True,
                           help='enter item quantity/valid item quantity')  # here-> help='enter item quantity' this is only for custom message if user not provide qty
        data = req_p.parse_args()  # this data is a dictionary , so how we can add id in it ...
        # data['id'] = id # in real time this is how we can add data , not update(), so if key not present it will be added at the end otherwise it will update the value
        dc = {"id": id, **data}  # this is how to add data (id here) in front of dictionary ....
        res = ItemController.update_one(dc)
        if res:
            return res
        return {"msg": f"for the given id {id}, no item found"}, 404

    @jwt_required()
    def delete(self,id):
        res = ItemController.delete_one(id)
        if res:
            return res
        return {"msg": f"for the given id {id}, no item found"},404

# now we have created restful api successfully ,now we will create Authentication .......
# means only register user can access this endpoint, becoz here anyone can access this endpoint ...
# when user logged in we will generate one token that token we need to send along with the request ....
# Authentication:- post, update(put), delete means only registered user can insert,update, delete the data, so we need to provide Authorization means we need to use jwt token....
# Again Process is same:- user needs to register with us ,if user wants to register we need to store user data in database, to store in db we need to define table after we need to create table,configurations already done, loading config already done,
# creating db obj done - so only we need to define the table, create the table, means when start the server it will automatically create the table-register, after that inserting in that one after login , means if user are giving right credentials ,
# we need to generate token after that we need to provide decorator jwt required, then it is going to look for token if token ,means valid token is present , it is going to trigger that function otherwise not going to trigger that fn  ...


"""
post
put 
delete
Note:-- means only login candidates can do/modify the data -- user going to do these endpoints-- protected route .....
"""
## For this user needs to register with us then login --- then we are going to generate access token and refresh token ...
## Access token for shorter period of time, refresh token for longer period of time  ....
## For using refresh token we are going to generates new access token ....

"""
post
put 
delete"""
### so for this means protected route we need tokens...
## Tokens --- jwt access_token
## To generate this access token - connection to the services - for connection - configurations is required ...
"""
Tokens --- jwt access_token -- to implement this jwt access_token  -- install flask extension --- pip install Flask-JWT-Extended
/login - username password
for login user needs to register with us ---
/registration - username password ....
/store the credential - to store it we required table ...
"""

## if access token is expired then for using refresh token we are going to generate new access token ...
## when user logged in at that time we are going to use both access and refresh token ....

"""
ItemsModel-
id
item_name
quantity
"""

## Cashing the data--- fetching the data
## now we are going to create one more app
## app_two :- from app_two we are going to call --
"""
call GET - item<id> ---> in this- data is going to contains -- id , item_name and quantity
## here for cashing /fetching the data along with id user needs to pass item_price and id

call GET - item<id> 
pip install requests --- by using this module from app_two ,we are going to call an Api which is present in the app_one ....
post -- id and item_price
id-
here we are going to create one more table -->  item_price
item_id -- itemModel-id (in item_price table)
item_name -- itemModel-item_name
quantity -- itemModel-quantity
item_price
"""

"""call GET - item<id> ---> here we need to call this API (from app_two we are calling an api which is present in app_one) ---> 
means one application needs to communicate with other application --> for this in flask we are using request module (only one way -- third-party module , where u call an api)...."""

"""Note:- In real time also we need to remember if we are creating another app there is only one way to call apis, present in diff app - using requests module

## so can 2 application run on the same port on local - no because ip address are going to be the same -- local host ..... 
so for that i need to give diff port number """

