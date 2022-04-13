import time
import webbrowser
import os
import threading

def start_browser():
    path = os.getcwd().replace("\\", "/")
    path += "../ext/dist"
    print()
    
    print("starting browser")
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe --load-extension="D:\dist" %s'
    webbrowser.get(chrome_path).open('http://docs.python.org/')

print(time.asctime(time.localtime(time.time())))
t = threading.Thread(target=start_browser)
t.start()

time.sleep(30)
os.system("taskkill /im chrome.exe /f")
print(time.asctime(time.localtime(time.time())))




