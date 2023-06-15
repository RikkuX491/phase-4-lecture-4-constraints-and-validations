from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hotel(db.Model):
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
