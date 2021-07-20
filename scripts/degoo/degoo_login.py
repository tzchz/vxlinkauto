 #-*-coding:utf-8-*-

from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

import importlib,sys
importlib.reload(sys)

class Degoo:  

  def __init__(self, DG_USER, DG_PASS):
    self.DG_USER = DG_USER
    self.DG_PASS = DG_PASS
    self.url = "https://www.vx.link/?tmpui_page=/signin.html"

  def login_degoo(self):

    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')

    driver = webdriver.Firefox(executable_path='geckodriver', options=options)
    try:
        driver.get(self.url)
    except:
        pass
    time.sleep(8)
    
    driver.set_window_size(1920,1080)
    time.sleep(3)

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    uname_box = driver.find_element_by_xpath("//input[@id='username']")
    pass_box = driver.find_element_by_xpath("//input[@id='password']")
    uname_box.send_keys(self.DG_USER)
    pass_box.send_keys(self.DG_PASS)

    login_btn = driver.find_element_by_xpath("//button[@id='submit']")
    login_btn.click()

    time.sleep(10)

    freea_btn = driver.find_element_by_xpath("//span[@class='btn-radius btn btn-danger']")
    freea_btn.click()
    
    time.sleep(5)

    freeb_btn = driver.find_element_by_xpath("//button[@onclick='vxHome.giftRequest()']")
    freeb_btn.click()

    time.sleep(5)
    
    alert = driver.switch_to.alert()
    print(alert.text)
    alert.accept()
    
    time.sleep(5)

    print(u'Success')
    driver.implicitly_wait(30)

    
    driver.close()
    
