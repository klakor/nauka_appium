# -*- coding: utf-8" -*

# Zalozenia:
# - aplikacje sa w folderze z projektem
# - adb devices - ok
# - adb server wlaczony
# - appium wlaczone

import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_wifi_pass(self):
        global suite
        self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Preference']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='3. Preference dependencies']").click()

        elements = self.driver.find_elements_by_android_uiautomator("new UiSelector().checkable(true)")
        amount_of_elements = len(elements)

        if amount_of_elements>=1:
            print("Co najmniej jeden checkbox obecny")

            self.driver.find_element_by_xpath("//android.widget.CheckBox[@resource-id='android:id/checkbox']").click()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='WiFi settings']").click()
            self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='android:id/edit']").send_keys("1234")
            self.driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
            self.driver.keyevent(4)
            self.driver.back()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)