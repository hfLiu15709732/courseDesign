from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from config.dbConfig import SQLManager

db_dict = {0: -65.25, 1: -56.99, 2: -51.67, 3: -47.74, 4: -44.62, 5: -42.03, 6: -39.82, 7: -37.89, 8: -36.17, 9: -34.63,
           10: -33.24,
           11: -31.96, 12: -30.78, 13: -29.68, 14: -28.66, 15: -27.7, 16: -26.8, 17: -25.95, 18: -25.15, 19: -24.38,
           20: -23.65,
           21: -22.96, 22: -22.3, 23: -21.66, 24: -21.05, 25: -20.46, 26: -19.9, 27: -19.35, 28: -18.82, 29: -18.32,
           30: -17.82,
           31: -17.35, 32: -16.88, 33: -16.44, 34: -16.0, 35: -15.58, 36: -15.16, 37: -14.76, 38: -14.37, 39: -13.99,
           40: -13.62,
           41: -13.26, 42: -12.9, 43: -12.56, 44: -12.22, 45: -11.89, 46: -11.56, 47: -11.24, 48: -10.93, 49: -10.63,
           50: -10.33,
           51: -10.04, 52: -9.75, 53: -9.47, 54: -9.19, 55: -8.92, 56: -8.65, 57: -8.39, 58: -8.13, 59: -7.88,
           60: -7.63,
           61: -7.38, 62: -7.14, 63: -6.9, 64: -6.67, 65: -6.44, 66: -6.21, 67: -5.99, 68: -5.76, 69: -5.55, 70: -5.33,
           71: -5.12, 72: -4.91, 73: -4.71, 74: -4.5, 75: -4.3, 76: -4.11, 77: -3.91, 78: -3.72, 79: -3.53, 80: -3.34,
           81: -3.15, 82: -2.97, 83: -2.79, 84: -2.61, 85: -2.43, 86: -2.26, 87: -2.09, 88: -1.91, 89: -1.75, 90: -1.58,
           91: -1.41, 92: -1.25, 93: -1.09, 94: -0.93, 95: -0.77, 96: -0.61, 97: -0.46, 98: -0.3, 99: -0.15, 100: 0.0}

def setting_voice_main(voice,isMute):
    # 获取音频设备
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))



    # 获取当前音量值
    current_volume = volume.GetMasterVolumeLevel()
    print(f"当前音量值: {current_volume}")

    # 获取音量范围
    volume_range = volume.GetVolumeRange()
    print(f"音量范围: {volume_range}")

    voice=int(voice)
    # 将音量百分比转换为分贝值
    # 设置音量
    volume.SetMasterVolumeLevel(db_dict[voice], None)
    # 使用列表和字符串格式化来生成消息
    print(f"已设置音量为{voice}%")

    # 设置是否静音
    volume.SetMute(isMute,None);
    muteList = ["非静音", "静音"]
    print(f"已设置属性为为{muteList[isMute]}%")

    # 判断是否静音
    is_mute = volume.GetMute()
    if is_mute:
        print("当前是静音状态")
    else:
        print("当前是非静音状态")


def setting_color_main(color,userid):
    db = SQLManager()
    data = db.get_list(f'UPDATE setting SET color = "{color}" WHERE userId = 1;')


