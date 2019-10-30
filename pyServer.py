################################ SYSTEM IMPORTS ################################
import socket
from threading import Thread
import os
import time
import subprocess


################################ CUSTOM IMPORTS ################################
from tcp_killer import TCPKiller


class Controller():

    
    def __init__(self):

        # Local Host for TCP Communications
        self.HOST = '127.0.0.1'

        # Port for receiving data from Java GUI
        self.fromJavaGUIPort = 65431
    

        # Data  From Java GUI (string)
        self.dataFromJavaGUI = ""
        
        # Location for Java GUI launcher   
        self.GUI = os.path.join(os.getcwd(),"JAVA_GUI\dist\JAVA_GUI.jar")



    def launchThreads(self):
        
        # Kill Any Server and Client running at the ports
        tcp_killer = TCPKiller()
        tcp_killer.KillPorts()

        # Launch Python Server
        Thread(target = self.launchServer).start()
        
        time.sleep(5)
        subprocess.Popen(['java', '-jar', self.GUI], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        



    def launchServer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Server Listening to port:", self.fromJavaGUIPort)
            s.bind((self.HOST, self.fromJavaGUIPort))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print("Java GUI has Connected to Python Server")
                while True:
                    try:
                        data = conn.recv(65536)
                        self.dataFromJavaGUI = data.decode('utf-8')
                    except:
                        print("Java GUI closed unexpectedly...")
                        break
                    # Process the data here
                    try:
                        response = str(eval(self.dataFromJavaGUI))+"\n"
                        conn.send(response.encode())
                    except:
                        response = b"incorrect_input\n"
                        conn.send(response)

                    
                    if not data:
                        break
                    
                    


        
if __name__ == "__main__":

    controller = Controller()
    controller.launchThreads()

