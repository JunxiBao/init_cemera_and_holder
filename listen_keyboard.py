import control_holder
import cv2
def listen_keyboard(): 
# 监听键盘事件，控制云台
    key = cv2.waitKey(1) & 0xFF

    if key == ord('a'):  # 按 'a' 向左
        control_holder.control_pantilt('left')
    elif key == ord('d'):  # 按 'd' 向右
        control_holder.control_pantilt('right')
    elif key == ord('w'):  # 按 'w' 向上
        control_holder.control_pantilt('up')
    elif key == ord('s'):  # 按 's' 向下
        control_holder.control_pantilt('down')