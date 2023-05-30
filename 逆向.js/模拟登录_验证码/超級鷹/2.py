import base64
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from urllib import request
import cv2, random

import ddddocr


def text_dis(bg, fg):
    slide = ddddocr.DdddOcr(det=False, ocr=False)
    with open(bg, 'rb') as f:
        target_bytes = f.read()
    with open(fg, 'rb') as f:
        background_bytes = f.read()
    res = slide.slide_comparison(target_bytes, background_bytes)
    return res.get('target')[0]


def get_slide():
    options = webdriver.ChromeOptions()
    # 对于老版本的浏览器不行
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get('https://www.geetest.com/demo/slide-bind.html')
    # 输入框输入账号和密码
    driver.find_element(By.ID, 'username').send_keys('13535353535')
    driver.find_element(By.ID, 'password').send_keys('123123123')
    # driver.find_element(By.ID,'btn').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div.btn').click()
    time.sleep(5)
    img_src = driver.execute_script('return document.getElementsByClassName("geetest_canvas_bg geetest_absolute")[0].toDataURL("image/png");')
    im_base64 = img_src.split(',')[1]
    im_bytes = base64.b64decode(im_base64)
    with open('./bg.png', 'wb') as f:
        f.write(im_bytes)
    temp = driver.execute_script(
        "return document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0].toDataURL('image/png');")
    temp_base64 = temp.split(',')[1]
    temp_bytes = base64.b64decode(temp_base64)
    with open('./temp.png', 'wb') as f:
        f.write(temp_bytes)

    distance = text_dis('bg.png', 'temp.png')
    # 拖动滑块
    slide = driver.find_element(By.CSS_SELECTOR, 'div.geetest_slider_button')
    action_chains = webdriver.ActionChains(driver)
    # 点击，准备拖拽
    action_chains.click_and_hold(slide)
    action_chains.pause(0.2)
    action_chains.move_by_offset(distance - 10, 0)
    action_chains.pause(0.8)
    action_chains.move_by_offset(10, 0)
    action_chains.pause(1.4)
    action_chains.move_by_offset(-10, 0)
    action_chains.release()
    action_chains.perform()
    time.sleep(20)


get_slide()

'''
2、鼠标操作
click --- 鼠标左键点击(可以指定或不指定元素对象)
click_and_hold --- 鼠标左键点击但不释放(可以指定或不指定元素对象)
release --- 释放鼠标点击动作(可以指定或不指定在目标元素对象上释放)
context_click --- 鼠标右键点击(可以指定或不指定元素对象)
double_click --- 鼠标左键双击(可以指定或不指定元素对象)
drag_and_drop --- 鼠标左键在两个元素之间拖拽
drag_and_drop_by_offset --- 鼠标左键拖拽元素到目标偏移位置
move_by_offset --- 鼠标移动指定偏移
move_to_element --- 鼠标移动到指定元素
move_to_element_with_offset --- 鼠标移动到指定元素的指定偏移位置

1、行为控制
perform --- 执行所有准备好的Action
reset_actions --- 清空所有准备好的Action　　#  该方法在 selenium 3.141.0版本不生效
pause --- 设置Action之间的动作时间间隔

'''