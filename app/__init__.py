from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    user = request.args.get('user')
    password = request.args.get('password')
    arr = ["123","123"]
    otherArr = ["456","456"]
    if user == "admin" and password == "admin":
        return jsonify(arr)
    else:
        return jsonify(otherArr)

if __name__ == '__main__':
    app.run()
