# controller/userController.py
from flask import Blueprint, jsonify

router = Blueprint('user', __name__)
# 获取注册路由的对应蓝图对象


# TODO userController 都还没写
@router.route('/user1', methods=['GET'])
def user1():
    return jsonify({"message": "User 1"}), 200

@router.route('/user2', methods=['GET'])
def user2():
    return jsonify({"message": "User 2"}), 200

@router.route('/user3', methods=['GET'])
def user3():
    return jsonify({"message": "User 3"}), 200
