from configuration.app.main_menu.main_menu import mainMenu_configuration
from main_app_designer import mainMenuDesigner


class mainMenuApp(mainMenuDesigner):

    def __init__(self):
        super().__init__()

    # Practica 1
    def info_acquisition(self):
        print("")
        #mainMenu_info_acquisition()

    # Practica 2
    def accounting(self):
        print("")
        #mainMenu_accounting()

    # Practica 3
    def performance(self):
        print("")
        #mainMenu_performance()

    # Practica 4
    def configuration(self):
        mainMenu_configuration()


mainMenuApp()
