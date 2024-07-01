from appium import webdriver as app
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions import interaction

from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import math

def start_app(driver, app_package, app_activity):
    driver.start_activity(app_package, app_activity)
    
    
def close_app(driver):
    driver.press_keycode(82)
    time.sleep(1)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(571, 1145)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(567, 591)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    

def main():
    app1 = {
    "platformName": "Android",
    "appium:platformVersion": "6",
    "appium:deviceName": "d4ead8a0",
    "appium:appPackage": "com.manmanbuy.bijia",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.manmanbuy.bijia.StartActivity",
    "appium:noReset": "false",
    }

    app2 = {
        "platformName": "Android",
        "platformVersion": "6",
        "deviceName": "d4ead8a0",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "automationName": "UiAutomator2",
        "noReset": "true",
    }

    appium_server = 'http://localhost:4723/wd/hub'

    # 启动第一个应用
    driver = app.Remote(appium_server, app1)
    time.sleep(6)
    TouchAction(driver).tap(x=788,y=1534).perform()
    time.sleep(5)
    # 关闭第一个应用
    for i in range(3):
        close_app(driver)
        time.sleep(1)
    print("wait")
    driver.press_keycode(82)
    
    # 切换到第二个应用
    start_app(driver, app2["appPackage"], app2["appActivity"])
    time.sleep(10)

    # 截屏
    driver.get_screenshot_as_file('screen.png')
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(680, 1867)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    time.sleep(6)
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(214, 785)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    time.sleep(10)
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(102, 472)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    time.sleep(10)
    close_app(driver)
    close_app(driver)
    close_app(driver)

    
    
    
    driver.quit()

if __name__ == '__main__':
    for i in range(2):
        try:
            main()
        except Exception as e:
            print(e)
            continue

