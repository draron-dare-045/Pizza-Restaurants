from flask import Blueprint, jsonify, request
from ..models import RestaurantPizza, Restaurant, Pizza
from ..app import db

restaurant_pizza_controller = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_controller.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    if not data or 'price' not in data or 'pizza_id' not in data or 'restaurant_id' not in data:
        return jsonify({'errors': ['Missing required fields']}), 400
    
    try:
        price = int(data['price'])
        if price < 1 or price > 30:
            return jsonify({'errors': ['Price must be between 1 and 30']}), 400
    except ValueError:
        return jsonify({'errors': ['Price must be an integer']}), 400
    
    restaurant = Restaurant.query.get(data['restaurant_id'])
    pizza = Pizza.query.get(data['pizza_id'])
    
    if not restaurant or not pizza:
        return jsonify({'errors': ['Restaurant or Pizza not found']}), 400
    
    rp = RestaurantPizza(
        price=price,
        restaurant_id=restaurant.id,
        pizza_id=pizza.id
    )
    
    db.session.add(rp)
    db.session.commit()
    
    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201