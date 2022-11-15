from info_acquisition.app.device.device_form_designer import deviceFormDesigner

class modifyDeviceDoc(deviceFormDesigner):

    def __init__(self, device):
        self.device=int(device)
        super().__init__()

    def add_agent_info(self):

        #Información de agente
        self.agent = self.community.get() + " " + "1" + " " + self.port.get() + " " +self.IP.get()

        #Documento de agentes
        lines=[]
        file = open("docs/agentes.txt","r")
        lines = [line.strip() for line in file]
        file.close()
        #print(lines)
        lines[self.device]=self.agent
        #print(lines)

        #Cambio de información
        with open('docs/agentes.txt', 'w') as file:
           file.writelines("\n".join(lines))

        self.window.destroy()