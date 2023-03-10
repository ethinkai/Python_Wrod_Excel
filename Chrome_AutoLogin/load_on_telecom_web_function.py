from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fileutils import my_GetData
import ddddocr
def my_OpenUrl(v_str1, v_str2):
    #设置为全局变量，否则网页会闪退
    global v_driver
    #关闭ssl检查
    v_option = Options()
    v_option.add_argument('--ignore-certificate-errors')
    #关闭无用日志
    v_option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    v_service = Service(r'D:\Python\Python38\chromedriver.exe')     #驱动所在位置
    v_driver = webdriver.Chrome(service=v_service, options=v_option)
    v_driver.implicitly_wait(60)    #每个步骤最大等待时间60秒
    #获取登录参数
    #v_str1 = 'h'
    #v_str2 = 'shijian'
    v_list = my_GetData(v_str1, v_str2)
    #判断是否打开url
    if(v_list == '1'):
        print ("参数错误！错误码：" + v_list)
        v_driver.quit()
        return
    #2022-11-8新增安全资源池
    check_str = v_list[0]
    if("8:" in check_str or "10:" in check_str):
        v_driver.get(check_str)
        v_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/table/tbody/tr/td/div[2]/form/div[1]/div[1]/div/input").send_keys(v_list[1])
        v_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/table/tbody/tr/td/div[2]/form/div[1]/div[2]/div/input").send_keys(v_list[2])
        #获取验证码图片
        img_element = v_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/table/tbody/tr/td/div[2]/form/div[1]/div[3]/div/div")
        img_element.screenshot('./captcha.jpg')
        #解析验证码图片
        ocr = ddddocr.DdddOcr()
        with open('./captcha.jpg', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        #将识别结果res填入
        v_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/table/tbody/tr/td/div[2]/form/div[1]/div[3]/div/input").send_keys(res)
        #页面加载较慢，等待3秒
        time.sleep(3)
      #  v_driver.find_element(By.CLASS_NAME, "uedc-ppkg-login_product-submit").click()
        v_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[3]/table/tbody/tr/td/div[2]/form/button").click()
        return
    #其他正常登录政务云
    v_driver.get(check_str)
    #XPath  获取xpath：右击鼠标-检查，定位到元素，在弹出的elements选中的地方鼠标右击-copy-copyxpath
    #click模拟点击
    v_driver.find_element(By.XPATH, "//*[@id='userNameId']").send_keys(v_list[1])
    v_driver.find_element(By.XPATH, "//*[@id='pwdId']").send_keys(v_list[2])
    #    print(v_list[2])
    v_driver.find_element(By.XPATH, "//*[@id='btn_submit']").click()
    #time.sleep(3)
    #关闭并清理浏览器，close()仅关闭
    #v_driver.quit()
