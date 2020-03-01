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

        is_checked_bool = False
        is_checked_value = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")

        if is_checked_value == "false":
            print("Checkbox nie jest zaznaczony")
            self.driver.find_element_by_class_name("android.widget.CheckBox").click()
            is_checked_bool = True

        self.assertTrue(is_checked_bool)
        sleep(3)

        self.driver.back()
        self.driver.find_element_by_accessibility_id('3. Preference dependencies').click()

        # czy checkbox jest zaznaczony ? jesli tak to nie zaznaczaj i daj wynik testu; OK ????
        is_checked_value = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")

        if is_checked_value == "true":
            print("Checkbox jest zaznaczony")
            is_checked_bool = True


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)