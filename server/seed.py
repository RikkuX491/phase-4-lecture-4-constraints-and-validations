#!/usr/bin/env python3

from app import app
from models import db, Hotel

with app.app_context():
    
    Hotel.query.delete()

    hotels = []
    hotels.append(Hotel(name="Marriott"))
    hotels.append(Hotel(name="Holiday Inn"))
    hotels.append(Hotel(name="Hampton Inn"))

    db.session.add_all(hotels)
    db.session.commit()
    print("🌱 Hotels successfully seeded! 🌱")
