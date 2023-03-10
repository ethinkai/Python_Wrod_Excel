from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fileutils import my_GetData
#driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path=r'D:\Python\Python38\chromedriver.exe')
#防止打印一些无用的错误
#option = webdriver.ChromeOptions()
#option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
#driver = webdriver.Chrome(chrome_options=option)
#关闭ssl检查
v_option = Options()
v_option.add_argument('--ignore-certificate-errors')
#关闭无用日志
v_option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

v_service = Service(r'D:\Python\Python38\chromedriver.exe')     #驱动所在位置
#driver放在函数内会导致页面闪退，需设置为全局变量
#global v_driver

v_driver = webdriver.Chrome(service=v_service, options=v_option)
v_driver.implicitly_wait(60)    #每个步骤最大等待时间60秒
#获取登录参数
v_str1 = 'h'
v_str2 = 'shijian'
v_list = my_GetData(v_str1, v_str2)
v_driver.get(v_list[0])
#定位方式
#ID
#v_driver.find_element(By.ID,'kw').send_keys('selenium')
#Name
#v_driver.find_element(By.NAME, "wd").send_keys("selenium")
#TagName
#driver.find_element_by_tag_name("input").send_keys("selenium")
#className
#driver.find_element_by_class_name("s_ipt").send_keys("selenium")
#CSS
#driver.find_element_by_css_selector("#kw").send_keys("selenium")

#XPath  获取xpath：右击鼠标-检查，定位到元素，在弹出的elements选中的地方鼠标右击-copy-copyxpath
#click模拟点击
v_driver.find_element(By.XPATH, "//*[@id='userNameId']").send_keys(v_list[1])
v_driver.find_element(By.XPATH, "//*[@id='pwdId']").send_keys(v_list[2])

v_driver.find_element(By.XPATH, "//*[@id='btn_submit']").click()
#driver.find_element_by_id("su").click()
#time.sleep(3)
#关闭并清理浏览器，close()仅关闭
#v_driver.quit()
