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
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_is_app2_installed(self):
        self.assertTrue(self.driver.is_app_installed('com.example.android.contactmanager'))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)