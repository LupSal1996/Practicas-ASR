from util.device_button_designer import deviceButtonDesigner
import util.requestSNMP as rq
import tkinter as tk
from tkinter import BOTH
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from util.graphRRD import graph_rrd
from datetime import datetime


class reportDevice(deviceButtonDesigner):

    def add_buttons_device(self):

        print("Formato: AAAA/MM/DD HH:MM:SS")

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

        # Entrada de fecha inicio
        self.dinit = tk.Entry(frame_form, font=('Times', 14))
        self.dinit.pack(fill=tk.X, padx=20, pady=10)

        # Fecha fin
        label_dend = tk.Label(frame_form, text="Fecha fin:", font=('Times', 14), bd=0, bg='#DDA0DD', anchor="w")
        label_dend.pack(fill=BOTH, padx=20, pady=5)

        # Etiqueta de fecha fin
        self.dend = tk.Entry(frame_form, font=('Times', 14))
        self.dend.pack(fill=tk.X, padx=20, pady=10)

        # Loop para mostrar botones de agentes
        for line in f:
            buttons.append(
                tk.Button(self.frame_buttons, text=line.strip(), font=('Times', 12), bd=0, bg='#9400D3', fg='#ffffff',
                          command=lambda name_device=line.strip(): self.information_device_search (name_device)))
            buttons[i].pack(fill=tk.X, padx=20, pady=10)
            i += 1
        f.close()

    def information_device_search(self, device):
        # Información para buscar el agente
        self.device = device.split()

        # Bandera de error
        flag = 0

        # Peticiones que no son las de interfaces
        answers_device = []
        #  OID_general_info = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.25.1.2.0', '1.3.6.1.2.1.67.2.2.1.1.3.1.2.1',
        #                     '1.3.6.1.2.1.67.2.2.1.1.3.1.3.1', '1.3.6.1.2.1.67.2.2.1.1.3.1.3.1', '1.3.6.1.2.1.1.4.0',
        #                    '1.3.6.1.2.1.67.2.2.1.1.3.1.3.1', '1.3.6.1.2.1.67.2.2.1.1.3.1.4.1',
        #                   '1.3.6.1.2.1.67.2.2.1.1.3.1.3.1', '1.3.6.1.2.1.67.2.2.1.1.3.1.3.1',
        #                  '1.3.6.1.4.1.9.9.163.1.2.3.1.12']

        OID_general_info = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.4.0', '1.3.6.1.2.1.4.2.0', '1.3.6.1.2.1.2.2.1.10.1',
                            '1.3.6.1.2.1.2.2.1.16.1', '1.3.6.1.2.1.1.3.0', '1.3.6.1.2.1.2.2.1.11.1',
                            '1.3.6.1.2.1.2.2.1.17.1']

        for oid in OID_general_info:
            answers_device.append((rq.request(self.device[0], self.device[1], self.device[2], self.device[3], oid)))
            if answers_device[-1] == 'ERROR':
                flag = 1
        print(answers_device)

        if flag == 1:
            print('ERROR, Verifica que la información del agente sea correcta')
            self.window.destroy()


        self.creategraph(device)
        self.createPDF(answers_device, device)


    def creategraph(self, device):

        time_init = datetime.strptime(
            self.dinit.get(), "%Y/%m/%d %H:%M:%S"
        ).timestamp()

        time_end = datetime.strptime(
            self.dend.get(), "%Y/%m/%d %H:%M:%S"
        ).timestamp()

        print(time_init)
        print(time_end)

        device = device.split(" ")
        title = ["Paquetes unicast que ha recibido una interfaz", "Paquetes IP suministrados en solicitudes de "
                                                                  "transmisión", "Mensajes ICMP recibidos",
                 "Segmentos TCP retransmitidos", "Datagramas enviados por el dispositivo"]
        y = ["Paquetes", "Paquetes", "Mensajes", "Segmentos", "Datagramas"]
        var = ["InterfG", "PcIP", "MsICMP", "SgTCP", "DgUDP"]
        i = 0
        for tt in title:
            graph_rrd(str(int(time_init)), str(int(time_end)), device[0], tt, i, y[i], var[i])
            i+=1


    def createPDF(self, info, device):

        # Bloques principales del PDF
        fileName = "docs/" + device + "-2" + ".pdf"
        documentTitle = device
        title = 'Administración de servicios en red'
        subTitle = 'Práctica 2-Saldaña Arcos Hilda G'

        textLines = [
            'Version: 1',
            'Device: agente monitorizado',
            'Description: agente monitorizado ' + info[0],
            'Date: ' + str(datetime.now()),
            'defaultProtocol: radius',
            'rdate: ' + str(datetime.now()),
            '#NAS-IP-Address',
            '4: ' + self.device[3],  # numero al final
            '#NAS-Port',
            '5: 61',
            '#NAS-Port-Type',
            '61: 1',
            '#User-Name',
            '1: ' + info[1],
            '#Acct-Status-Type',
            '40: 1',
            '#Acct-Delay-Time',  # Tiempo de vida insetado en encabezado ip
            '41: ' + info[2],
            '#Acct-Input-Octets',  # octetos recibidos en la interface
            '47: ' + info[3],
            '#Acct-Output-Octets',
            '48: ' + info[4],  # octetos recibidos en la interface
            '#Acct-Session-Id',
            '44: ' + self.device[3],
            '#Acct-Authentic',
            '45: 1',
            '#Acct-Session-Time',  # Sistema se reinicio por ultima vez
            '46: ' + info[5],
            '#Acct-Input-Packets',  # Paquetes unicast de entrada
            '47: ' + info[6],
            '#Acct-Output-Packets',  # Paquetes unicast de salida
            '48: ' + info[7],
            '#Acct-Terminate-Cause',
            '49: 11',
            '#Acct-Multi-Session-Id',
            '50: ' + self.device[3] + '-' + self.device[0],
            '#Acct-Link-Count',
            '#51: 2'
        ]

        print(textLines)

        # Se crea un lienzo para el documento
        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)

        # Se definen las caracteristicas de los bloques anteriores
        pdf.setFont("Times-Bold", 30)
        pdf.drawCentredString(300, 770, title)

        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Helvetica-BoldOblique", 24)
        pdf.drawCentredString(290, 720, subTitle)

        pdf.line(30, 710, 550, 710)

        # Se coloca la información general de agente
        text = pdf.beginText(60, 650)
        text.setFont("Courier", 12)
        text.setFillColor(colors.purple)
        for line in textLines:
            text.textLine(line)
        pdf.drawText(text)

        pdf.showPage()
        pdf.drawImage('docs/' + self.device[0] + '-0.png', 30, 100, 520, 300)
        pdf.drawImage('docs/' + self.device[0] + '-1.png', 30, 500, 520, 300)
        pdf.showPage()
        pdf.drawImage('docs/' + self.device[0] + '-2.png', 30, 100, 520, 300)
        pdf.drawImage('docs/' + self.device[0] + '-3.png', 30, 500, 520, 300)
        pdf.showPage()
        pdf.drawImage('docs/' + self.device[0] + '-4.png', 30, 500, 520, 300)
        pdf.showPage()

        pdf.save()
