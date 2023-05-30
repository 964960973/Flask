import base64
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from urllib import request
import cv2, random
import requests
import ddddocr

def text_dis(bg, fg):
    slide = ddddocr.DdddOcr(det=False, ocr=False)
    with open(bg, 'rb') as f:
        target_bytes = f.read()
    with open(fg, 'rb') as f:
        background_bytes = f.read()
    res = slide.slide_comparison(target_bytes, background_bytes)
    return res.get('target')[0]

def save_image(image_url,name):
    url = image_url

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
    }
    response = requests.get(url, headers=headers).content
    with open(f"./{name}.png", "wb") as f:
        f.write(response)
    return

def get_slide():
    options = webdriver.ChromeOptions()
    # 对于老版本的浏览器不行
    url = r'https://www.anjuke.com/captcha-verify/?history=aHR0cHM6Ly9iaW56aG91LmFuanVrZS5jb20vY29tbXVuaXR5Lz9mcm9tPWVzZl9saXN0&namespace=anjuke_xiaoqu_pc&serialID=27e90554cad254c28a0f80195369760d_7baf26a84e554a92bf932587e43d6e54&callback=shield&from=antispam'
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(3)
    info = driver.find_element(By.XPATH,'//img[@class="dvc-captcha__bgImg"]')
    targetUrl = info.get_attribute("src")
    save_image(targetUrl,"image1")
    info1 = driver.find_element(By.XPATH,'//*[@id="ISDCaptcha"]/div[1]/div/img[2]')
    tempUrl = info1.get_attribute("src")
    save_image(tempUrl,"image2")
    with open('./image1.png', 'rb') as f:
        target_bytes = f.read()
    with open('./image2.png', 'rb') as f:
        background_bytes = f.read()

    distance = text_dis('image1.png', 'image2.png')
    slide = driver.find_element(By.CLASS_NAME, 'dvc-slider__handler')
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