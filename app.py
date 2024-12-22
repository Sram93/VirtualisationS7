from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
from bson import ObjectId
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

app = Flask(__name__)

# Vérification des variables d'environnement
try:
    DB_URI = os.environ['DB_URI']  # URI MongoDB, généralement sous la forme "mongodb://<user>:<password>@<host>:<port>/<dbname>"
except KeyError as e:
    raise Exception(f"Variable d'environnement manquante : {e}")

# Configuration de la connexion MongoDB
app.config["MONGO_URI"] = DB_URI
mongo = PyMongo(app)

# Autoriser les requêtes provenant d'une origine spécifique (par exemple, http://localhost:3000)
CORS(app, origins=["http://localhost", "http://localhost:3000", "http://localhost:80"], methods=["GET", "POST", "DELETE"])  # Ajoutez les origines nécessaires


# Route pour récupérer toutes les transactions
@app.route('/transactions', methods=['GET'])
def get_transactions():
    try:
        transactions = mongo.db.transactions.find()  # Accès à la collection "transactions"
        result = [
            {
                "id": str(t['_id']),  # Convertir l'ID MongoDB (ObjectId) en chaîne
                "amount": t['amount'],
                "type": t['type'],
                "description": t['description'],
                "date": t.get('date', None)
            }
            for t in transactions
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la récupération des transactions : {str(e)}"}), 500

# Route pour ajouter une transaction
@app.route('/transactions', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        if not data or 'amount' not in data or 'type' not in data or 'description' not in data:
            return jsonify({"error": "Les champs 'amount', 'type' et 'description' sont requis"}), 400

        new_transaction = {
            "amount": data['amount'],
            "type": data['type'],
            "description": data['description'],
            "date": data.get('date', None)  # Utilisez la date envoyée par le client ou None
        }

        result = mongo.db.transactions.insert_one(new_transaction)
        return jsonify({"message": "Transaction ajoutée avec succès", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": f"Erreur lors de l'ajout de la transaction : {str(e)}"}), 500


# Route pour supprimer une transaction
@app.route('/transactions/<string:id>', methods=['DELETE'])
def delete_transaction(id):
    try:
        # Vérification si l'ID est valide (ObjectId)
        if not ObjectId.is_valid(id):
            return jsonify({"error": "ID invalide"}), 400
        
        result = mongo.db.transactions.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Transaction non trouvée"}), 404
        return jsonify({"message": "Transaction supprimée avec succès"}), 200
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la suppression de la transaction : {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
