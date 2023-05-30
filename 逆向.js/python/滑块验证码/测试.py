from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time

#步骤一:点击按钮，弹出没有缺口的图片

#步骤二：获取步骤一的图片

#步骤三：点击滑动按钮，弹出带缺口的图片

#步骤四：获取带缺口的图片

#步骤五：对比两张图片的所有RBG像素点，得到不一样像素点的x值，即要移动的距离

#步骤六：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹

#步骤七：按照轨迹拖动，完全验证

#步骤八：完成登录
def get_snap():
    '''
    对整个网页截图，保存成图片，然后用PIL.Image拿到图片对象
    :return: 图片对象
    '''
    driver.save_screenshot('snap.png')
    page_snap_obj=Image.open('snap.png')
    return page_snap_obj

def get_image():
    '''
    从网页的网站截图中，截取验证码图片
    :return: 验证码图片
    '''
    img=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
    time.sleep(2) #保证图片刷新出来
    localtion=img.location
    size=img.size

    top=localtion['y']
    bottom=localtion['y']+size['height']
    left=localtion['x']
    right=localtion['x']+size['width']

    page_snap_obj=get_snap()
    crop_imag_obj=page_snap_obj.crop((left,top,right,bottom))
    return crop_imag_obj


def get_distance(image1,image2):
    '''
    拿到滑动验证码需要移动的距离
    :param image1:没有缺口的图片对象
    :param image2:带缺口的图片对象
    :return:需要移动的距离
    '''
    threshold=60
    left=57
    for i in range(left,image1.size[0]):
        for j in range(image1.size[1]):
            rgb1=image1.load()[i,j]
            rgb2=image2.load()[i,j]
            res1=abs(rgb1[0]-rgb2[0])
            res2=abs(rgb1[1]-rgb2[1])
            res3=abs(rgb1[2]-rgb2[2])
            if not (res1 < threshold and res2 < threshold and res3 < threshold):
                return i-7 #经过测试，误差为大概为7
    return i-7 #经过测试，误差为大概为7


def get_tracks(distance):
    '''
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+½at²
    ③v²-v0²=2as

    :param distance: 需要移动的距离
    :return: 存放每0.3秒移动的距离
    '''
    #初速度
    v=0
    #单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t=0.3
    #位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks=[]
    #当前的位移
    current=0
    #到达mid值开始减速
    mid=distance*4/5

    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a= 2
        else:
            a=-3

        #初速度
        v0=v
        #0.2秒时间内的位移
        s=v0*t+0.5*a*(t**2)
        #当前的位置
        current+=s
        #添加到轨迹列表
        tracks.append(round(s))
        #速度已经达到v,该速度作为下次的初速度
        v=v0+a*t
    return tracks


try:

    chrome_options = webdriver.ChromeOptions()
    chrome_driver = r"./chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
    driver.get('https://account.geetest.com/login')
    wait=WebDriverWait(driver,10)

    #步骤一：先点击按钮，弹出没有缺口的图片
    b = driver.find_element(By.XPATH,'//*[@id="captchaIdLogin"]/div/div[1]/div[1]').click()
    # button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_radar_tip')))
    # button.click()

    #步骤二：拿到没有缺口的图片
    image1=get_image()

    #步骤三：点击拖动按钮，弹出有缺口的图片
    button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_slider_button')))
    button.click()

    #步骤四：拿到有缺口的图片
    image2=get_image()

    # print(image1,image1.size)
    # print(image2,image2.size)

    #步骤五：对比两张图片的所有RBG像素点，得到不一样像素点的x值，即要移动的距离
    distance=get_distance(image1,image2)

    #步骤六：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹
    tracks=get_tracks(distance)
    print(tracks)
    print(image1.size)
    print(distance,sum(tracks))


    #步骤七：按照轨迹拖动，完全验证
    button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_slider_button')))
    ActionChains(driver).click_and_hold(button).perform()
    for track in tracks:
        ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
    else:
        ActionChains(driver).move_by_offset(xoffset=3,yoffset=0).perform() #先移过一点
        ActionChains(driver).move_by_offset(xoffset=-3,yoffset=0).perform() #再退回来，是不是更像人了

    time.sleep(0.5) #0.5秒后释放鼠标
    ActionChains(driver).release().perform()


    #步骤八：完成登录
    input_email=driver.find_element(By.XPATH,'//*[@id="inputId_1670487361599_0"]')
    # input_email=driver.find_element_by_id('email')
    # input_password=driver.find_element_by_id('password')
    input_password=driver.find_element(By.XPATH,'//*[@id="inputId_1670487361599_1"]')
    button=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'login-btn')))

    input_email.send_keys('18611453110@163.com')
    input_password.send_keys('linhaifeng123')
    # button.send_keys(Keys.ENTER)
    button.click()

    import time
    time.sleep(200)
finally:
    driver.close()