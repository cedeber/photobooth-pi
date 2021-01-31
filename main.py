from gpiozero import Button
from time import sleep
from lib import LCD_2inch4
from PIL import Image, ImageDraw, ImageFont
from picamera import PiCamera, PiCameraCircularIO
from io import BytesIO
import time
import cv2

# Resources
display = LCD_2inch4.LCD_2inch4()
camera = PiCamera()
button = Button(1)
font = ImageFont.truetype("./assets/alkhemikal_16.ttf", 16)
stream = BytesIO()

# Init
display.Init()
display.clear()

# camera.resolution = (3280, 2464)
camera.resolution = (320, 240)
camera.hflip = True
# camera.rotation = -90
# camera.framerate = 30
camera.sensor_mode = 4  # Mode 2 for photo

while True:
    start_time = time.time()  # start time of the loop

    if button.is_pressed:
        text = u"Pressé"
    else:
        text = u"Relaché"

    camera.capture(stream, format='jpeg', use_video_port=True)
    stream.seek(0)  # Back to the beggining

    # image = Image.new("RGB", (display.width, display.height), "#242526")
    image = Image.open(stream)
    draw = ImageDraw.Draw(image)
    draw.text((5, 50), text, fill="white", font=font)

    # Reset the stream for the next capture
    stream.seek(0)
    stream.truncate()

    draw.text((5, 5), str(int(round(1.0 / (time.time() - start_time)))) + "fps",
              fill="white", font=font)

    # print(1.0 / (time.time() - start_time), "fps")
    display.ShowImage(image)
    # sleep(.2)
