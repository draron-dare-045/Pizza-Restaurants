from server.models import db, Restaurant, Pizza, RestaurantPizza
from server.app import create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Luigi's", address="123 Pasta Street")
    r2 = Restaurant(name="Mario's", address="456 Mushroom Ave")
    db.session.add_all([r1, r2])

    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Cheese, Pepperoni")
    db.session.add_all([p1, p2])
    db.session.commit()
