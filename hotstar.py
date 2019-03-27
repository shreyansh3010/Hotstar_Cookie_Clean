import webbrowser
import os
from selenium import webdriver
from threading import Timer
def magic():
    os.system("taskkill /f /im "+"chrome.exe")
    url1 = "" #matchurl
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.get(url1)
    driver.delete_all_cookies()
    Timer(235, magic, ()).start()
magic()