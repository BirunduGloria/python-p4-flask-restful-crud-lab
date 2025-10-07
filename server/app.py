from flask import Flask, request, jsonify, make_response
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)

# GET /plants/:id
@app.route('/plants/<int:id>', methods=['GET'])
def get_plant(id):
    plant = db.session.get(Plant, id)
    
    if not plant:
        return jsonify({"error": "Plant not found"}), 404
    
    return jsonify({
        "id": plant.id,
        "name": plant.name,
        "image": plant.image,
        "price": plant.price,
        "is_in_stock": plant.is_in_stock
    }), 200


# PATCH /plants/:id
@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = db.session.get(Plant, id)

    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    data = request.get_json()

    if "is_in_stock" in data:
        plant.is_in_stock = data["is_in_stock"]

    db.session.commit()

    return jsonify({
        "id": plant.id,
        "name": plant.name,
        "image": plant.image,
        "price": plant.price,
        "is_in_stock": plant.is_in_stock
    }), 200


# DELETE /plants/:id
@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = db.session.get(Plant, id)

    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    db.session.delete(plant)
    db.session.commit()

    return make_response("", 204)  # 204 means No Content


if __name__ == '__main__':
    app.run(port=5555, debug=True)
