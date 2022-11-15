from info_acquisition.app.device.device_form_designer import deviceFormDesigner
import rrdtool
import time


class addDevice(deviceFormDesigner):

    def __init__(self):
        super().__init__()

    # Agrega la información de los agentes a su documento
    def add_agent_info(self):
        self.agente = self.community.get() + " " + "1" + " " + self.port.get() + " " + self.IP.get() + "\n"
        print(self.agente)
        f = open("docs/agentes.txt", "a")
        f.write(self.agente)
        f.close()
        self.createdatabase(self.agente)
        self.window.destroy()

    def createdatabase(self, agent):
        agent = agent.split(" ")
        init = str(time.time())
        init = init.split('.')

        # Crea base
        ret = rrdtool.create("util/" + agent[0] + ".rrd",  # nombre base
                             "--start", init[0],
                             "--step", '300',  # tiempo de pasos
                             "DS:InterfG:COUNTER:120:U:U",  # contador
                             "DS:PcIP:COUNTER:120:U:U",  # contador
                             "DS:MsICMP:COUNTER:120:U:U",  # contador
                             "DS:SgTCP:COUNTER:120:U:U",  # contador
                             "DS:DgUDP:COUNTER:120:U:U",  # contador
                             "RRA:AVERAGE:0:1:576")
        self.createxml(agent)

        if ret:
            print(rrdtool.error())

    def createxml(self, agent):
        last_update = rrdtool.lastupdate("util/" + agent[0] + ".rrd")
        # Grafica desde la última lectura menos cinco minutos
        # print(last_update)
        tiempo_inicial = int(last_update['date'].timestamp()) - 300
        # print(tiempo_inicial)
        rrdtool.dump("util/" + agent[0] + ".rrd", "util/" + agent[0] + ".xml")  # crea xml
