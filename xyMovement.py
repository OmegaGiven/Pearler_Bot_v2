import threading
import time
try:
    import RPi.GPIO as GPIO
    from config import x, x_dir, y, y_dir, X_Motor_Configuration, Y_Motor_Configuration


    GPIO.setmode(GPIO.BCM)

    CW = 1
    CCW = 0
    SPR = 50
    delay = 0.001

    GPIO.setup(x, GPIO.OUT)
    GPIO.setup(x_dir, GPIO.OUT)
    GPIO.output(x_dir, CW)

    GPIO.setup(y, GPIO.OUT)
    GPIO.setup(y_dir, GPIO.OUT)
    GPIO.output(y_dir, CW)


    class totals:
        x_total = 0
        y_total = 0

        def get_x_total(self):
            return self.x_total

        def get_y_total(self):
            return self.y_total

        def set_x_total(self, new_x):
            self.x_total = new_x

        def set_y_total(self, new_y):
            self.y_total = new_y


    total = totals()


    def move_x(distance):
        if distance < 0:
            distance = distance * -1
            dir = CCW
            print("going counter clockwise")
        else:
            dir = CW
            print("clockwise")
        threadx = threading.Thread(target=thread_x(distance * X_Motor_Configuration, dir), args=(1,))
        print("threadx started with distance: " + str(distance))
        threadx.start()
        total.set_x_total(total.get_x_total() + distance)


    def thread_x(distance, dir):
        GPIO.output(x_dir, dir)
        for i in range(distance):
            GPIO.output(x, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(x, GPIO.LOW)
            time.sleep(delay)


    def move_y(distance):
        if distance < 0:
            distance = distance * -1
            dir = CCW
        else:
            dir = CW
        thready = threading.Thread(target=thread_y(distance * Y_Motor_Configuration, dir), args=(1,), )
        print("thready started with distance: " + str(distance))
        thready.start()
        total.set_y_total(total.get_y_total() + distance)


    def thread_y(distance, dir):
        GPIO.output(y_dir, dir)
        for i in range(distance):
            GPIO.output(y, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(y, GPIO.LOW)
            time.sleep(delay)


    def cleanpins():
        GPIO.cleanup()

except:
    print("loading as not a Raspberry pi")
