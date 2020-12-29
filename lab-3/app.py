from flask import Flask,request
from werkzeug.security import generate_password_hash,check_password_hash
from wsgiref.simple_server import make_server
from ormm import Order,Med,User,Upd,engine
from sqlalchemy.orm import Session
from datetime import datetime
from validation import User_valid,Med_valid,Order_valid
import hashlib
import json
from collections import namedtuple
from json import JSONEncoder
from marshmallow import Schema, fields, INCLUDE, ValidationError
from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask import make_response
from werkzeug.security import generate_password_hash
import os
from flask import Flask, render_template, flash, redirect, url_for, request, abort, jsonify
from flask import make_response

import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app = Flask(__name__)
bcrypt = Bcrypt(app)

session = Session(engine)
auth = HTTPBasicAuth(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/hello-world-19')
def start():
    return 'Hello, World 15!'
@auth.verify_password
def verify_password(username, password):

    user = session.query(User).filter_by(username = username).first()
    if user==None:
        return False
        print("loxxxx")
    print("verify")
    return check_password_hash(user.password,password=password)

@app.route('/medicine',methods=['POST'])
@auth.login_required
def add_madicine():
    user = session.query(User).filter_by(username=auth.current_user()).first()
    print(user.username)
    if user.userRole != "pokypets":

        try:
            d = request.get_json()
            med = Med_valid().load(d)
            session.add(med)
            session.commit()
            return 'medicine aded succesfully',201
        except ValidationError as err:
            print(err)
            return "invalid input "+str(err),404
    else:
        return "acces denied you are not provisor"


@app.route('/medicine/<id>',methods=['GET'])
@auth.login_required
def get_medicine(id):
    user = session.query(User).filter_by(username=auth.current_user()).first()
    print(user.username)
    if user.userRole != "provizor":
        return make_response('Access denied', 403)
    else:
        x = session.query(Med).filter_by(id=id).first()
        return (json.dumps(x.as_dict()),200) if x != None else ("not found medicine with current id",404)

@app.route('/medicine/<demannd>',methods=['GET'])
def get_medicine_demand(demannd):
    result = session.query(Med).filter_by(demannd=demannd).first()
    return (json.dumps(result.as_dict()),200) if result != None else ("not found",404)

@auth.login_required
@app.route('/medicine/<id>',methods=['PUT'])

def put_medicine(id):
    obj = session.query(Med).filter_by(id=id).first()
    if obj==None:
        return "not found",404
    d = request.get_json()
    try:
        med = Med_valid().load(d)
        obj.new_price,obj.new_number = 10,25
        session.add()
        session.commit()
        return 'Medicine has been updated',201
    except ValidationError as err:
        return 'invalid input 404',404
@auth.login_required
@app.route('/medicine/<id>',methods=['DELETE'])
def delete_medicine(id):
    user = session.query(User).filter_by(username=auth.current_user()).first()
    print(user.username)
    if user.userRole != "provizor":
        return make_response('Access denied', 403)
    else:

        l= session.query(Med).filter_by(id=id)
        if  l.first()==None:
            return "not found medicine with curent id",404
        session.query(Med).filter_by(id=id).delete()
        session.commit()
        return 'deleted medicine '+id



@app.route('/store/order',methods=['POST'])
@auth.login_required
def add_order():
    user = session.query(User).filter_by(username=auth.current_user()).first()
    print(user.username)
    if user.userRole != "pokypets":
        return make_response('Access denied', 403)
    else:

     try:

        d = request.get_json()
        order= Order_valid().load(d)
        session.add(order)
        session.commit()
        return 'order created succesfully',201
        return usert.id
     except ValidationError as err:
        print(err)
        return "invalid input "+str(err),404

@app.route('/medicine/order/<id>',methods=['GET'])
def get_order(id):
    f = session.query(Order).filter_by(id=id).first()
    if f != None:
        return (json.dumps(f.as_dict()),200)
    else: ("not found",404)
@app.route('/medicine/order/<id>',methods=['DELETE'])
@auth.login_required
def delete_order(id):
    user = session.query(User).filter_by(username=auth.current_user()).first()
    print(user.username)
    if user.userRole != "pokypets":
        return make_response('Access denied', 403)
    else:

        x = session.query(Order).filter_by(id=id).first()
        if x==None:
            return "not found",404
        session.query(Order).filter_by(id=id).delete()
        session.commit()
        return 'deleted medicine order '+id

@app.route('/user/create',methods=['POST'])
def create_user():
    try:
        d = request.get_json()
        create= User_valid().load(d)
        create.password = generate_password_hash(request.json['password'])
        session.add(create)
        session.commit()
        return 'account created succesfully'
    except ValidationError as err:
        print(err)
        return "invalid input " + str(err), 405
    session.add(create)
    session.commit()

@app.route('/user/logout/', methods=['GET'])
@auth.login_required
def logout():
    return "You have been logged out."



@app.route('/user/<id>',methods=['GET'])

def get_user(id):
    result = session.query(User).filter_by(id=id).first()
    if result != None:
        return (json.dumps(result.as_dict()),200)
    else: ("not found",404)

@app.route('/user/<id>',methods=['PUT'])
def put_user(id):
    obj = session.query(User).filter_by(id=id).first()
    if obj==None:
        return "not found",404
    d = request.get_json()

    obj.username,obj.firstName,obj.lastName = "lox","mox","llo"
    session.commit()
    return 'The user has been updated',201

@app.route('/user/<id>',methods=['DELETE'])
@auth.login_required
def delete_user(id):
    result = session.query(User).filter_by(id=id).first()
    if result==None:
        return "not found",404
    session.query(User).filter_by(id=id).delete()
    session.commit()
    return 'deleted user '+id,200



with make_server('', 5000, app) as server:
    print("That is working!!!")

    server.serve_forever()
