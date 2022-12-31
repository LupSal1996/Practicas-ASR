from util.graphRRD_performance import graph_rrd
import util.requestSNMP as rq
import time
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


class emaildevice:
    def __init__(self):
        self.device = ""
        self.answers_device = []
        self.element_warning = ""

    def information_device_search(self, device, element_warning):
        # Información para buscar el agente
        self.device = device.split()
        self.element_warning = element_warning

        # Bandera de error
        flag = 0

        # Peticiones que no son las de interfaces

        OID_general_info = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0']

        for oid in OID_general_info:
            self.answers_device.append(
                (rq.request(self.device[0], self.device[1], self.device[2], self.device[3], oid)))
            if self.answers_device[-1] == 'ERROR':
                flag = 1
        print(self.answers_device)

        if flag == 1:
            print('ERROR, Verifica que la información del agente sea correcta')

        self.creategraph()

    def creategraph(self):

        time_end = int(time.time())
        time_init = time_end - 1200
        print(time_init)
        print(time_end)

        title = ["Rendimiento CPU", "Rendimiento RAM", "Trafico de red"]
        var = ["CPUload", "RAMload", "NWload"]
        y = ["% carga CPU", "% carga RAM", "MB"]
        ul = ['100', '100', '300']
        var_desc = ["Carga del CPU", "Carga de la RAM", "MB en la red"]
        umbrales = [['25', '45', '60'], ['80', '85', '90'], ['195', '205', '215']]

        graph_rrd(str(int(time_init)), str(int(time_end)), self.device[0], title[0], '0', y[0], var[0], '0', ul[0],
                  var_desc[0], umbrales[0])
        graph_rrd(str(int(time_init)), str(int(time_end)), self.device[0], title[1], '1', y[1], var[1], '0', ul[1],
                  var_desc[1], umbrales[1])
        graph_rrd(str(int(time_init)), str(int(time_end)), self.device[0], title[2], '2', y[2], var[2], '0', ul[2],
                  var_desc[2], umbrales[2])

        self.sentemail("Actualización de rendimiento")

    def sentemail(self, notificacion):
        imgpath = 'docs/'

        subject = notificacion + self.answers_device[0] + self.element_warning
        mailsender = "dummycuenta3@gmail.com"
        mailreceip = "lupitavillalp96@gmail.comm"
        mailserver = 'smtp.gmail.com: 587'
        password = 'dvduuffmlhspbmjj'

        msgtext = self.answers_device[1] + " " + self.device[0] + " " + str(datetime.now())
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = mailsender
        msg['To'] = mailreceip

        msg.attach(MIMEText(msgtext, "plain"))

        for i in range(3):
            fp = open(imgpath + self.device[0] + '-' + str(i) + '.png', 'rb')
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)

        s = smtplib.SMTP(mailserver)

        s.starttls()
        # Login Credentials for sending the mail
        s.login(mailsender, password)

        s.sendmail(mailsender, mailreceip, msg.as_string())
        s.quit()
