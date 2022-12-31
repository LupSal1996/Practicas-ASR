from util.device_button_designer import deviceButtonDesigner
import util.requestSNMP as rq
import tkinter as tk
from pysnmp.hlapi import *
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class reportDevice(deviceButtonDesigner):

    def add_buttons_device(self):

        #Documento de agentes
        f = open("docs/agentes.txt", "r")
        i=0
        buttons=[]

        #Loop para mostrar botones de agentes
        for line in f:
            buttons.append(tk.Button(self.frame_buttons, text=line.strip(),font=('Times',12), bd=0, bg='#9400D3', fg='#ffffff',command=lambda name_device=line.strip(): self.information_device_search(name_device)))
            buttons[i].pack(fill=tk.X,padx=20,pady=10)
            i+=1
        f.close()

    def information_device_search(self,device):
        #Información para buscar el agente
        self.device = device.split()

        #Bandera de error
        flag=0

        #Peticiones que no son las de interfaces
        answers_device=[]
        OID_general_info=['1.3.6.1.2.1.1.1.0', '1.3.6.1.2.1.1.5.0','1.3.6.1.2.1.1.4.0','1.3.6.1.2.1.1.6.0','1.3.6.1.2.1.2.1.0']
      
        for oid in OID_general_info:
            answers_device.append((rq.request(self.device[0],self.device[1],self.device[2],self.device[3],oid)))
            if answers_device[-1]=='ERROR':
                flag=1
        #print(answers_device)

        if flag==1:
            print('ERROR, Verifica que la información del agente sea correcta')
            self.window.destroy()

        #peticiones de interfaces
        interfaces=[]
        if int(answers_device[-1])>5:
            top=5
        else:
            top=int(answers_device[-1])        
        for i in range(1,int(top+1),1):
            interfaces.append(rq.request(self.device[0],self.device[1],self.device[2],self.device[3],'1.3.6.1.2.1.2.2.1.2.'+str(i)))
            interfaces.append(rq.request(self.device[0],self.device[1],self.device[2],self.device[3],'1.3.6.1.2.1.2.2.1.7.'+str(i)))
        self.createPDF(answers_device,interfaces,device,top)


    def createPDF(self, info, interfaces, device,top):

        #Estado de las interfaces
        interace_state={1:"Up",2:"Down",3:"Testing"}

        #Determinación de la imagen dependiendo el sistema operativo
        if "Windows" in str(info[0]):
            SO='Windows.jpg'
        elif "Ubuntu" in str(info[0]):
            SO='Ubuntu.png'
        else:
            SO='Otro.jpg'

        #Bloques principales del PDF
        fileName = "docs/"+device+".pdf"
        documentTitle = device
        title = 'Administración de servicios en red'
        subTitle = 'Práctica 1-Saldaña Arcos Hilda G'
        textLines = [
        'Nombre del dispositivo: '+info[1],
        'Información de contacto: '+info[2],
        'Ubicación: '+info[3],
        'Número de interfaces: '+info[4]
        ]

        #Se crea un lienzo para el documento
        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)

        #Se definen las caracteristicas de los bloques anteriores
        pdf.setFont("Times-Bold", 30)
        pdf.drawCentredString(300, 770, title)

        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Helvetica-BoldOblique", 24)
        pdf.drawCentredString(290, 720, subTitle)

        pdf.line(30, 710, 550, 710)
        
        #Se coloca la información sobre el SO
        textSO =pdf.beginText(20, 680)
        textSO.setFont("Courier",7)
        textSO.setFillColor(colors.red)
        textSO.textLine("S.O: "+info[0])
        pdf.drawText(textSO)

        #Se coloca la información general de agente
        text = pdf.beginText(60, 650)
        text.setFont("Courier", 15)
        text.setFillColor(colors.green)
        for line in textLines:
            text.textLine(line)
        pdf.drawText(text)

        #Se coloca la información de las interfaces
        interf = pdf.beginText(60, 550)
        interf.setFont("Courier", 12)
        interf.setFillColor(colors.purple)

        for i in range (0,int((top)*2)-1,2):

            interf_aux=interfaces[i]

            if "Windows" in str(info[0]):
                interf_aux=bytearray.fromhex(interf_aux[3:])
                interf_aux=interf_aux.decode()
            

            interf.textLine(interf_aux+ "- "+interfaces[i+1]+": "+interace_state[int(interfaces[i+1])])
            pdf.drawText(interf)
            interf.textLine("------------------------------------")
            pdf.drawText(interf)

        #Se coloca el logo del SO
        image = 'imagenes/'+SO
        pdf.drawInlineImage(image, 0, 0)

        pdf.save()
