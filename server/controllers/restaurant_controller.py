from flask import Blueprint, jsonify, request
from server.models import db, Restaurant

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants')
def get_restaurants():
    return jsonify([r.to_dict() for r in Restaurant.query.all()])

@restaurant_bp.route('/restaurants/<int:id>')
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant.to_dict_with_pizzas())

@restaurant_bp.route('/restaurants/<int:id>', methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
