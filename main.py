import subprocess
import time
import pygetwindow as gw

# Launch Everything.exe
process = subprocess.Popen(["C:\\Program Files\\Everything\\Everything.exe"])

# Process.Wait() does not ensure that the window is loaded, so we have to use sleep
time.sleep(0.25)
search_for_window = True

while search_for_window:
    # Find the window and close it
    if (gw.getWindowsWithTitle("Everything")):
        window = gw.getWindowsWithTitle("Everything")[0]
        window.close()
        search_for_window = False
