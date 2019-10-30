################################ SYSTEM IMPORTS ################################
import socket
from threading import Thread


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



    def launchThreads(self):
        
        # Kill Any Server and Client running at the ports
        tcp_killer = TCPKiller()
        tcp_killer.KillPorts()

        # Launch Python Server
        Thread(target = self.launchServer).start()
        



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
                    response = str(eval(self.dataFromJavaGUI))+"\n"

                    
                    if not data:
                        break
                    
                    conn.send(response.encode())


        


if __name__ == "__main__":

    controller = Controller()
    controller.launchThreads()

