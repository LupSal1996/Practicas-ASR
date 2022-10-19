import tkinter as tk
from tkinter import BOTH
import util.generic as utl


class deviceButtonDesigner:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x400")
        utl.center_window(self.window, 500, 400)

        #frame principal
        frame_main = tk.Frame(self.window, bd=0, padx=5, pady=5, bg='#800080')
        frame_main.pack(expand=tk.YES,fill=tk.BOTH)

        #Frame de titulo
        frame_title = tk.Frame(frame_main, bd=0)
        frame_title.pack(side="top", fill=tk.X)
        title=tk.Label(frame_title, text="Selecciona un dispositivo", font=('Times',15), bd=0, bg='#D8BFD8')
        title.pack(expand=tk.YES, fill=BOTH)

        #Frame de botones
        self.frame_buttons=tk.Frame(frame_main, bd=0, padx=5, pady=5, bg='#DDA0DD')
        self.frame_buttons.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        self.add_buttons_device()

        self.window.mainloop()
