
from configuration.app.main_menu.main_menu_designer import mainMenuDesigner
from configuration.app.device.download_config_device.DownloadConfigDevice import DownloadConfigDevice
from configuration.app.device.load_config_device.loadConfigDevice import LoadConfigDevice
from configuration.app.device.config_file_device.configFileDevice import ConfigFileDevice


class mainMenu_configuration(mainMenuDesigner):
    
    def __init__(self):
        super().__init__()

    def download_config_device(self):
        DownloadConfigDevice()

    def load_config_device(self):
        LoadConfigDevice()

    def create_config_device(self):
        ConfigFileDevice()
