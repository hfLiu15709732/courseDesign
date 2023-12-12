from flask import  jsonify


def create_result(value, errorType):
    # 统一结果返回的公共工具，errorType是类型，
    if errorType == 200:
        data = {
            'data': value,
            'code': 200,
            'msg': None
        }
    elif errorType == 500:
        data = {
            'data': None,
            'code': 500,
            'msg': "服务器异常"
        }
    elif errorType == 401:
        data = {
            'data': None,
            'code': 401,
            'msg': "无权操作"
        }
    else:
        data = {
            'data': None,
            'code': 503,
            'msg': "未知异常"
        }
    return jsonify(data)
