from cx_Freeze import setup, Executable 
  
setup(name = "RunMe" , 
      version = "0.1" , 
      description = "" , 
      executables = [Executable("pyServer.py")]) 