from configuration.app.device.device_File_form_designer import deviceFileFormDesigner
from telnetlib import Telnet
import time


class ConfigFileDevice(deviceFileFormDesigner):

    def __init__(self):
        super().__init__()


    def create_config(self):

        command = self.command.get(1.0,"end-1c").split("\n")
        
        #Se conecta por telnet
        self.use_telnet(command)


    def use_telnet(self, command):
        user = 'rcp'
        password = 'rcp'

        try:

            with Telnet(self.IP.get(), 23) as tn:
                tn.read_until(b'User: ', float(3))
                print(tn.read_eager().decode('ascii'))
                print(tn.read_eager().decode('ascii'))
                tn.write(user.encode("ascii") + b'\n')
                time.sleep(3)                 #10
                print(tn.read_eager().decode('ascii'))
                tn.read_until(b'Password: ', float(10))
                tn.write(password.encode("ascii") + b'\n')
                print(tn.read_eager().decode('ascii'))
                time.sleep(3)                 #10
                print(tn.read_eager().decode('ascii'))
                tn.write(b'en\n')
                time.sleep(3)                  #10
                print(tn.read_eager().decode('ascii'))
                tn.write(b'config\n')
                time.sleep(5)                 #15
                print(tn.read_eager().decode('ascii'))

                for comm in command:
                    tn.write(comm.encode("ascii") + b'\n')
                    time.sleep(3)            #13
                    print(tn.read_eager().decode('ascii'))

                tn.write(b'exit\n')
                time.sleep(3)              #15
                print(tn.read_eager().decode('ascii'))
                tn.write(b'exit\n')
                time.sleep(3)               #15
                print(tn.read_eager().decode('ascii'))

                print(tn.read_all().decode('ascii'))
                tn.close()
        except Exception as e:
            print(e)

