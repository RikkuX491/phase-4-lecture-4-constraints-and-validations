#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hotel, Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Hotels(Resource):

    def get(self):
        hotels = Hotel.query.all()

        response_body = []

        for hotel in hotels:
            hotel_dictionary = {
                "id": hotel.id,
                "name": hotel.name
            }
            response_body.append(hotel_dictionary)

        return make_response(jsonify(response_body), 200)

    def post(self):
        new_hotel = Hotel(name=request.get_json().get('name'))
        db.session.add(new_hotel)
        db.session.commit()

        response_body = {
            "id": new_hotel.id,
            "name": new_hotel.name
        }
        
        return make_response(jsonify(response_body), 201)

api.add_resource(Hotels, '/hotels')

class HotelById(Resource):

    def get(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()

        if not hotel:
            response_body = {
                "error": "Hotel not found"
            }
            status = 404

        else:
            response_body = {
                "id": hotel.id,
                "name": hotel.name
            }
            status = 200

        return make_response(jsonify(response_body), status)
    
    def patch(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()

        if not hotel:
            response_body = {
                "error": "Hotel not found"
            }
            status = 404

        else:
            json_data = request.get_json()
            for key in json_data:
                setattr(hotel, key, json_data.get(key))
            db.session.commit()

            response_body = {
                "id": hotel.id,
                "name": hotel.name
            }
            status = 200

        return make_response(jsonify(response_body), status)
    
    def delete(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()

        if not hotel:
            response_body = {
                "error": "Hotel not found"
            }
            status = 404

        else:
            db.session.delete(hotel)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)


api.add_resource(HotelById, '/hotels/<int:id>')

class Customers(Resource):

    def get(self):
        customers = Customer.query.all()

        response_body = []
        for customer in customers:
            response_body.append(customer.to_dict())
        
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        new_customer = Customer(first_name=request.get_json().get('first_name'), last_name=request.get_json().get('last_name'))

        db.session.add(new_customer)
        db.session.commit()
        
        return make_response(jsonify(new_customer.to_dict()), 201)

api.add_resource(Customers, '/customers')

class CustomerById(Resource):

    def get(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if not customer:
            response_body = {
                "error": "Customer not found"
            }
            status = 404
        else:
            response_body = customer.to_dict()
            status = 200

        return make_response(jsonify(response_body))
    
    def patch(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if not customer:
            response_body = {
                "error": "Customer not found"
            }
            status = 404
        else:
            json_data = request.get_json()
            
            for key in json_data:
                setattr(customer, key, json_data.get(key))

            db.session.commit()

            response_body = customer.to_dict()
            status = 200

        return make_response(jsonify(response_body), status)
    
    def delete(self, id):
        customer = Customer.query.filter(Customer.id == id).first()
        
        if not customer:

            response_body = {
                "error": "Customer not found"
            }
            status = 404
        
        else:
            
            db.session.delete(customer)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)

api.add_resource(CustomerById, '/customers/<int:id>')

if __name__ == '__main__':
    app.run(port=7000, debug=True)