import serial
import keyboard

# 配置串口
ser = serial.Serial('COM3', 9600, timeout=0.01)

# 设置按键映射
key_map = {
    "Left": "left",
    "Right": "right",
    "Up": "up",
    "Down": "down",
    "Pedal1": "space",
    "Pedal2": "alt",
    "Pedal3": "delete"
}

# 跟踪当前按下的方向键和开关
pressed_keys = set()
pressed_pedals = set()
pedal_states = {}


while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        if line == '':
            continue
        # print(line)

        # 解析引脚状态信息
        states = line.split(" | ")
        for state in states:
            try:
                pin, value = state.split(": ")
            except:
                continue
            if pin in key_map:
                key = key_map[pin]
                if value == "0":
                    if key not in pressed_keys:
                        keyboard.press(key)
                        pressed_keys.add(key)
                        print(f"Pressed: {pin} ({key})")
                else:
                    if key in pressed_keys:
                        keyboard.release(key)
                        pressed_keys.remove(key)
                        print(f"Released: {pin} ({key})")
            elif pin.startswith("Pedal"):
                pedal_num = int(pin[5:])
                if value == "0":
                    if pedal_num not in pressed_pedals:
                        pressed_pedals.add(pedal_num)
                        if pedal_num == 1:
                            # keep pressing space, so that the character will keep jumping
                            keyboard.press("space")
                        elif pedal_num == 2:
                            keyboard.press("alt")
                        elif pedal_num == 3:
                            keyboard.press("delete")
                    else:
                        if pedal_num in pressed_pedals:
                            pressed_pedals.remove(pedal_num)
                            if pedal_num == 1:
                                keyboard.release("space")
                            elif pedal_num == 2:
                                keyboard.release("alt")
                            elif pedal_num == 3:
                                keyboard.release("delete")
