from flask import Blueprint, jsonify
from server.models.pizza import Pizza
from server.models import db

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    response = [pizza.to_dict() for pizza in pizzas]
    return jsonify(response), 200
