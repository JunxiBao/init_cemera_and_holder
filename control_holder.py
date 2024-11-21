import move_holder
def control_pantilt(direction):
    
    if direction == 'left':
        print("云台向左移动")
        # 添加控制云台向左的代码
        move_holder.move_left()
    elif direction == 'right':
        print("云台向右移动")
        # 添加控制云台向右的代码
        move_holder.move_right() 
    elif direction == 'up':
        print("云台向上移动")
        # 添加控制云台向上的代码
        move_holder.move_up()
    elif direction == 'down':
        print("云台向下移动")
        # 添加控制云台向下的代码
        move_holder.move_down()
    else:
        print("未知指令")
