from info_acquisition.app.main_menu.main_menu import mainMenu_info_acquisition
from accounting.app.main_menu.main_menu import mainMenu_accounting
from main_app_designer import mainMenuDesigner


class mainMenuApp(mainMenuDesigner):

    def __init__(self):
        super().__init__()

    # Practica 1
    def info_acquisition(self):
        mainMenu_info_acquisition()

    # Practica 2
    def accounting(self):
        mainMenu_accounting()


mainMenuApp()
