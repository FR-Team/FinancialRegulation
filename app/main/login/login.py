from flask import request,jsonify
from app.main import main

@main.route('/login', methods=['GET'])
def login():
    user = request.args.get('user')
    password = request.args.get('password')
    arr = ["123","123"]
    otherArr = ["456","456"]
    if user == "admin" and password == "admin":
        return jsonify(arr)
    else:
        return jsonify(otherArr)