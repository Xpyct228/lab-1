from marshmallow import validate, Schema, fields,post_load

from ormm import Order,Med,User,Upd


class User_valid(Schema):
    id = fields.Integer()
    username = fields.String(required =True)
    firstName = fields.String()
    lastName = fields.String()
    password = fields.String()
    phone = fields.Integer()
    userRole = fields.String()

    @post_load
    def get_user(self,data,**kwargs):
        return User(**data)

class Med_valid(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Int()
    number = fields.Integer()
    photoUrl=fields.String()
    description=fields.String()
    demannd=fields.String()

    @post_load
    def get_med(self,data,**kwargs):
        return Med(**data)

class Order_valid(Schema):
    id = fields.Integer()
    userId = fields.Integer()
    medId = fields.Integer()
    quantity = fields.Integer()
    status =fields.String()

    @post_load
    def get_order(self,data,**kwargs):
        return Order(**data)
class UPD_valid(Schema):
    id = fields.Integer()
    id_medicine=fields.Integer()
    new_price = fields.Int()
    new_number = fields.Integer()

    @post_load
    def get_upd(self, data, **kwargs):
        return Order(**data)