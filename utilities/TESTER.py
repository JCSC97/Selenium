from xvfbwrapper import Xvfb
from selenium import webdriver
from utilities.InicioSesion import SingUp

import time
SU = SingUp
vdisplay = Xvfb()
vdisplay.start()
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://www.google.com.mx")
print("SI llega")
time.sleep(3)
SU.takescreenshot(driver, namescren="Al", directory="ScreenshotsPruebaLogin/")

vdisplay.stop()
driver.close()




















