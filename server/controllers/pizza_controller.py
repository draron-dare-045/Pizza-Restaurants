from flask import Blueprint, jsonify
from ..models import Pizza
from ..app import db

pizza_controller = Blueprint('pizzas', __name__)

@pizza_controller.route('/pizzas', methods=['GET']) #method to get all pizzas or get by id 
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'ingredients': p.ingredients
    } for p in pizzas])