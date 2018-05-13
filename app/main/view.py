from flask import request,jsonify,render_template
from .import main


@main.route('/')
def main_index():
    return render_template('index.html')