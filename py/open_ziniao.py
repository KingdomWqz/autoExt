import os
import subprocess

def runPS(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

result = runPS("Get-StartApps 'SuperBrowser'")
os.system(str(result.stdout).split("\\r\\n")[3].split(" ")[1])


