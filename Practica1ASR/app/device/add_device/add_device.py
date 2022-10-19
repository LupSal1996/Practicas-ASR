from app.device.device_form_designer import deviceFormDesigner

class addDevice(deviceFormDesigner):

    def __init__(self):
        super().__init__()

    #Agrega la información de los agentes a su documento
    def add_agent_info(self):
        self.agente =  self.community.get() + " " + "1" + " " + self.port.get() + " " + self.IP.get() + "\n"
        print(self.agente)
        f = open("docs\\agentes.txt","a")
        f.write(self.agente)
        f.close
        self.window.destroy()