# -*- coding: utf-8 -*-

from appium import webdriver

# 使用正则表达式筛选设备 id
import re

# 使用time.sleep(xx)函数进行等待
import time

# 使用 os 模块调用命令
import os

# 记录日志
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s", datefmt="%m/%d/%Y %H:%M:%S")

# 测试的包的路径和包名
appLocation = "/Users/mofei/Downloads/ucss/MSG/55/SGAgent_Android_3.1.0_55.apk"



# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())

# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
logging.info("设备ID是：" + deviceId)
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]

# 读取 APK 的 package 信息
appPackageAdb = list(os.popen('aapt dump badging ' + appLocation ).readlines())
appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]
logging.info("应用安装包是：" + appPackage)


'''
目前只支持华为手机客户端登录 - 2019-5-13
'''

# 删除以前的安装包
os.system('adb uninstall ' + appPackage)
'''
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = deviceVersion
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.skyguard.mobile.agent'
desired_caps['appActivity'] = 'com.skyguard.mobile.ui.SGLoginActivity'

'''
desired_caps = {
    'platformName': 'Android',
    'platformVersion': deviceVersion,
    'deviceName': deviceId,
    'appPackage': appPackage,
    'app': appLocation,
    'appActivity': "com.skyguard.mobile.ui.SGLoginActivity",
}

command_executor = "http://localhost:4723/wd/hub"
try:
    driver = webdriver.Remote(command_executor, desired_caps)
    logging.info("成功连接Appium Server： "+ command_executor)
except:
    logging.info("连接Appium："+command_executor+"失败")

# time.sleep(10)

logon_name = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/TextInputLayout[1]/android.widget.FrameLayout/android.widget.EditText")
logon_name.click()
logon_name.send_keys("murphy" + "\n")
# driver.hide_keyboard()


login_pwd = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/TextInputLayout[2]/android.widget.FrameLayout/android.widget.EditText")
login_pwd.click()
login_pwd.send_keys("*******"+"\n")
# login_pwd.send_keys()
# driver.hide_keyboard() # Keyboard has no UI; no closing necessary


login_button = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button")
login_button.click()

# handle popup dialog/window
'''
# https://discuss.appium.io/t/android-not-able-to-identify-popup-dialog-window/10125

# https://discuss.appium.io/t/handling-popups-in-native-app/9626/7
# by_android_uiautomator -> new UiSelector()
'''

driver.find_elements_by_android_uiautomator('new UiSelector().description("确定")')
vpn_click = driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
logging.info("VPN的对话框包含如下内容：")
for click_content in vpn_click:
    logging.info(click_content)
logging.info("选择[1]才是确定")
vpn_click[1].click() #1才是确定



time.sleep(20) # 确保出现下一步界面
allow_install_app = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch")
allow_install_app.click()


back_view1 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"向上导航\"]/android.widget.ImageView")
back_view1.click()

allow_install_other = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Switch")
allow_install_other.click()


back_view2 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"向上导航\"]/android.widget.ImageView")
back_view2.click()

client_info_click_view = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.LinearLayout[3]").click()

click_update=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[2]")
click_update.click()
logging.info('第1次点击立即更新')

for click_times in range(1, 3):
    time.sleep(10)
    click_update.click()
    logging.info('第'+str(click_times+1)+'次点击立即更新')



driver.quit()