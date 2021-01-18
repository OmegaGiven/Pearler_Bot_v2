try:
    import Applicaiton
    from guizero import App, PushButton, MenuBar, Text, Slider, Box, yesno
    from xyMovement import move_x, move_y, cleanpins
    from aggregator import aggregator_on, aggregator_off
    from colorSelector import move_pusher, move_rotator
    from startPrint import pearl


    def start_print(file_name):
        if file_name.value == "none selected":
            Applicaiton.Application.send_message("None selected")
        else:
            print_list = load_file(file_name.value)
            pearl(print_list)
            print("success")


    def edit_function():
        return


    def clean():
        cleanpins()


    def load_file(file_name):
        loaded_file = []
        f = open(file_name, 'r')
        for line in f:
            line = line.rstrip('\n')
            val = line.split(',')
            for x in val:
                x = int(x)
            val_list = list(val)
            loaded_file.append(val_list)
        f.close()
        print(loaded_file)
        return loaded_file

except:
    print("guizero not supported on this device")
