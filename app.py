from time import sleep
from selenium import webdriver
from secrets import usr, pw

class instagram_bot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("http://instagram.com")
        sleep(2)
        self.driver.find_element_by_css_selector("input[name='username']")\
            .send_keys(username)
        self.driver.find_element_by_css_selector("input[name='password']")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

instagram_bot(usr,pw)