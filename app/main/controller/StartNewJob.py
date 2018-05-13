from app.main.model import DataProcess as dp
from flask import jsonify,request
from app.main import main


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
