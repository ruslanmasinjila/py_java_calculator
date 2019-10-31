set mypath=%cd%

start %mypath%\build\exe.win-amd64-3.7\pyServer.exe

SLEEP 3

java -jar %mypath%\JAVA_GUI\dist\JAVA_GUI.jar
