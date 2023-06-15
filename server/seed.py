#!/usr/bin/env python3

from app import app
from models import db, Hotel, Customer

with app.app_context():
    
    Hotel.query.delete()
    Customer.query.delete()

    hotels = []
    hotels.append(Hotel(name="Marriott"))
    hotels.append(Hotel(name="Holiday Inn"))
    hotels.append(Hotel(name="Hampton Inn"))

    customers = []
    customers.append(Customer(first_name="Alice", last_name="Baker"))
    customers.append(Customer(first_name="Barry", last_name="Smith"))
    customers.append(Customer(first_name="Chris", last_name="Jones"))

    db.session.add_all(hotels)
    db.session.add_all(customers)
    db.session.commit()
    print("🌱 Hotels and Customers successfully seeded! 🌱")
