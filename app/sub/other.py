from flask import request, jsonify
from . import sub


@sub.route('/register')
def register():
    user = request.args.get('user')
    password = request.args.get('password')
    if user == "admin" and password == "admin":
        return jsonify("Others Success")
    else:
        return jsonify("Others Fail")
