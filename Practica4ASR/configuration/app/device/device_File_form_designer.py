import tkinter as tk
from tkinter import BOTH
import util.generic_win as utl_win


class deviceFileFormDesigner:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x400")
        self.window.resizable(width=0, height=0)
        utl_win.center_window(self.window, 700, 600)

        # frame principal
        frame_main = tk.Frame(self.window, bd=0, padx=5, pady=5, bg='#800080')
        frame_main.pack(expand=tk.YES, fill=tk.BOTH)

        # Frame de titulo
        frame_title = tk.Frame(frame_main, bd=0)
        frame_title.pack(side="top", fill=tk.X)
        title = tk.Label(frame_title, text="Datos del enrutador", font=('Times', 15), bd=0, bg='#D8BFD8')
        title.pack(expand=tk.YES, fill=BOTH)

        # Frame de formulario
        frame_form = tk.Frame(frame_main, bd=0, padx=5, pady=5, bg='#DDA0DD')
        frame_form.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        # Etiqueta de nombre
        label_name = tk.Label(frame_form, text="Router:", font=('Times', 14), bd=0, bg='#DDA0DD', anchor="w")
        label_name.pack(fill=BOTH, padx=10, pady=5)

        # Entrada de nombre
        self.name = tk.Entry(frame_form, font=('Times', 14))
        self.name.pack(fill=tk.X, padx=20, pady=5)

        # Etiqueta de IP
        label_IP = tk.Label(frame_form, text="IP:", font=('Times', 14), bd=0, bg='#DDA0DD', anchor="w")
        label_IP.pack(fill=BOTH, padx=10, pady=5)

        # Entrada de ip
        self.IP = tk.Entry(frame_form, font=('Times', 14))
        self.IP.pack(fill=tk.X, padx=20, pady=5)

        # Etiqueta de comando
        label_command = tk.Label(frame_form, text="Ingresa los comandos", font=('Times', 14), bd=0, bg='#DDA0DD',
                                 anchor="w")
        label_command.pack(fill=BOTH, padx=10, pady=5)

        # Cuadro de texto de comandos
        self.command = tk.Text(frame_form, width=10, height=20, font=('Times', 10), bd=0, bg='#FFFFFF')
        self.command.pack(fill=tk.X, padx=5, pady=5)

        # Botton form
        button_add = tk.Button(frame_form, text="Listo", font=('Times', 12), bd=0, bg='#9400D3', fg='#ffffff',
                               command=lambda: self.create_config())
        button_add.pack(fill=tk.X, padx=20, pady=5)

        self.window.mainloop()

    def create_config(self):
        pass
