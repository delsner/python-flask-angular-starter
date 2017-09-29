from flask import Flask, jsonify, Response, request
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

# mongodb config
DB_HOST_MONGO = 'mongodb://db:27017/'
DB_NAME_MONGO = "db"
DB_COLLECTION_MONGO = "board"
DB_USERNAME = 'root'
DB_PASSWORD = 'admin'

# mongodb connection
mongo_client = MongoClient(DB_HOST_MONGO)
mongo_client[DB_NAME_MONGO].authenticate(DB_USERNAME, DB_PASSWORD, mechanism='SCRAM-SHA-1')
db = mongo_client[DB_NAME_MONGO]
collection = db[DB_COLLECTION_MONGO]

# start flask app
app = Flask(__name__)

@app.route('/api/board/<board_id>', methods=['GET'])
def get_single_board(board_id):
    board = collection.find_one({"_id": ObjectId(board_id)})
    return dumps(board)

@app.route('/api/board', methods=['GET'])
def get_all_boards():
    boards = collection.find()
    return dumps(boards)

@app.route('/api/board', methods=['POST'])
def create_board():
    board = request.get_json()
    board_id = collection.insert_one(board).inserted_id
    return dumps(collection.find_one({"_id": board_id}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
