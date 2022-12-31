
from accounting.app.main_menu.main_menu_designer import mainMenuDesigner
from accounting.app.device.report_device.report_device import reportDevice

class mainMenu_accounting(mainMenuDesigner):
    
    def __init__(self):
        super().__init__()

#ventana para agenerar un reporte
    def report_device(self):
        reportDevice()
