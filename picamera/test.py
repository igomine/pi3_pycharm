import time
import picamera
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    while True:
        pass
        pass
    # time.sleep(10)
    # camera.stop_preview()
    # camera.capture('foo.jpg')

# import picamera
#
# with picamera.PiCamera() as camera:
#
#     camera.resolution = (640, 480)
#     camera.start_recording('my_video.h264')
#     camera.wait_recording(10)
#     camera.stop_recording()