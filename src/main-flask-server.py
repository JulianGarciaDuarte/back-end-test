from flask import Flask, request, jsonify
from PIL import Image

import redis

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "<p>Le serveur est activé!!!</p>"

@app.route("/load-img", methods=['POST'])
def load_img():
    # Retrieves the image as binary data
    bin_img = request.files['image']
    code = request.files['code']

    # Sends the image
    
    # Success message 
    return jsonify({'msg': 'success'})

@app.route("/get-code", methods=['GET'])
def get_code():
    #return jsonify({'code': manager.get_unique_id()})
    return jsonify({'code': 0})

@app.route("/load-model", methods=["POST"])
def load_model():

    # Retreives the model 
    bin_model = request.files['model']

    # Sends the model

    return jsonify({'model': 2})

app.run(host='0.0.0.0', port=80)


