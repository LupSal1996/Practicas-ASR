
from performance.app.main_menu.main_menu_designer import mainMenuDesigner
from performance.app.device.performance_device.performance_device import  performanceDevice

class mainMenu_performance(mainMenuDesigner):
    
    def __init__(self):
        super().__init__()

#ventana para enviar un reporte
    def performance_device(self):
        performanceDevice()
