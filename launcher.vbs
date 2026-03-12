Set WshShell = CreateObject("WScript.Shell")

' Start the server completely silently in the background (0 = hidden)
' We redirect stdout and stderr to server.log to prevent [Errno 22] Invalid argument 
' when python or C++ libraries try to write to a non-existent console.
WshShell.Run "cmd /c cd /d D:\agri && python -m uvicorn backend.app:app --host 127.0.0.1 --port 8001 > server.log 2>&1", 0, False

' Give the server a few seconds to initialize
WScript.Sleep 3000

' Open the Chrome web application smoothly
chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
WshShell.Run """" & chromePath & """ --app=http://127.0.0.1:8001 --start-maximized", 1, False
