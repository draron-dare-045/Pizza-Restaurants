import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pizza_restaurant.db' #setting up the db
    SQLALCHEMY_TRACK_MODIFICATIONS = False #so that Flask-SQLAlchemy does not track modifications of objects which can lead to our app being slow 