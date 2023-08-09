# clean-start-everything
[Everything](https://www.voidtools.com/) is an exceptionally fast file explorer developed by Voidtools. This script enables clean start-up execution of Everything, without displaying a window or triggering a UAC prompt.

Recommended to use with [EverythingToolbar](https://github.com/srwi/EverythingToolbar).

<br>

---

<br>

Setup:

1. Assuming Everything.exe is stored in the default directory C:\Program Files\Everything, [download](https://github.com/Eeelis/clean-start-everything/releases/download/v1.0.0/CleanStartEverything.exe) CleanStartEverything.exe. If Everything.exe is stored somewhere else, you can modify the directory in the source code, and build the program from source.
2. Disable Everything in the list of apps under Settings > Startup. If you have created scheduled tasks or shortcuts related to launching Everything, delete them.
3. Create a new task by launching the Task Scheduler, and clicking "Create Task".
4. Give the task an appropriate name.
5. Tick "Run with highest privileges"
6. Select the Triggers tab, and click New to add a new trigger.
7. Choose "At log on" and click ok.
8. Select the Actions tab, and click New to add a new action.
9. Find and select CleanStartEverything.exe by clicking Browse.
10. If you are on a laptop, untick "Start the task only if the computer is on AC power" in the Conditions tab.
11. Click OK.
12. Restart your computer. Everything should now launch without a UAC prompt and stay in the background, ready to be used with EverythingToolbar.
