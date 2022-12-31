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

        # Crea base practica 2
        ruta = "util/"
        ret = rrdtool.create("util/" + agent[0] + ".rrd",  # nombre base
                             "--start", init[0],
                             "--step", '300',  # tiempo de pasos
                             "DS:InterfG:COUNTER:120:U:U",  # contador
                             "DS:PcIP:COUNTER:120:U:U",  # contador
                             "DS:MsICMP:COUNTER:120:U:U",  # contador
                             "DS:SgTCP:COUNTER:120:U:U",  # contador
                             "DS:DgUDP:COUNTER:120:U:U",  # contador
                             "RRA:AVERAGE:0:1:576")
        self.createxml(agent, ruta)

        if ret:
            print(rrdtool.error())

        # Crea base practica 3
        ruta1 = "rrd_db/"
        ret1 = rrdtool.create("rrd_db/" + agent[0] + ".rrd",
                              "--start", 'N',
                              "--step",'60',
                              "DS:CPUload:GAUGE:60:0:100","RRA:AVERAGE:0.5:1:24",
                              "DS:RAMload:GAUGE:60:0:100","RRA:AVERAGE:0.5:1:24",
                              "DS:NWload:GAUGE:60:0:1000","RRA:AVERAGE:0.5:1:24")
        self.createxml(agent, ruta1)
        if ret1:
            print(rrdtool.error())

    def createxml(self, agent, ruta):
        last_update = rrdtool.lastupdate(ruta + agent[0] + ".rrd")
        # Grafica desde la última lectura menos cinco minutos
        # print(last_update)
        tiempo_inicial = int(last_update['date'].timestamp()) - 300
        # print(tiempo_inicial)
        rrdtool.dump(ruta + agent[0] + ".rrd", ruta + agent[0] + ".xml")  # crea xml
