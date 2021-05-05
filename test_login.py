# coding = utf-8
# @Time : 2020/12/31 22:35
# @Author : 崔孟泽
# @File : test_login.py
# @Software: PyCharm
from common_method import Caps
from common_constant import URL,USERNAME,PASSWORD
from selenium.webdriver.common.by import By
def test_login():
    # 调用封装公共方法(作用：传入Capabilities信息；驱动启动app；返回driver）
    dr = Caps()
    # 隐式等待(最多等待5秒)
    dr.implicitly_wait(5)
    # 点击‘添加账户’
    addBtn = dr.find_element(By.ID,'com.seafile.seadroid2:id/account_footer_btn')
    addBtn.click()
    # 点击'其他Seafile服务器'
    others = dr.find_elements(By.ID,'android:id/text1')[2]
    others.click()
    # 输入'云盘网址'
    svr = dr.find_element(By.ID,'com.seafile.seadroid2:id/server_url')
    svr.send_keys(URL)
    # 输入'用户名'
    usr = dr.find_element(By.ID,'com.seafile.seadroid2:id/email_address')
    usr.send_keys(USERNAME)
    # 输入'密码'
    pwd= dr.find_element(By.ID,'com.seafile.seadroid2:id/password')
    pwd.send_keys(PASSWORD)
    # 点击‘登录’
    loginBtn= dr.find_element(By.ID,'com.seafile.seadroid2:id/login_button')
    loginBtn.click()
    # 检测是否显示我的个人资料库，判断登录是否成功
    try:
        my=dr.find_element_by_android_uiautomator('text("崔孟泽的资料库")')
        my.click()
    except:
        print(USERNAME,'你好，本次测试登录失败！')
        return False
    else:
        print(USERNAME,'你好，本次测试登录成功！')
        return True
# 自测程序
if __name__=='__main__':
    test_login()