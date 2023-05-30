from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time
# 导入超级鹰
from 超级鹰 import Chaojiying_Client
#根据系统，可能截图不成功，需要使用无头浏览，mac系统可以不设置
options=webdriver.ChromeOptions()
options.headless=True

driver=webdriver.Chrome(options)
driver.get('http://www.zhaopingou.com/signin')



driver.find_element_by_class_name('li02').click()
wait=WebDriverWait(driver,20,0.5)
# 账号登录
login_phone=wait.until(EC.visibility_of_element_located((By.ID,'pwd_login_phone')))
login_phone.send_keys('***')
# 密码
driver.find_element_by_id('form_login_password').send_keys('***')
# 点击获取图片
captcha = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="phone_login_pwd"]//iframe[starts-with(@id, "captcha_widget")]')))
captcha.click()
# 点击
# 保存图片（可以不保存）
captcha_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//body[@class="graybc"]//iframe[starts-with(@id, "captcha_frame")]')))
captcha_element.screenshot('zhaopingou.png')

# 将图片转换为二进制
bytes_img=captcha_element.screenshot_as_png
# print(bytes_img)

result=Chaojiying_Client.post_pic(bytes_img,'9101')
x,y=result['pic_str'].split(',')
print(x,y)
x=int(x)
y=int(y)
# ActionChains(driver).move_to_element_with_offset(bytes_img,x,y).click().perform()
ActionChains(driver).move_to_element_with_offset(captcha_element, x, y).click().perform()
time.sleep(2)
driver.find_element_by_id('free_login_btn').click()

print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
# time.sleep(5)
driver.quit()
