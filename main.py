import cv2
from picamera2 import Picamera2
import listen_keyboard
import libcamera


def main():
    picamera = Picamera2()
    
    # 配置相机设置
    config = picamera.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)},
                                                   raw={"format": "SRGGB12", "size": (1920, 1080)})
    config["transform"] = libcamera.Transform(hflip=1, vflip=1)  # 水平和垂直翻转
    picamera.configure(config)
    picamera.start()

    while True:
        # 捕获帧
        frame = picamera.capture_array()

        # 转换为 BGR 格式
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # 显示图像
        cv2.imshow("Camera Output", frame)

        listen_keyboard.listen_keyboard()


if __name__ == "__main__":
    main()
