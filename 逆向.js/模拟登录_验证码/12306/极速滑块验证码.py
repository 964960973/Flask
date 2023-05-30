import json
from openpyxl import load_workbook
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import base64
import requests
import cv2
import threading
from lxml import etree
from selenium import webdriver
import redis
# chrome_driver = r"./chromedriver.exe"

option = Options()
options = webdriver.ChromeOptions()

# """为了实现更好的隐藏效果，可以继续加入两个实验选项"""
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"./chromedriver.exe")
driver.maximize_window()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

# 添加隐释等待，加强脚本稳定性
driver.implicitly_wait(5)
driver.get(f'https://kyfw.12306.cn/otn/resources/login.html')  # 打开网址.

a = driver.page_source
# driver = webdriver.Chrome(options=option, executable_path=chrome_driver)
# driver.find_element(By.XPATH, '//*[@id="J-btn-login"]').click()
# 账号框
user_name = driver.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('0000000')
# 密码框
pass_word = driver.find_element(By.XPATH, '//*[@id="J-password"]').send_keys('000')
# 点击登录
driver.find_element(By.XPATH,'//*[@id="J-login"]').click()

#匹配出滑块的位置
huak = driver.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')

# 导入ActionChains对象
action = ActionChains(driver)
# 点击并按住滑块
action.click_and_hold(huak)
# x轴为400，y轴不变为0,轴位置可通过截图获取
action.move_by_offset(400,0)
# 松开鼠标
action.release()
#让action生效
action.perform()


time.sleep(5)
driver.close()









