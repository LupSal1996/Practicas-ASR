from util.device_button_designer import deviceButtonDesigner
import os
import tkinter as tk

class deleteDevice(deviceButtonDesigner):

    def __init__(self):
        super().__init__()
        
    
    def add_buttons_device(self):

        #Documento de agentes
        f = open("docs/agentes.txt", "r")
        i=0
        buttons=[]

        #Loop para mostrar botones de agentes
        for line in f:
            buttons.append(tk.Button(self.frame_buttons, text=line.strip(),font=('Times',12), bd=0, bg='#9400D3', fg='#ffffff',command=lambda name_device=line.strip(): self.delete_doc_line(name_device)))
            buttons[i].pack(fill=tk.X,padx=20,pady=10)
            i+=1
        f.close()


    def delete_doc_line(self, device):

        #Se destruye la ventana de dispositivos
        self.window.destroy()

        #Se eliminan los repostes de dispositivo
        if os.path.isfile('docs/'+device+'.pdf'):
            os.remove('docs/'+device+'.pdf')

        #Se elimina el disposivo del cocumento de agentes
        with open("docs/agentes.txt","r") as file:
            lines = file.readlines()
            with open('docs/agentes.txt', 'w') as fw:
                for line in lines:
                    if line.strip() != device:
                        fw.write(line)