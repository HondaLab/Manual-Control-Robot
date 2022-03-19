# Manual Control Robot
RasPiロボット(SSRX)で，ラジコンで操縦するプログラムです．
## プレステ3のコントローラーでラジコン 
以下のIPアドレス指定をPS3コントローラーを接続したPCと，ロボット双方で行う．

modules/socket.py のなかのIPアドレス

robot='172.16.xxx.yyy'

をロボットのIPアドレスに変更する．

その後，
PS3コントローラを接続したPCで ps3.pyを実行．
PS3コントローラーのスティック操作が値として表示されると同時に，
先に指定したIPアドレスにその値が送られる．

ロボットでssr3ps3.pyを実行する．
コントローラーの値を受け取って，ロボットのサーボモータを駆動する．


## 簡便にキーボードだけで，
前進，後退，右折，左折などを行います．

## Piカメラの向きを距離センサで制御
実行プログラム：ssr101b.py 
制御のアルゴリズムは modules/rc3c.py 内のKeyAssignクラスupdateメソッドの中に．

tofセンサーを４つ搭載した．
対応表

|ssr101b |tofL | tofR | tofC | tofM |
---------|-----|------|------|------|
|vl53_6a |tof1 | tof2 | tof3 | tof4 |
|gpio    |22   |  4   | 17   |  27  |

## GPIOの変更
SSR2.1/3.1 でGPIOを大幅に変更する．
基盤上のピン配置と配線スペースの都合上．


motorL:23; motorR:14
camera servo:18

(2021 11/24)

## 必要なもの (Requirement)
### pigpiod
```
sudo apt-get install pigpiod
sudo pigpiod
```

### OpenCV
```
sudo apt-get install python3-opencv
```

## rcXX.pyを実行してください．
```
python3 rcXY.py
```

## キーボードで操縦します (Control by keyboard)

  - q: 終了
  - s: stop
  - f: 前進増速
  - d: 後退増速
  - j: 左折増速
  - k: 右折増速
  - h: 左折
  - l: 右折


