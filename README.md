#  Pizza Restaurant API

A Flask-based RESTful API for managing pizza restaurants, their menus, and pizza offerings.

### Prerequisites
- Python 3.9+
- pipenv (`pip install pipenv`)

### Installation

git clone [your-repo-url]
cd PizzaRestaurantAPI


pipenv install #setup environment
pipenv shell #entering the environment shell


export FLASK_APP=server/app.py #enviroment variable


# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed sample data
python server/seed.py

# Postman 

# 1. Install and Setup Postman
Download from postman.com

Install and create an account (optional)

# 2. Import the API Collection
Click "Import" in top-left

Select your challenge-1-pizzas.postman_collection.json file

The collection will appear in the left sidebar under "Collections"

# 3. Set Up Your Environment
Click the eye icon 👁️ top-right → "Manage Environments"

Create a new environment called Local Dev

Add a variable:

Variable: baseUrl

Initial Value: http://localhost:5000

Select this environment from the dropdown

# 4 Testing Endpoints
GET All Restaurants
In Postman, open the "Pizza Restaurant API" collection

Click "GET All Restaurants"

Click Send (blue button)

Check response (status should be 200 with restaurant data)

# Database 
 SQLITE