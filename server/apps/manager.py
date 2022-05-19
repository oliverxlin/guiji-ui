from flask import Blueprint, jsonify, request, json
import numpy as np

bp = Blueprint("manager", __name__, url_prefix="/server")

@bp.route("/testpost", methods=['POST'])
def testpost(): # 获取右向数据
    print("test post")
    return "test post"


@bp.route("/testget", methods=['GET'])
def testget():
    print("test get")
    return "test get"

@bp.route("/gettestdata", methods=['GET'])
def gettestdata():
    data_path = "data/testdata%s.npy"
    data_id = request.args.get("data_id")
    print("!!!", data_id)
    data = np.load(data_path % data_id)
    print("load path data: ",  data.shape)
    ret_data = {"data_id" : data_id, "data" : data.T.tolist()}
    return jsonify(ret_data)