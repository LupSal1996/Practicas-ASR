
from app.main_menu.main_menu_designer import mainMenuDesigner
from app.device.add_device.add_device import addDevice
from app.device.delete_device.delete_device import deleteDevice
from app.device.modify_device.modify_device import modifyDevice
from app.device.report_device.report_device import reportDevice

class mainMenu(mainMenuDesigner):
    
    def __init__(self):
        super().__init__()

    #ventana para agregar un dispositivo
    def add_device(self):
        addDevice()

    #ventana para eliminar un dispositivo
    def delete_device(self):
        deleteDevice()

    #ventana para modificar un dispositivo
    def modify_device(self):
        modifyDevice()

    #ventana para agenerar un reporte
    def report_device(self):
        reportDevice()
