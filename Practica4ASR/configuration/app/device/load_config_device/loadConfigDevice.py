from configuration.app.device.device_form_designer import deviceFormDesigner
from ftplib import FTP

class LoadConfigDevice(deviceFormDesigner):

    def __init__(self):
        super().__init__()

    def move_config(self):

        # Se conecta por medio de FTP al router
        ftp = FTP(self.IP.get(), "rcp", "rcp")

        self.load_config(ftp, "startup-config")

        self.window.destroy()

    def load_config(self, ftp, filename):
        # Se carga el archivo del router a la carpeta docs
        path = "docs\\"
        try:
            ftp.storbinary("STOR " + filename, open(path + self.name.get(), "rb"))
        except Exception as e:
            print(e)
