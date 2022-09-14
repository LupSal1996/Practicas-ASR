import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tkFont
from tkinter import ttk
import os
from pysnmp.hlapi import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors



class PReporte:
    def __init__(self, root):
        self.master=root
        self.master.title("Reporte") 
        self.master.geometry("400x550") 

        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame, text="Comunidad-SNMPv-Puerto-IP").grid(column=0, row=0,ipady=10)
        self.desplegaReg()

    def desplegaReg(self):
        f = open("C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\agentes.txt", "r")
        i=1
        for linea in f:
            ttk.Button(self.frame, text=linea.strip(),command=lambda m=linea.strip(): self.producirReporte(m)).grid(column=0, row=i, columnspan = 3, pady=2)
            i+=1
        f.close()
    
    def producirReporte(self,datos):
        datosAgente = datos.split()
        tiposInterfaces={131:'Tunnel',71:'ieee80211',6:'ethernetCsmacd',24:'softwareLoopback'}
        estadoInterfaces={1:"Up",2:"Down",3:"Testing"}

        respuestas=[]
        OIDSGenerales=['1.3.6.1.2.1.1.1.0', '1.3.6.1.2.1.1.5.0','1.3.6.1.2.1.1.4.0','1.3.6.1.2.1.1.6.0','1.3.6.1.2.1.2.1.0']
        for oid in OIDSGenerales:
            respuestas.append((self.consulta(datosAgente[0],datosAgente[1],datosAgente[2],datosAgente[3],oid)))
        print(respuestas)

        if "Windows" in str(respuestas[0]):
            SO='Windows.jpg'
        elif "Ubuntu" in str(respuestas[0]):
            SO='Ubuntu.png'
        else:
            SO='Otro.jpg'


        interfaces=[]
        if int(respuestas[-1])>5:
            tope=6
        else:
            tope=int(respuestas[-1])
        for i in range(1,int(tope),1):
            interfaces.append(self.consulta(datosAgente[0],datosAgente[1],datosAgente[2],datosAgente[3],'1.3.6.1.2.1.2.2.1.3.'+str(i)))
            interfaces.append(self.consulta(datosAgente[0],datosAgente[1],datosAgente[2],datosAgente[3],'1.3.6.1.2.1.2.2.1.7.'+str(i)))
            
        print(interfaces)

        fileName = "C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\"+datos+".pdf"
        documentTitle = datos
        title = 'Administración de servicios en red'
        subTitle = 'Práctica 1-Saldaña Arcos Hilda G'
        textLines = [
        'Nombre del dispositivo: '+respuestas[1],
        'Información de contacto: '+respuestas[2],
        'Ubicación: '+respuestas[3],
        'Número de interfaces: '+respuestas[4]
        ]

        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)

        pdf.setFont("Times-Bold", 30)
        pdf.drawCentredString(300, 770, title)

        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Helvetica-BoldOblique", 24)
        pdf.drawCentredString(290, 720, subTitle)

        pdf.line(30, 710, 550, 710)

        textSO =pdf.beginText(60, 680)
        textSO.setFont("Courier",6)
        textSO.setFillColor(colors.red)
        textSO.textLine("S.O: "+respuestas[0])
        pdf.drawText(textSO)

        text = pdf.beginText(60, 650)
        text.setFont("Courier", 15)
        text.setFillColor(colors.red)
        for line in textLines:
            text.textLine(line)
        pdf.drawText(text)

        interf = pdf.beginText(60, 550)
        interf.setFont("Courier", 15)
        interf.setFillColor(colors.green)

        for i in range (0,int((tope-1)*2),2):
            if int(interfaces[i]) in tiposInterfaces:
                interf.textLine(interfaces[i]+": "+tiposInterfaces[int(interfaces[i])]+" - "+interfaces[i+1]+": "+estadoInterfaces[int(interfaces[i+1])])
                pdf.drawText(interf)
            else:
                interf.textLine(interfaces[i]+": otro tipo"+" - "+interfaces[i+1]+": "+estadoInterfaces[int(interfaces[i+1])])
                pdf.drawText(interf)

        image = 'C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\imagenes\\'+SO
        pdf.drawInlineImage(image, 0, 0)

        pdf.save()
                
        

    def consulta(self,comunidad,SNMPv,puerto,ip,OID):
        iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=0),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(OID))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            return(errorIndication)

        elif errorStatus:
            return('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

        else:
            for varBind in varBinds:
                aux=str(varBind).split("=")
                return(aux[1])



class Dregistro:
    def __init__(self, root):
        self.master=root
        self.master.title("Eliminar dispositivo") 
        self.master.geometry("400x550") 

        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame, text="Comunidad-SNMPv-Puerto-IP").grid(column=0, row=0,ipady=10)
        self.desplegaReg()
    
    def desplegaReg(self):
        f = open("C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\agentes.txt", "r")
        i=1
        for linea in f:
            ttk.Button(self.frame, text=linea.strip(),command=lambda m=linea.strip(): self.eliminarReg(m)).grid(column=0, row=i, columnspan = 3, pady=2)
            i+=1
        f.close()

    def eliminarReg(self,nomAgente):
        
        if os.path.isfile('C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\'+nomAgente+'.pdf'):
            os.remove('C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\'+nomAgente+'.pdf')
        else:
            print("No se encontró ningún reporte de este dispositivo")
        
        with open("C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\agentes.txt","r") as file:
            lines = file.readlines()
            with open('C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\agentes.txt', 'w') as fw:
                for line in lines:
                    if line.strip() != nomAgente:
                        fw.write(line)



class Wregistro: 

    def __init__(self, root):
        self.master=root
        self.master.title("Agregar dispositivo") 
        self.master.geometry("400x350") 

        self.frame = tk.Frame(root)
        self.frame.pack()

        labelS = tkFont.Font(family="Arial", size=11)

        st = ttk.Style(self.frame)
        st.configure("Alm.TButton", foreground="#FF5733", font="Arial")
        st.map("Alm.TButton", foreground=[("active", "#FFA500")])

        comunidad=tk.StringVar(self.frame)
        version=tk.StringVar(self.frame)
        puerto=tk.StringVar(self.frame)
        ip=tk.StringVar(self.frame)

        tk.Label(self.frame, text="Comunidad:",font=labelS,pady=10).grid(column=0, row=0, columnspan = 3)
        entryComunidad = tk.Entry(self.frame, width=20, textvariable=comunidad).grid(column=0, row=1, columnspan = 3)

        tk.Label(self.frame, text="Versión SNMP:",font=labelS,pady=10).grid(column=0, row=2, columnspan = 3)
        entryVersion = tk.Entry(self.frame, width=20, textvariable=version).grid(column=0, row=3, columnspan = 3)

        tk.Label(self.frame, text="Puerto:",font=labelS,pady=10).grid(column=0, row=4, columnspan = 3)
        entryPuerto = tk.Entry(self.frame, width=20, textvariable=puerto).grid(column=0, row=5, columnspan = 3)

        tk.Label(self.frame, text="IP:",font=labelS,pady=10).grid(column=0, row=6, columnspan = 3)
        entryIP= tk.Entry(self.frame, width=20, textvariable=ip).grid(column=0, row=7, columnspan = 3)

        sendButton = ttk.Button(self.frame,  text="Almacenar",style='Alm.TButton', command= lambda: self.writeDoc(comunidad,version,puerto,ip)).grid(column=0, row=9, columnspan = 3, pady=20)

        self.master.mainloop()

    def writeDoc(self,comunidad,version,puerto,ip):
        self.agente = comunidad.get() + " " + version.get() + " " + puerto.get() + " " + ip.get()+"\n"
        print(self.agente)
        f = open("C:\\Users\\lupit\\Desktop\\ASR\\Practica1\\agentes.txt","a")
        f.write(self.agente)
        f.close



class Aplicacion:
    def __init__(self, root):
        self.master = root
        self.master.title('Inicio')
        self.master.geometry('400x400')

        self.frame = tk.Frame(root)
        self.frame.pack()

        bold = tkFont.Font(family="Times new roman", size=13)
        options = tkFont.Font(family="Arial", size=12)

        s = ttk.Style()
        s.configure("Option.TButton", foreground="#FF5733", font="Arial")
        s.map("Option.TButton", foreground=[("active", "#FFA500")])

        tk.Label(self.frame, text="Sistema de adminsitación de red",font=bold).grid(column=0, row=0, columnspan = 3)
        tk.Label(self.frame, text="Práctica 1-Adquisición de información",font=bold).grid(column=0, row=1, columnspan = 3)
        tk.Label(self.frame, text="Saldaña Arcos Hilda G    4CM13     2020630549",font=bold).grid(column=0, row=2, columnspan = 3)
        
        tk.Label(self.frame, text="",font=options).grid(column=0, row=3,ipady=10)
        tk.Label(self.frame, text="Elige una opción:",font=options).grid(column=0, row=4,ipady=5)

        boton1 = ttk.Button(self.frame, text = '1- Agregar dispositivo',width = 20,style = 'Option.TButton', command=lambda: self.Nregistro(root)).grid(column=0, row=5, columnspan = 3, pady=2)
        boton2 = ttk.Button(self.frame, text = '2- Eliminar dispositivo', width = 20,style = 'Option.TButton', command=lambda: self.Eregistro(root)).grid(column=0, row=6,columnspan = 3, pady=2)
        boton3 = ttk.Button(self.frame, text = '3- Generar reporte', width = 20, style = 'Option.TButton', command=lambda: self.Preporte(root)).grid(column=0, row=7, columnspan = 3, pady=2)
        

    def Nregistro(self, root):
        root = tk.Tk()
        nuevo = Wregistro(root)
        root.mainloop()

    def Eregistro(self, root):
        root = tk.Tk()
        nuevo = Dregistro(root)
        root.mainloop()
    
    def Preporte(self, root):
        root = tk.Tk()
        nuevo = PReporte(root)
        root.mainloop()



def main(): 
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == '__main__':
    main()