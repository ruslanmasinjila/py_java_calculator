################################ SYSTEM IMPORTS ################################
from psutil import process_iter
from signal import SIGTERM # or SIGKILL
import time

################################ CUSTOM IMPORTS ################################


class TCPKiller():
    
    def __init__(self):
        pass
    
    def KillPorts(self):

        fromJavaGUIPort = 65431
        allPorts = [fromJavaGUIPort]
        
        for proc in process_iter():
            for conns in proc.connections(kind='inet'):
                for i in allPorts:
                    if conns.laddr.port == i:
                        try:
                            proc.send_signal(SIGTERM) # or SIGKILL
                        except:
                            pass
                        continue 
        time.sleep(1)
        print("Ports killed successfully")
                    
if __name__ == "__main__":
    tcp_killer=TCPKiller()
    tcp_killer.KillPorts()