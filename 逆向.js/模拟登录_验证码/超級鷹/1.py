# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from 超级鹰 import Chaojiying_Client
from selenium.webdriver.support.ui import WebDriverWait

USERNAME = '964960973'
PASSWORD = '063599a.'
SOFTID = 938475
class XieCheng:
    def __init__(self):
        # 打开chrome浏览器
        self.d = webdriver.Chrome()
        self.chaojiying = Chaojiying_Client(USERNAME, PASSWORD,SOFTID)
        self.wait = WebDriverWait(self.d,20)
        self.action = ActionChains(self.d)  # 创建动作链对象
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.action = ActionChains(self.d)
        self.url = 'https://passport.ctrip.com/user/reg/home'
    def open_url(self):
        # 打开携程网注册页面
        self.d.get(self.url)
        # 点击同意并继续
        self.d.find_element(By.XPATH, '//div[@class="pop_footer"]/a[@class="reg_btn reg_agree"]').click()
        # 定位到滑块按钮元素
        ele_button = self.d.find_element(By.XPATH, '//*[@id="slideCode"]/div[1]/div[2]')
        # 打印滑块按钮的宽和高
        print('滑块按钮的宽：', ele_button.size['width'])
        print('滑块按钮的高：', ele_button.size['height'])
        # 定位到滑块区域元素
        ele = self.d.find_element(By.XPATH, '//div[@class="cpt-bg-bar"]')
        # 打印滑块区域的宽和高
        print('滑块区域的宽：', ele.size['width'])
        print('滑块区域的高：', ele.size['height'])
        # 按住滑块不动
        self.action.click_and_hold(ele_button).perform()
        # 拖动滑块
        self.action.drag_and_drop_by_offset(ele_button, ele.size['width'], ele.size['height']).perform()
        # action.move_by_offset(xoffset=ele.size['width'], yoffset=0).perform()


    def get_position(self):
        img_element = self.d.find_element(By.XPATH, '//*[@id="slideCode-choose"]/div[2]')
        img_element1 = self.d.find_element(By.XPATH, '//*[@id="slideCode-choose"]/div[2]')
        img_element.screenshot('img.png')
        im = open('img.png', 'rb').read()  # 以二进制的方式读取验证码
        result = self.chaojiying.PostPic(im, 9005)['pic_str']  # 9005获取验证码3-5坐标字典，并取出坐标值
        print(result)
        for index in result.split('|'):  # 以"|"进行分割，得到一个列表，并循环出每一个字的坐标
            x = index.split(',')[0]  # 得到x轴的坐标
            y = index.split(',')[1]  # 得到y轴的坐标
            print(x,y)

            self.action.move_to_element_with_offset(img_element1, int(x), int(y)).click().perform()
            # image:验证码的元素框；x：验证码的横轴；y:验证码的纵轴
        time.sleep(1)
        self.d.find_element(By.XPATH,'//*[@id="slideCode-choose"]/div[2]/div[4]/a').click()



if __name__ == '__main__':
    api = XieCheng()
    api.open_url()
    api.get_position()
