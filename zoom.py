import webbrowser
import os
import time
url = 'ZOOM URL HERE'
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
webbrowser.get('firefox').open(url)

time.sleep(3)
os.system("taskkill /im firefox.exe /f")
