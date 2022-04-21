
import os
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
if (not os.path.exists(chrome_path)):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
chrome_path += ' %s'

print(chrome_path)
webbrowser.get(chrome_path).open('https://www.baidu.com/')