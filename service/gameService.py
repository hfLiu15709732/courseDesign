import math
import random
import cvzone
import cv2
import numpy as np
import PySimpleGUI as sg
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

#设置画面的尺寸大小，过小的话导致贪吃蛇活动不开
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)


def start_aside_window(self):
    # 创建一个多列布局
    column1 = [[sg.Text('游戏信息', size=(10, 20), key='-INFO-')]]
    column2 = [[sg.Button('开始游戏')], [sg.Button('暂停游戏')], [sg.Button('退出游戏')], [sg.Button('重启游戏')]]

    upper_layout = [
        [sg.Column(column1), sg.Column(column2)]
    ]

    # 创建一个单列布局
    lower_layout = [
        [sg.Text('游戏道具')],
        [sg.Button('道具1'), sg.Button('道具2'), sg.Button('道具3'), sg.Button('道具4')]
    ]

    # 将两个布局组合在一起
    layout = [
        [sg.Frame('', upper_layout)],
        [sg.Frame('', lower_layout)]
    ]

    # 创建一个窗口
    window = sg.Window('贪吃蛇游戏', layout, size=(300, 600))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == '开始游戏':
            # 开始游戏的代码
            pass
        elif event == '暂停游戏':
            # 暂停游戏的代码
            pass
        elif event == '退出游戏':
            # 退出游戏的代码
            break
        elif event == '重启游戏':
            # 重启游戏的代码
            pass
        elif event in ['道具1', '道具2', '道具3', '道具4']:
            # 使用道具的代码
            pass

    window.close()


class SnakeGameClass:
  def __init__(self, pathFood):
      self.points = []  #贪吃蛇身上所有点
      self.lengths = []  #每一个点之间的距离
      self.currentLength = 0  #当下蛇的长度
      self.allowedLength = 50  #最大允许长度（阈值）
      self.previousHead = 0, 0  #手部关键点之后的第一个点

      self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED) #定义食物
      self.hFood, self.wFood, _ = self.imgFood.shape
      self.foodPoint = 0, 0
      self.randomFoodLocation()

      self.score = 0
      self.gameOver = False

  def randomFoodLocation(self):
      self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

  def update(self, imgMain, currentHead):
      #游戏结束，打印文本
      if self.gameOver:
          cvzone.putTextRect(imgMain, "Game Over", [300, 400],
                             scale=7, thickness=5, offset=20)
          cvzone.putTextRect(imgMain, f'Your Score: {self.score}', [300, 550],
                             scale=7, thickness=5, offset=20)
      else:
          px, py = self.previousHead
          cx, cy = currentHead

          self.points.append([cx, cy])
          distance = math.hypot(cx - px, cy - py)
          self.lengths.append(distance)
          self.currentLength += distance
          self.previousHead = cx, cy

          #长度缩小
          if self.currentLength > self.allowedLength:
              for i, length in enumerate(self.lengths):
                  self.currentLength -= length
                  self.lengths.pop(i)
                  self.points.pop(i)
                  if self.currentLength < self.allowedLength:
                      break

          #检查贪吃蛇是否已经触碰到食物
          rx, ry = self.foodPoint
          if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                  ry - self.hFood // 2 < cy < ry + self.hFood // 2:
              self.randomFoodLocation()
              self.allowedLength += 50
              self.score += 1
              print(self.score)

          #使用线条绘制贪吃蛇
          if self.points:
              for i, point in enumerate(self.points):
                  if i != 0:
                      cv2.line(imgMain, self.points[i - 1], self.points[i], (255, 0, 0), 13)
              cv2.circle(imgMain, self.points[-1], 20, (0, 255, 0), cv2.FILLED)

          #显示食物
          imgMain = cvzone.overlayPNG(imgMain, self.imgFood,
                                      (rx - self.wFood // 2, ry - self.hFood // 2))

          cvzone.putTextRect(imgMain, f'Score: {self.score}', [50, 80],
                             scale=3, thickness=3, offset=10)

          #检测是否碰撞
          pts = np.array(self.points[:-2], np.int32)
          pts = pts.reshape((-1, 1, 2))
          cv2.polylines(imgMain, [pts], False, (0, 255, 0), 3)
          minDist = cv2.pointPolygonTest(pts, (cx, cy), True)

          if -1 <= minDist <= 1:
              print("Hit")
              self.gameOver = True
              self.points = []  #蛇身上所有的点
              self.lengths = []  #不同点之间的距离
              self.currentLength = 0  #当前蛇的长度
              self.allowedLength = 50  #最大允许长度
              self.previousHead = 0, 0  #先前的蛇的头部
              self.randomFoodLocation()

      return imgMain



def start_game(self):
    game = SnakeGameClass("Donut.png")

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)  # 镜像翻转
        hands, img = detector.findHands(img, flipType=False)
        # 检测到第一个手，并标记手部位置
        if hands:
            lmList = hands[0]['lmList']
            pointIndex = lmList[8][0:2]  # 第八个坐标点的 x, y值，其中 z 值不被包括在里面
            # cv2.circle(img, pointIndex, 20, (200, 0, 200), cv2.FILLED) #在关键点处绘制一个圆点并进行填充（此处只是示范，后面会更改）
            img = game.update(img, pointIndex)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        # 按下‘r'重新开始游戏
        if key == ord('r'):
            game.gameOver = False

