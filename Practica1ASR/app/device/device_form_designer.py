import tkinter as tk
from tkinter import BOTH
import util.generic as utl


class deviceFormDesigner:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x400")
        self.window.resizable(width=0, height=0)
        utl.center_window(self.window, 500, 400)

        #frame principal
        frame_main = tk.Frame(self.window, bd=0, padx=5, pady=5, bg='#800080')
        frame_main.pack(expand=tk.YES,fill=tk.BOTH)

        #Frame de titulo
        frame_title = tk.Frame(frame_main, bd=0)
        frame_title.pack(side="top", fill=tk.X)
        title=tk.Label(frame_title, text="Datos del dispositivo", font=('Times',15), bd=0, bg='#D8BFD8')
        title.pack(expand=tk.YES, fill=BOTH)

        #Frame de formulario
        frame_form=tk.Frame(frame_main, bd=0, padx=5, pady=5, bg='#DDA0DD')
        frame_form.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        #Etiqueta de comunidad
        label_community=tk.Label(frame_form,text="Comunidad:", font=('Times',14), bd=0, bg='#DDA0DD', anchor="w")
        label_community.pack(fill=BOTH, padx=20, pady=5)

        #Entrada de comunidad
        self.community=tk.Entry(frame_form, font=('Times',14))
        self.community.pack(fill=tk.X,padx=20,pady=10)

        #Etiqueta de version SNMP
        label_version=tk.Label(frame_form,text="Versión SNMP:", font=('Times',14), bd=0, bg='#DDA0DD', anchor="w")
        label_version.pack(fill=BOTH, padx=20, pady=5)

        #Etiqueta de valor version SNMP
        label_valversion=tk.Label(frame_form,text="1", font=('Times',14), bd=0, bg='#DDA0DD', anchor="w")
        label_valversion.pack(fill=BOTH, padx=20, pady=5)

        #Etiqueta de puerto
        label_port=tk.Label(frame_form,text="Puerto:", font=('Times',14), bd=0, bg='#DDA0DD', anchor="w")
        label_port.pack(fill=BOTH, padx=20, pady=5)

        #Entrada de puerto
        self.port=tk.Entry(frame_form, font=('Times',14))
        self.port.pack(fill=tk.X,padx=20,pady=10)

        #Etiqueta de IP
        label_IP=tk.Label(frame_form,text="IP:", font=('Times',14), bd=0, bg='#DDA0DD', anchor="w")
        label_IP.pack(fill=BOTH, padx=20, pady=5)

        #Entrada de ip
        self.IP=tk.Entry(frame_form, font=('Times',14))
        self.IP.pack(fill=tk.X,padx=20,pady=10)
        
        #Botton form
        button_add=tk.Button(frame_form, text="Listo", font=('Times',12), bd=0, bg='#9400D3', fg='#ffffff', command=lambda: self.add_agent_info())
        button_add.pack(fill=tk.X,padx=20,pady=10)

        self.window.mainloop()

    def add_agent_info(self):
        pass
