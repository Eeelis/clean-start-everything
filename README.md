# clean-start-everything
[Everything](https://www.voidtools.com/) is an exceptionally fast file explorer developed by Voidtools. This script enables clean start-up execution of Everything, without displaying a window or triggering a UAC prompt.

Recommended to use with [EverythingToolbar](https://github.com/srwi/EverythingToolbar).

<br>

---

<br>

Setup:

1. Assuming Everything.exe is stored in the default directory C:\Program Files\Everything, [download](https://github.com/Eeelis/clean-start-everything/releases/download/v1.0.0/CleanStartEverything.exe) CleanStartEverything.exe. If Everything.exe is stored somewhere else, you can modify the path in the source code accordingly, and build the program from source.
2. Disable Everything in the list of apps under Settings > Startup. If you have created scheduled tasks or shortcuts related to launching Everything, delete them.
3. Press Win + R, type in taskschd.msc in the run dialog box, and click OK. 
4. Create a new task by clicking "Create Task" in the Task Manager.
5. Give the task an appropriate name and tick "Run with highest privileges".
7. Select the Triggers tab, and click New to add a new trigger.
8. Choose "At log on" and click OK.
9. Select the Actions tab, and click New to add a new action.
10. Find and select CleanStartEverything.exe by clicking Browse.
11. If you are on a laptop, untick "Start the task only if the computer is on AC power" in the Conditions tab.
12. Click OK.
13. Restart your computer. Everything should now launch without a UAC prompt and stay in the background, ready to be used with EverythingToolbar.
