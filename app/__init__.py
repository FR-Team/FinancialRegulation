from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    user = request.args.get('user')
    password = request.args.get('password')
    if user == "admin" and password == "admin":
        return jsonify(True)
    else:
        return jsonify(False)

if __name__ == '__main__':
    app.run()
