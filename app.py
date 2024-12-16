from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from a .env file (for local development)
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'postgresql://user:password@localhost/dbname'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define routes
@app.route('/')
def index():
    return jsonify(message="Welcome to your Flask app connected to PostgreSQL!")

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users=[{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
