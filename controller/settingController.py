
from flask import Blueprint, request
from util.common import create_result
from service.settingService import setting_voice_main,setting_color_main
from config.dbConfig import SQLManager

router = Blueprint('setting', __name__)
# 获取注册路由的对应蓝图对象

@router.route('/voice', methods=['GET'])
def api_setting_voice():


    try:
        voice = request.args.get('voice')
        isMute = request.args.get('isMute')
        print(voice)
        setting_voice_main(int(voice), int(isMute))
        return create_result("修改成功", 200), 200
        pass
    except Exception as e:
        return create_result("修改失败，请重新尝试", 500), 500

@router.route('/test', methods=['GET'])
def api_setting_test():
    try:
        db = SQLManager()
        data = db.get_list('select * from tb_hotel;')
        return create_result(data, 200), 200
        pass
    except Exception as e:
        return create_result("修改失败，请重新尝试", 500), 500
    finally:
        db.close()



@router.route('/color', methods=['GET'])
def api_setting_color():

    try:
        mainColor = request.args.get('color')
        mainCircle = request.args.get('circle')
        color = f'{mainColor}&&{mainCircle}'
        setting_color_main(color, 1)

        return create_result("修改成功", 200), 200
        pass
    except Exception as e:
        return create_result("修改失败，请重新尝试", 500), 500
