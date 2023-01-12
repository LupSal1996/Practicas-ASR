import tkinter as tk
from tkinter import BOTH
import util.generic_win as utl_win


class mainMenuDesigner:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menú principal")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        utl_win.center_window(self.window, 500, 400)

        # frame principal
        frame_main = tk.Frame(self.window, bd=0, padx=5, pady=5, bg='#800080')
        frame_main.pack(expand=tk.YES, fill=tk.BOTH)

        # Frame de titulo
        frame_title = tk.Frame(frame_main, bd=0)
        frame_title.pack(side="top", fill=tk.X)
        title = tk.Label(frame_title,
                         text="Sistema de adminsitación de red \n Prácticas \n Saldaña Arcos Hilda    4CM13     "
                              "2020630549",
                         font=('Times', 15), bd=0, bg='#D8BFD8')
        title.pack(expand=tk.YES, fill=BOTH)

        # Frame de botones
        frame_buttons = tk.Frame(frame_main, bd=0, padx=5, pady=5, bg='#DDA0DD')
        frame_buttons.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        # Etiqueta de instracciones
        label_choice = tk.Label(frame_buttons, text="Elige una opción:", font=('Times', 14), bd=0, bg='#DDA0DD')
        label_choice.pack(fill=tk.X, padx=20, pady=20)

        # Botton opcion 1
        button_choice1 = tk.Button(frame_buttons, text="1- Adquirir información de dispositivo", font=('Times', 12),
                                   bd=0, bg='#9400D3', fg='#ffffff', command=lambda: self.info_acquisition())
        button_choice1.pack(fill=tk.X, padx=20, pady=10)

        # Botton opcion 2
        button_choice2 = tk.Button(frame_buttons, text="2- Información de contabilidad de dispositivo",
                                   font=('Times', 12), bd=0, bg='#9400D3', fg='#ffffff',
                                   command=lambda: self.accounting())
        button_choice2.pack(fill=tk.X, padx=20, pady=10)

        # Botton opcion 3
        button_choice3 = tk.Button(frame_buttons, text="3- Monitorizar rendimiento de dispositivo",
                                   font=('Times', 12), bd=0, bg='#9400D3', fg='#ffffff',
                                   command=lambda: self.performance())
        button_choice3.pack(fill=tk.X, padx=20, pady=10)

        # Botton opcion 4
        button_choice4 = tk.Button(frame_buttons, text="4- Administración de configuración de routers",
                                   font=('Times', 12), bd=0, bg='#9400D3', fg='#ffffff',
                                   command=lambda: self.configuration())
        button_choice4.pack(fill=tk.X, padx=20, pady=10)

        self.window.mainloop()

    def info_acquisition(self):
        pass

    def accounting(self):
        pass

    def performance(self):
        pass

    def configuration(self):
        pass
    