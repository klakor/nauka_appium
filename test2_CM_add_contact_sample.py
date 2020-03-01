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
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        # nowe ustawienia dla klawiatury
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()


    # funcje testujace:
    def test_is_app_contact_manager_installed(self):
        self.assertTrue(self.driver.is_app_installed('com.example.android.contactmanager'))

    def test_contact_form(self):
        self.driver.find_element_by_accessibility_id('Add Contact').click()
        sleep(2)
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")

        textfields[0].send_keys("Tomasz")
        textfields[1].send_keys("555666999")
        textfields[2].send_keys("tomasz@wsb.pl")
        sleep(1)

        self.assertEqual(textfields[0].text, "Tomasz")
        self.assertEqual(textfields[1].text, "555666999")
        self.assertEqual(textfields[2].text, "tomasz@wsb.pl")

        print("Liczba elementow znalezionych elementow o takiej klasie:")
        print(textfields.__len__().__str__())

       # self.assertEqual(textfields.__len__().__str__(), 3)
        #Dydaktyczne printy
        print("Porownanie co jest w wyszukanych elementach")
        print(textfields[0])
        print(textfields[0].text)

        self.driver.find_element_by_class_name("android.widget.Button").click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)