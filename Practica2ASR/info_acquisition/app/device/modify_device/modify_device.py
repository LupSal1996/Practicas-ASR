from util.device_button_designer import deviceButtonDesigner
from info_acquisition.app.device.modify_device.modify_device_doc import modifyDeviceDoc
import tkinter as tk


class modifyDevice(deviceButtonDesigner):

    def __init__(self):
        super().__init__()

    def add_buttons_device(self):

        #Documento de agentes
        f = open("docs\\agentes.txt", "r")
        i=0
        buttons=[]

        #Loop para mostrar botones de agentes
        for line in f:
            buttons.append(tk.Button(self.frame_buttons, text=line.strip(),font=('Times',12), bd=0, bg='#9400D3', fg='#ffffff',command=lambda num_device=str(i): self.form_change_line(num_device)))
            buttons[i].pack(fill=tk.X,padx=20,pady=10)
            i+=1
        f.close()

    def form_change_line(self, device):
        self.window.destroy()
        modifyDeviceDoc(device)