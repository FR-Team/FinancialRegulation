from flask import Flask, render_template

app = Flask(__name__,root_path='app/templates')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/login', methods=['GET'])
def login(user, password):
    if user == "admin" and password == "admin":
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
