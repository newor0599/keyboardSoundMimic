from infi.systray import SysTrayIcon
import os
 
def after_click(systray):
    os.system("start ui.py")

menu_options = (("Configure", None, after_click),)
systray = SysTrayIcon("icon3.png", "Configure", menu_options)
systray.start()