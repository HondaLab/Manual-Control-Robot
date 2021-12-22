#!/usr/bin/python3
# Yasushi Honda 2021 12/23
# PS3のジョイスティック値を読み込んで、raspi にソケットで送る。
import pygame
from pygame.locals import *
import modules.socket as sk
import modules.keyin as kin

# ジョイスティックの初期化
pygame.joystick.init()
try:
   # ジョイスティックインスタンスの生成
   joystick = pygame.joystick.Joystick(1)
   joystick.init()
   print('ジョイスティックの名前:', joystick.get_name())
   print('ボタン数 :', joystick.get_numbuttons())
except pygame.error:
   print('ジョイスティックが接続されていません')

# pygameの初期化
pygame.init()

# 画面の生成
screen = pygame.display.set_mode((320, 320))

# ループ
udp=sk.UDP_Send(sk.robot,sk.port)
data=[]
key=kin.Keyboard()
active = True
count=0
ch='c'
while ch!='q':
   # イベントの取得
   for e in pygame.event.get():
       # 終了ボタン
       if e.type == QUIT:
           active = False

       # ジョイスティックのボタンの入力
       if e.type == pygame.locals.JOYAXISMOTION:
           count+=1
           #print(count, joystick.get_axis(0), joystick.get_axis(1))
           print("\r %d %10.7f %10.7f %10.7f %10.7f" % (count, joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(3), joystick.get_axis(4)),end='')
           data.append(joystick.get_axis(0))
           data.append(joystick.get_axis(1))
           data.append(joystick.get_axis(3))
           data.append(joystick.get_axis(4))
           udp.send(data)
           data.clear()
       '''
       elif e.type == pygame.locals.JOYBUTTONDOWN:
           print('ボタン'+str(e.button)+'を押した')
       elif e.type == pygame.locals.JOYBUTTONUP:
           print('ボタン'+str(e.button)+'を離した')
       '''

   ch=key.read()