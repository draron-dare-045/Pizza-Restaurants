from server.app import app, db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_database():
    with app.app_context():
        print("Resetting database...")
        db.drop_all()
        db.create_all()
        
        print("Creating restaurants...")
        restaurants = [
            Restaurant(name="Pizza Inn", address="123 Luthuli Street"),
            Restaurant(name="Swahili Dishes", address="456 Mombasa Ave"),
            Restaurant(name="Big Square ", address="Mombasa Road")
        ]
        
        print("Creating pizzas...")
        pizzas = [
            Pizza(name="Margherita chicken", ingredients="Tomato sauce, Mozzarella, Basil"),
            Pizza(name="Pepperoni beef", ingredients="Tomato sauce, Mozzarella, Pepperoni"),
            Pizza(name="Vegetarian", ingredients="Tomato sauce, Mozzarella, Bell peppers, Mushrooms, Olives")
        ]
        
        db.session.add_all(restaurants + pizzas)
        db.session.commit()
        
        print("Creating restaurant pizzas...")
        restaurant_pizzas = [
            RestaurantPizza(price=1000, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=1200, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=1500, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=800, restaurant_id=3, pizza_id=1)
        ]
        
        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()