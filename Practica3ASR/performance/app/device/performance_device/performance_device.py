from util.device_button_designer import deviceButtonDesigner
import tkinter as tk
from performance.app.device.performance_device.email_device import emaildevice as ed


class performanceDevice(deviceButtonDesigner):

    def __init__(self):
        super().__init__()

    def add_buttons_device(self):
        # Documento de agentes
        f = open("docs/agentes.txt", "r")
        i = 0
        buttons = []
        edi=ed()

        # Loop para mostrar botones de agentes
        for line in f:
            buttons.append(
                tk.Button(self.frame_buttons, text=line.strip(), font=('Times', 12), bd=0, bg='#9400D3', fg='#ffffff',
                          command=lambda name_device=line.strip(): edi.information_device_search(name_device, "")))
            buttons[i].pack(fill=tk.X, padx=20, pady=10)
            i += 1
        f.close()
