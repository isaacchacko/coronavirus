import os
import monitor
import threading

x = threading.Thread(target = monitor.main)
x.start()
x.join()
os.startfile('C:\\Users\\isaac\\Desktop\\desktop python 4-27-20\\coronavirus.xlsx')