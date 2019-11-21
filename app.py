from flask import Flask, jsonify
api_app = Flask(__name__)

cats = ['Bengal', 'Persian', 'Siamese']


@api_app.route('/')
def hello_world():
    return 'Hello, IS 355!'


@api_app.route('/api/cat-breeds/')
def cat_breeds_index():
    return jsonify(cats)


@api_app.route('/api/cat-breeds/<int:id>')
def cat_breed(id):
    return jsonify(cats[id])
