from xyMovement import move_x, move_y, total
from colorSelector import move_pusher, move_rotator, ctotal
from multiprocessing import Process

threadPearl = Process(target=lambda: thread_pearl([]))


def goto(startpointX, startpointY, startColor):
    move_rotator(startColor)
    move_pusher()
    # need to add sleep timer here so the bead can hav time to fall.
    move_x(startpointX)
    move_y(startpointY)


def pearl(print_list):
    threadPearl = Process(target=lambda: thread_pearl(print_list))
    threadPearl.start()
    print('thread Pearl started')


def thread_pearl(print_list):
    for point in print_list:
        if float(point[1])//2 == 1:
            goto(int(point[0]), int(point[1]), int(point[2]))
        else:
            goto(int("-"+point[0]), int(point[1]), int(point[2]))
    goto(-total.x_total, -total.y_total,  -ctotal.c_total)


def stop_all():
    threadPearl.terminate()
    threadPearl.join()
    print('stopped functions')
