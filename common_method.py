# coding = utf-8
# @Time : 2020/12/30 20:19
# @Author : 崔孟泽
# @File : common.py
# @Software: PyCharm
from appium import webdriver
def Caps():
    # 传入 desired capabilities (被测对象的基本信息)
    caps = {}
    caps['platformName'] = 'Android'
    caps['platformVersion'] = '7.1.2'
    caps['deviceName'] = '127.0.0.1:21503'
    caps['appPackage'] = 'com.seafile.seadroid2'
    caps['appActivity'] = 'com.seafile.seadroid2.ui.activity.BrowserActivity'
    caps['noReset'] = 'False'
    caps['app'] = r'D:\Desktop\软件测试\软件测试项目\App项目实战\1.SEAFILE系统环境部署\Seafile手册与app包\seafile-2.2.8.apk'
    # 处理中文问题
    caps['unicodeKeyboard'] = 'True'
    caps['resetKeyboard'] = 'True'
    # 解决安卓7.0 以上元素定位出Bug的配置项
    # caps['automationName'] = "uiautomator2"
    # 启动app
    driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
    return driver