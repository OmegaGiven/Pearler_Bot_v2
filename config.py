"""
Configuration of Motors
    input the number used in manual control to drop to specific pins and holes for accurate movement.
"""
X_Motor_Configuration = 5
Y_Motor_Configuration = 5
x = 24
x_dir = 23
y = 7
y_dir = 8

Rotator_Motor_Configuration = 6
Pusher_Motor_Configuration = 80
rotator = 6
rotator_dir = 5
pusher = 22
pusher_dir = 27


aggregator = 21
aggregator_dir = 20
Aggregator_Motor_Configuration = 200

"""
Motor Configuration:
200 value is a 360deg angle
10.1deg angle is from center to center of each color selecting area on the main color selector.
5.61111111 is the actual value between the color selections
"""