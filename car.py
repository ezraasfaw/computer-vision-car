###################################
# Computer Vision Car project:    #
# follow directions of the car in #
# front by following the red back #
# light                           #
# Mechatronics                    #
# Ezra-Fikru Asfaw                #
###################################
import sensor, image, time
from tb6612 import Motor

motor1 = Motor(1) # A0 & A1
motor2 = Motor(2) # B0 & B1



x1 = 0
y1 = 0

x2 = 0
y2 = 0

thresholdInd = 0

# Color for tracking
thresholdInd = 0
thresholds = [  (15, 100, 30, 100, -30, 30),     # R
                (0, 0, 0, 0, 0, 0),              # G
                (0, 0, 0, 0, 0, 0)]              # B

if __name__ == '__main__':
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.skip_frames(time = 2000)
    clock = time.clock()

    while(True):
        clock.tick()
        img = sensor.snapshot()
        for blob in img.find_blobs([thresholds[thresholdInd]],roi=(0,0,160,240), pixels_threshold=200, area_threshold=2000, merge=True):
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy()) #values of x & y

            x1 = blob.cx()
            y1 = blob.cy()


        for blob in img.find_blobs([thresholds[thresholdInd]],roi=(161,0,320,240), pixels_threshold=200, area_threshold=2000, merge=True):
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())

            x2 = blob.cx()
            y2 = blob.cy()

        blob_list = img.find_blobs([thresholds[thresholdInd]], pixels_threshold=50, area_threshold=250, merge=False)
        blob_cnt = len(blob_list)



        #Halt
        if (blob_cnt < 2):
            motor1.set_speed(0)
            motor2.set_speed(0)
            print("Halt")

        #Forward
        elif ((x2-x1) < 150):
            motor1.set_speed(60)
            motor2.set_speed(-60)
            print("Forward")

        #Backwards
        elif ((x2-x1) > 200):
            motor1.set_speed(-60)
            motor2.set_speed(60)
            print("Backwards")

        #Left Turn
        elif ((x1<80) or (x2<240)):
            motor1.set_speed(60)
            motor2.set_speed(60)
            print("Left Turn")

        #Right Turn
        elif ((x1>140) or (x2>260)):
            motor1.set_speed(-60)
            motor2.set_speed(-60)
            print("Right Turn")

        else:
        #Stop
            print("stopped")
