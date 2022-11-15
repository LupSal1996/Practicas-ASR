from util.device_button_designer import deviceButtonDesigner
import tkinter as tk
from tkinter import BOTH
from util.graphRRD import graph_rrd
import datetime

class graphDevice(deviceButtonDesigner):

    def add_buttons_device(self):

        # Documento de agentes
        f = open("docs/agentes.txt", "r")
        i = 0
        buttons = []

        # Frame de formulario
        frame_form = tk.Frame(self.frame_buttons, bd=0, padx=5, pady=5, bg='#DDA0DD')
        frame_form.pack(side='top', fill=tk.BOTH)

        # Fecha inicio
        label_dinit = tk.Label(frame_form, text="Fecha inicio:", font=('Times', 14), bd=0, bg='#DDA0DD', anchor="w")
        label_dinit.pack(fill=BOTH, padx=20, pady=5)

        # Entrada de comunidad
        self.dinit = tk.Entry(frame_form, font=('Times', 14))
        self.dinit.pack(fill=tk.X, padx=20, pady=10)

        # Fecha fin
        label_dend = tk.Label(frame_form, text="Fecha fin:", font=('Times', 14), bd=0, bg='#DDA0DD', anchor="w")
        label_dend.pack(fill=BOTH, padx=20, pady=5)

        # Etiqueta de valor version SNMP
        self.dend = tk.Entry(frame_form, font=('Times', 14))
        self.dend.pack(fill=tk.X, padx=20, pady=10)

        # Loop para mostrar botones de agentes
        for line in f:
            buttons.append(
                tk.Button(self.frame_buttons, text=line.strip(), font=('Times', 12), bd=0, bg='#9400D3', fg='#ffffff',
                          command=lambda name_device=line.strip(): self.creategraph(name_device)))
            buttons[i].pack(fill=tk.X, padx=20, pady=10)
            i += 1
        f.close()

    def creategraph(self, device):

        print(self.dinit.get())
        print(self.dend.get())

        init= datetime.strptime(self.dinit.get(), "%Y/%m/%d %H:%M:%S").timestamp()
        end = datetime.strptime(self.dend.get(), "%Y/%m/%d %H:%M:%S").timestamp()

        device = device.split(" ")
        title = ["Paquetes multicast que ha enviado una interfaz", "Paquetes IP suministrados en solicitudes de "
                                                                  "transmisión", "Mensajes ICMP recibidos",
                 "Segmentos TCP retransmitidos", "Datagramas enviados por el dispositivo"]
        y = ["Paquetes", "Paquetes", "Mensajes", "Segmentos", "Datagramas"]
        var = ["InterfG", "PcIP", "MsICMP", "SgTCP", "DgUDP"]
        i = 0
        for tt in title:
            graph_rrd(init, end, device[0], tt, i, y[i], var[i])
            i+=1
