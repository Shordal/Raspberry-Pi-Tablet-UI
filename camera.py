from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1080, 1080)
camera.image_effect = 'pastel'
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/Picture/Sketch.jpg')
camera.stop_preview()
