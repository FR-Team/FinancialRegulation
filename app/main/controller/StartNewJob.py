from app.main.model import DataProcess as dp
from flask import jsonify


# @main.route('/get_property', methods=['GET'])
def get_property():
    return jsonify(dp.get_property())


# @main.route('/get_result', methods=['GET'])
def get_result(property_list, id):
    # 获取数据
    filename = id + ".csv"
    return dp.kmeans_process(property_list, filename)
