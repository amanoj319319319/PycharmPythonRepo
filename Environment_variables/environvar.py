'''
import os

for a,b in os.environ.items():
    print ("%s = %s" %(a,b))

print("**************************")
print (os)
'''

import unittest
from selenium import webdriver
import requests


class SeleniumCBT(unittest.TestCase):
    def setUp(self):
        self.username = "user@email.com"
        self.authkey = "12345"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username, self.authkey)
        self.test_result = None

        caps = {}
        caps['browserName'] = 'Chrome'
        caps['version'] = '60x64'
        caps['platform'] = 'Windows 10'
        caps['screenResolution'] = '1366x768'
        caps['record_video'] = 'true'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (self.username, self.authkey)
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):
        self.driver.get('http://crossbrowsertesting.github.io/selenium_example_page.html')
        self.assertEqual("Selenium Test Example Page", self.driver.title)
        self.test_result = 'pass'
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()