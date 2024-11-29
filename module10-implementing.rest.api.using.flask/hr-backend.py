import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from flask_socketio import SocketIO

from rest_utility.utils import extract_body

# region persistence layer
mongo_client = MongoClient('mongodb://localhost:27017')
hrdb = mongo_client['hrdb']
employees_collection = hrdb['employees']
# endregion

# region rest-api configuration
hr_rest_api = Flask(__name__)
hr_rest_api.config['DEBUG'] = True
cors = CORS(hr_rest_api)
socketio = SocketIO(hr_rest_api, cors_allowed_origins="*")

# endregion

# region rest-api layer
updatable_fields = ["fullname", "iban", "salary", "department", "fulltime", "photo"]


@hr_rest_api.route("/hr/api/v1/employees/<identity>", methods=['GET'])
def get_employees_by_identity(identity: str):
    return jsonify(employees_collection.find_one({"identity": identity}))


@hr_rest_api.route("/hr/api/v1/employees", methods=['GET'])
def get_employees():
    limit = request.args.get('limit')
    skip = request.args.get('skip')    
    return json.dumps([emp for emp in employees_collection.find({})])


@hr_rest_api.route("/hr/api/v1/employees", methods=['POST'])
def hire_employee():
    global socketio
    employee = request.get_json()
    employee["_id"] = employee["identity"]
    employees_collection.insert_one(employee)
    socketio.emit("hire", employee)
    return jsonify({"status": "ok"})


@hr_rest_api.route("/hr/api/v1/employees/<identity>", methods=['PUT', 'PATCH'])
def update_employee(identity: str):
    employee = extract_body(request, updatable_fields)
    employees_collection.find_one_and_update(
        {"_id": identity},
        {"$set": employee},
        upsert=False
    )
    return jsonify({"status": "ok"})


@hr_rest_api.route("/hr/api/v1/employees/<identity>", methods=['DELETE'])
def fire_employee(identity: str):
    global socketio
    employee = employees_collection.find_one({"identity": identity})
    employees_collection.delete_one({"identity": identity})
    socketio.emit("fire", employee)
    return jsonify(employee)


# endregion

socketio.run(hr_rest_api, port=7001)
