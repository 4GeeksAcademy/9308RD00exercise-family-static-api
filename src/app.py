"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)




@app.route('/members', methods=['POST'])
def create_member():
    member = request.json
    jackson_family.add_member(member)
    return jsonify(jackson_family.get_all_members())
    







@app.route('/members', methods=['PUT'])
def edit_member():
    new_menb = request.json
    jackson_family.replace_member(new_menb)
    return jsonify(jackson_family.get_all_members())











@app.route('/members/<int:id>', methods=['PATCH'])
def update_user(id):
    request_data = request.json                                                 # Get JSON data with updates
    updated_member = jackson_family.update_member(id, request_data)             # Attempt to update member attributes
    for key, value in request_data.items():                                     # VALIDATION: Loop through specified keys to update
        member = jackson_family.get_member(id)                                  # Get the current member data
        if member[key] == value:                                                # Check if the update was successful
            return jsonify(updated_member), 200                                 # Return updated member if successful
        else:
            return jsonify({"error": "Change could not be processed"}), 500     # Return error if update failed
    if updated_member:
        return jsonify(updated_member), 200                                     # VALIDATION: Return updated member if found and modified
    else:
        return jsonify({"error": "Member not found"}), 404      


    




@app.route('/members/<int:member_id>', methods=['DELETE'])
def remove_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify(jackson_family.get_all_members())







@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    


    return jsonify(members), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
