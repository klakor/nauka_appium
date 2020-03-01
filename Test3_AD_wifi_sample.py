# -*- coding: utf-8" -*

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
        self.driver.implicitly_wait(10) # co to robi?


    def tearDown(self):
        self.driver.quit()


    def test_wifi_checkbox(self):
        el = self.driver.find_element_by_accessibility_id('Preference')
        el.click()
        el = self.driver.find_element_by_accessibility_id('3. Preference dependencies')
        el.click()
        # print(el)
        self.assertIsNotNone(el)
        #
        # #Jesli chcemy zaznaczyc wszystkie checkboxy
        #
        # elements= self.driver.find_elements_by_android_uiautomator("new UiSelector().checkable(true)")
        # amount_of_elements=len(elements)
        #
        # for elem in elements:
        #     elem.click()




        # Od kroku 3

        elements= self.driver.find_elements_by_android_uiautomator("new UiSelector().checkable(true)")
        amount_of_elements=len(elements)

        print("Checkboxow jest:"+amount_of_elements.__str__()) # pomocniczo

        if amount_of_elements>=1:
            print("Jest conajmniej jeden checkbox")

            self.driver.find_element_by_id('android:id/checkbox').click()

            # jak kliknac na drugi index
            self.driver.find_elements_by_xpath("//android.widget.RelativeLayout")[1].click()

            # alternatywne rozwiazanie dla 45 linii ale gorzej
            #self.driver.find_element_by_xpath('//android.widget.TextView[@text="WiFi settings]').click()

            self.driver.find_element_by_class_name("android.widget.EditText").send_keys("12334")

            self.driver.find_elements_by_class_name("android.widget.Button")[1].click()

            self.driver.keyevent(4) # dla przycisku androidowego BACk
            self.driver.back()

        # Od kroku 3 - alternatywne rozwiazenie

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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)