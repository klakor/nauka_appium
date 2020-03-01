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

from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.quit()

    def test_add_contact(self):
        self.driver.find_element_by_accessibility_id("Add Contact").click()
        contact_name = self.driver.find_element_by_id("com.example.android.contactmanager:id/contactNameEditText")
        contact_name.send_keys("Andrzej Nowak")
        contact_phone = self.driver.find_element_by_id("com.example.android.contactmanager:id/contactPhoneEditText")
        contact_phone.send_keys("123456789")
        #self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='android:id/text1']").select_by_value("Work")
        contact_email = self.driver.find_element_by_id("com.example.android.contactmanager:id/contactEmailEditText")
        contact_email.send_keys("andrzej.nowak@mail.com")
        touch = TouchAction(self.driver)
        touch.press(x=349, y=522).move_to(x=349, y=372).release().perform()

        self.assertEqual(contact_name.text, "Andrzej Nowak")
        self.assertEqual(contact_phone.text, "123456789")
        self.assertEqual(contact_email.text, "andrzej.nowak@mail.com")

        save = self.driver.find_elements_by_xpath("//android.widget.Button[@resource-id='com.example.android.contactmanager:id/contactSaveButton']")
        save.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)