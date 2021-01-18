try:
    import RPi.GPIO as GPIO
    import threading
    import time
    from config import pusher, pusher_dir, rotator, rotator_dir, Pusher_Motor_Configuration, Rotator_Motor_Configuration

    GPIO.setmode(GPIO.BCM)

    CW = 1
    CCW = 0
    SPR = 50
    delay = 0.01

    """ Top Pusher Pin setup """
    GPIO.setup(pusher, GPIO.OUT)
    GPIO.setup(pusher_dir, GPIO.OUT)
    GPIO.output(pusher_dir, CW)

    """ Rotator Pin setup """
    GPIO.setup(rotator, GPIO.OUT)
    GPIO.setup(rotator_dir, GPIO.OUT)
    GPIO.output(rotator_dir, CW)


    class ctotals:
        c_total = 0

        def get_c_total(self):
            return self.c_total

        def set_c_total(self, new_c):
            self.c_total = new_c


    ctotal = ctotals()


    def move_pusher():
        dir = CW
        threadx = threading.Thread(target=thread_pusher(Pusher_Motor_Configuration, dir), args=(1,))
        print("thread pusher started with distance: " + str(Pusher_Motor_Configuration))
        threadx.start()
        dir = CCW
        threadx = threading.Thread(target=thread_pusher(Pusher_Motor_Configuration, dir), args=(1,))
        print("thread pusher started with distance: " + str(Pusher_Motor_Configuration))
        threadx.start()


    def thread_pusher(distance, dir):
        GPIO.output(pusher_dir, dir)
        for i in range(distance):
            GPIO.output(pusher, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(pusher, GPIO.LOW)
            time.sleep(delay)


    def move_rotator(distance):
        if distance == ctotal.get_c_total():
            return
        else:
            move_amount = distance - ctotal.get_c_total() * Rotator_Motor_Configuration
            if move_amount < 0:
                dir = CCW
                thready = threading.Thread(target=thread_rotator(move_amount * -1, dir), args=(1,), )
                print("thread rotator started with distance: " + str(distance))
                thready.start()
                ctotal.set_c_total(distance)
            else:
                dir = CW
                thready = threading.Thread(target=thread_rotator(move_amount, dir), args=(1,), )
                print("thread rotator started with distance: " + str(distance))
                thready.start()
                ctotal.set_c_total(distance)


    def thread_rotator(distance, dir):
        GPIO.output(rotator_dir, dir)
        for i in range(distance):
            GPIO.output(rotator, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(rotator, GPIO.LOW)
            time.sleep(delay)

except:
    print("loading as not a Raspberry pi")
