import os
from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
toaster.show_toast("Vaccine", "Injecting Essential Oils...", threaded=True, icon_path=None, duration=4)
os.system("taskkill /f /im  pyw.exe")

while toaster.notification_active():
	time.sleep(0.1)
	
toaster.show_toast("Vaccine", "5G Towers disabled.", threaded=True, icon_path=None, duration=4)