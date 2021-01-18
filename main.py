from Applicaiton import Application
import xyMovement
import colorSelector
import aggregator


# the following class was converted to be used with GPIO from:
# https://robograham.wordpress.com/2014/02/24/servo-motors-being-controlled-by-directional-keys/
class Remote(object):
    def __init__(self):  # initial settings
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def key_pressed(self, event):  # when a key is pressed the event becomes true or for ecp in exit the program
        if event.keysym == 'Right':
            self.right = True
            xyMovement.move_x(10)
        elif event.keysym == 'Left':
            self.left = True
            xyMovement.move_x(-10)
        elif event.keysym == 'Up':
            self.up = True
            xyMovement.move_y(10)
        elif event.keysym == 'Down':
            self.down = True
            xyMovement.move_y(-10)

        elif event.keysym == 'z':
            self.down = True
            colorSelector.move_rotator(10)
        elif event.keysym == 'x':
            self.down = True
            colorSelector.move_rotator(-10)
        elif event.keysym == 'c':
            self.down = True
            colorSelector.move_pusher()
        elif event.keysym == 'v':
            self.down = True
            aggregator.toggle()

    def key_released(self, event):  # when the key is released the value becomes false again
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
        elif event.keysym == 'Down':
            self.down = False

        elif event.keysym == 'z':
            self.right = False
        elif event.keysym == 'x':
            self.left = False
        elif event.keysym == 'c':
            self.up = False
        elif event.keysym == 'v':
            self.down = False


remote = Remote()

app = Application()

app.root().bind_all('<Key>', remote.key_pressed)
app.root().bind_all('<KeyRelease>', remote.key_released)

app.mainloop()


