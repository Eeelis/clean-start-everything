import subprocess
import time
import pygetwindow as gw

# Launch Everything.exe
process = subprocess.Popen(["C:\\Program Files\\Everything\\Everything.exe"])

# Process.Wait() does not ensure that the window is loaded, so we have to use sleep
time.sleep(0.5)
search_for_window = True

while search_for_window:
    # Find the window and close it
    window = gw.getWindowsWithTitle("Everything")
    if (window and window[0]):
        window[0].close()
        search_for_window = False
    
