# controller/gameController.py
from flask import Blueprint
from threading import Thread
from util.common import create_result
from service.gameService import start_game,start_aside_window

router = Blueprint('game', __name__)
# 获取注册路由的对应蓝图对象

@router.route('/start', methods=['GET'])
def api_start():


    try:
        thread1 = Thread(target=start_game, args=("null",))
        thread2 = Thread(target=start_aside_window, args=("null",))

        # 开启动线程
        thread1.start()
        thread2.start()

        # TODO 如果其他页面用WEB的话，这块要改成websocket，这块返回开始游戏信息
        # 等待多线程结束
        thread1.join()
        thread2.join()

        # TODO 这块需要返回游戏结束信息
        # TODO 最后杀掉websocket
        return create_result("游戏结束", 200), 200
        pass
    except Exception as e:
        return create_result("修改失败，请重新尝试", 500), 500
