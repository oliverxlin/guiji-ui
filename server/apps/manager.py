import imp
from flask import Blueprint, jsonify, request
import json

bp = Blueprint("manager", __name__, url_prefix="/server")

@bp.route("/testpost", methods=['POST'])
def testpost(): # 获取右向数据
    print("test post")
    return "test post"


@bp.route("/testget", methods=['GET'])
def testget():
    print("test get")
    return "test get"