from app.main.model import DataProcess as dp
from flask import jsonify, request
from app.main import main
import os


@main.route('/get_property', methods=['GET'])
def get_property():
    return jsonify(dp.get_property())


@main.route('/get_result', methods=['GET'])
def get_result():
    # 获取数据
    property_list = request.args.get('property_list')
    id = request.args.get('id')
    filename = id + ".csv"
    return jsonify(dp.kmeans_process(property_list, filename))


@main.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['the_file']
    fid = "fid"
    file.save(os.path.abspath('..') + '\\' + 'data')
    return ""
