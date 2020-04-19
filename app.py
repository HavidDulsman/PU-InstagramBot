from selenium import webdriver
from secrets import usr, pw

class instagram_bot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("http://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()

instagram_bot(usr,pw)