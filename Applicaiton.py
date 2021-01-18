import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import config
import menuFunctions


class Application(tk.Frame):
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("1024x720")
        super().__init__(self.master)
        self.file = "No File Selected"
        self.pack()
        self.menu_bar()
        self.create_widgets()
        self.configurations()
        self.window()
        self.help_text()
        self.log()
        self.master.protocol('WM_DELETE_WINDOW', self.close)

    def close(self):
        """When you click to exit, this function is called"""
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            # menuFunctions.clean()
            self.master.destroy()

    def window(self):
        self.master.title("Pearler Controller")

    def menu_bar(self):
        self.menubar = Menu(self.master)
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Open", command=lambda: self.select_file())
        self.file_menu.add_separator()
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="Help Index", )
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        self.master.config(menu=self.menubar)

    def help_text(self):
        help =  """
                Use Arrow keys to move the XY motors
                use Z key to rotate pusher left
                use X key to rotate pusher right
                use C to activate pusher sequence
                use V key to toggle agitator on/off
                """
        self.help_text = Label(text=help, bg="#17202A", fg="#EAECEE")
        self.help_text.place(relx= 0.5, rely=0)

    def create_widgets(self):
        self.file_name = Label(text="File: " + self.file, bg="#17202A", fg="#EAECEE")
        self.file_name.place(relx=0, rely=0)

        self.start_button = tk.Button(activebackground="red")
        self.start_button["text"] = "Start Print"
        self.start_button["command"] = lambda: menuFunctions.start_print(self.file)
        self.start_button.place(relx=0, rely=0.66)

        self.quit_button = tk.Button(activebackground="red",)
        self.quit_button["text"] = "Cancel All Functions"
        self.quit_button["command"] = self.stop_all
        self.quit_button.place(relx=0.88, rely=.66)

        self.start_pause = tk.Button(activebackground="red")
        self.start_pause["text"] = "Pause"
        self.start_pause["command"] = self.pause_print
        self.start_pause.place(relx=0.8, rely=0.66)

    def configurations(self):
        self.title = Label(text="CONFIGURATIONS", bg="#17202A", fg="#EAECEE")
        self.title.place(relx=0, rely=0.03)

        self.x_motor = Label(text="X Motor: ", bg="#17202A", fg="#EAECEE")
        self.x_motor.place(relx=0, rely=0.06)
        x = StringVar(value=config.X_Motor_Configuration)
        self.x_config = Entry(textvariable=x)
        self.x_config.place(relx=0.1, rely=0.06)

        self.y_motor = Label(text="Y Motor: ", bg="#17202A", fg="#EAECEE")
        self.y_motor.place(relx=0, rely=0.09)
        y = StringVar(value=config.Y_Motor_Configuration)
        self.y_config = Entry(textvariable=y)
        self.y_config.place(relx=0.1, rely=0.09)

        self.rotation_motor = Label(text="Rotation Motor: ", bg="#17202A", fg="#EAECEE")
        self.rotation_motor.place(relx=0, rely=0.12)
        r = StringVar(value=config.Rotator_Motor_Configuration)
        self.r_config = Entry(textvariable=r)
        self.r_config.place(relx=0.1, rely=0.12)

        self.pusher_motor = Label(text="Pusher Motor: ", bg="#17202A", fg="#EAECEE")
        self.pusher_motor.place(relx=0, rely=0.15)
        p = StringVar(value=config.Pusher_Motor_Configuration)
        self.p_config = Entry(textvariable=p)
        self.p_config.place(relx=0.1, rely=0.15)

        self.agitator_motor = Label(text="Agitator Motor: ", bg="#17202A", fg="#EAECEE")
        self.agitator_motor.place(relx=0, rely=0.18)
        a = StringVar(value=config.Aggregator_Motor_Configuration)
        self.a_config = Entry(textvariable=a)
        self.a_config.place(relx=0.1, rely=0.18)

    def select_file(self):
        self.file = tk.filedialog.askopenfilename()
        self.send_message("File " + self.file + " selected")
        self.file_name["text"] = "File: " + self.file

    def log(self):
        # to show chat window
        # self.master.deiconify()
        # self.master.resizable(width=False,
        #                       height=False)
        self.master.configure(width=470,
                              height=500,
                              bg="#17202A")

        self.textCons = Text(self.master,
                             width=20,
                             height=2,
                             bg="#17202A",
                             fg="#EAECEE",
                             font="Helvetica 14",
                             padx=10,
                             pady=1)

        self.textCons.place(relheight=.3,
                            relwidth=1,
                            rely=0.7)
        self.textCons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
        scrollbar.place(relheight=1,
                        relx=0.99)
        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=DISABLED)

    def pause_print(self):
        self.send_message("print paused")

    def stop_all(self):
        return

    def root(self):
        return self.master

    def send_message(self, message):
        # insert messages to text box
        self.textCons.config(state=NORMAL)
        self.textCons.insert(END, message + "\n")

        self.textCons.config(state=DISABLED)
        self.textCons.see(END)
