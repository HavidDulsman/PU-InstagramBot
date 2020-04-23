from time import sleep
from selenium import webdriver
from secrets import usr, pw, text

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
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button")\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button")\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button")\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[4]/div[3]/button")\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[5]/div[3]/button")\
            .click()
        top_ten = ["instagram", "cristiano", "arianagrande","therock", "selenagomez","kyliejenner","kimkardashian","leomessi","beyonce","neymarjr"]
        for i in top_ten:
            self.driver.get("http://instagram.com/" + i)
            sleep(1)
            # self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")\
            #     .click()
            self.driver.find_element_by_class_name('eLAPa')\
                .click()
            sleep(1)
            for i in range(2):
                self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")\
                    .click()
                sleep(2)
                self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")\
                    .click()
                sleep(2)
            
bot = instagram_bot(usr,pw)