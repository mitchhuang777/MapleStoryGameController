## 楓之谷『腳』本 - MapleStoryGameController

此專案的初衷是為了幫助那些無法使用手部進行遊戲的人們，特別是具有手部功能障礙或行動不便的玩家。透過這個裝置，他們可以通過娃娃機搖桿和腳踏開關來進行楓之谷（MapleStory）遊戲的控制。以下是專案的主要目的與功能：

1. 提供遊戲體驗：專案旨在提供一種更加包容和無障礙的遊戲控制方式，讓那些無法使用手部進行遊戲的人們也能夠享受到楓之谷遊戲的樂趣。

2. 搖桿控制角色移動：透過娃娃機搖桿的上下左右移動，玩家可以輕鬆控制遊戲角色在楓之谷遊戲中的移動。

3. 腳踏開關控制角色技能：使用腳踏開關，玩家可以觸發角色的技能，例如攻擊、跳躍和範圍攻擊等按鍵操作。

4. 高度可自訂化：專案提供按鍵映射的設定，使玩家可以根據自己的喜好和遊戲需求，自定義搖桿和腳踏開關的控制功能。

5. 資源分享與社群參與：將專案的程式碼分享到 GitHub 上，讓有需要的玩家可以自行下載、修改和貢獻。

## 環境設定

- Arduino Uno
- Python 3.9.13 已安裝
- 已安裝 Arduino IDE

## Arduino 設定

1. 將 Arduino Uno 連接到電腦上。
2. 開啟 Arduino IDE。
3. 複製 `maplestory_game_arduino.ino` 的內容並貼到 Arduino IDE 中。
4. 選擇正確的開發板和連接埠設定。
5. 按下 "燒錄" 按鈕將程式燒錄到 Arduino Uno 上。

## Python 設定

1. 在終端機或命令提示字元中，導航到包含 `maplestory_game_control.py` 的目錄。
2. 執行以下命令安裝所需的 Python 套件：

`pip install pyserial keyboard`

## 執行 Python

1. 確認 Arduino Uno 已經成功燒錄並連接到電腦上。
2. 在終端機或命令提示字元中，執行以下命令以運行 Python 程式：

`python maplestory_game_control.py`

3. 程式運行後，它將開始監聽 Arduino Uno 發送的腳位狀態。
4. 確保 Arduino Uno 和遊戲中的角色技能設定相符。
5. 使用娃娃機搖桿控制角色的上下左右移動，使用腳踏開關觸發角色的技能。

## 腳位說明

以下是 Arduino 程式碼中使用的腳位說明：

- `pinDown` (下方向腳位): 5
- `pinUp` (上方向腳位): 4
- `pinRight` (右方向腳位): 7
- `pinLeft` (左方向腳位): 6
- `pinPedal1` (腳踏板1腳位): 10
- `pinPedal2` (腳踏板2腳位): 11
- `pinPedal3` (腳踏板3腳位): 12

## Demo

請查看以下連結以觀看專案的運行影片：

[楓之谷黑科技 | 我寫了一個史上最安全、防測謊『腳』本、V252以後皆適用！#arduino](https://youtu.be/K-W-LrIBjXw)

## 支持
感謝您關注並支持我的工作！如果您欣賞我的作品，歡迎在「Buy Me a Coffee」平台上為我買一杯咖啡，這將給予我更多資源和動力來創造更好的項目。感謝您的慷慨支持！
