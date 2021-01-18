try:
    import RPi.GPIO as GPIO
    from multiprocessing import Process
    import time
    import threading
    from config import aggregator, aggregator_dir, Aggregator_Motor_Configuration

    GPIO.setmode(GPIO.BCM)

    CW = 1
    CCW = 0
    SPR = 50

    GPIO.setup(aggregator, GPIO.OUT)
    GPIO.setup(aggregator_dir, GPIO.OUT)
    GPIO.output(aggregator_dir, CW)
    delay = 0.01


    class ThreadA(threading.Thread):
        def __init__(self):
            super(ThreadA, self).__init__()
            self.stop = True

        def thread_move(self):
            while self.stop:
                GPIO.output(aggregator_dir, CW)
                for i in range(Aggregator_Motor_Configuration):
                    GPIO.output(aggregator, GPIO.HIGH)
                    time.sleep(delay)
                    GPIO.output(aggregator, GPIO.LOW)
                    time.sleep(delay)
                GPIO.output(aggregator_dir, CCW)
                for i in range(Aggregator_Motor_Configuration):
                    GPIO.output(aggregator, GPIO.HIGH)
                    time.sleep(delay)
                    GPIO.output(aggregator, GPIO.LOW)
                    time.sleep(delay)
                return

        def run(self):
            self.thread_move()


    thread_a = ThreadA()
    aggregatorProcess = Process(target=lambda: thread_a.thread_move())
    aggregatorProcess.start()


    def toggle():
        if not thread_a.stop:
            aggregator_on()
        else:
            aggregator_off()


    def aggregator_on():
        thread_a.stop = False


    def aggregator_off():
        thread_a.stop = True

except:
    print("loading as not a Raspberry pi")
