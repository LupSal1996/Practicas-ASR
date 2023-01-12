from configuration.app.device.device_form_designer import deviceFormDesigner
from ftplib import FTP

class DownloadConfigDevice(deviceFormDesigner):

    def __init__(self):
        super().__init__()

    def move_config(self):

        # Se conecta por medio de FTP al router
        ftp = FTP(self.IP.get(), "rcp", "rcp")

        self.save_config(ftp, "startup-config")

        self.window.destroy()

    def save_config(self, ftp, filename):
        # Se descarga el archivo del router a la carpeta docs
        path = "docs\\"
        try:
            ftp.retrbinary("RETR " + filename, open(path + self.name.get() + "-sc", "wb").write)
        except Exception as e:
            print(e)

    