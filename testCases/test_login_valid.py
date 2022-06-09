from selenium import webdriver
from pageObject.LoginPage import LoginPages
from utilities.readProperties import ReadConfig
from utilities.dataLog import Log_Data
from selenium.webdriver.common.by import By
# import pytest
import time


class Test_valid_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    log = Log_Data.custom_logger()

#===============================================================================
# TESTCASE 1 : Verify valid POPULIX Login Page
#===============================================================================

    def test1_loginPageTitle(self):
        self.log.info("=== Test_1_Title_Login ===")
        
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        
        get_title=self.driver.title

        if get_title=='Populix':
            assert True
            self.log.info("=== test 1_Login Page Title: PASS")
            self.driver.close()
        else:
            self.log.error("=== test 1_Login Page Title: FAIL")
            self.driver.close()
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
            assert False

#===============================================================================
# TESTCASE 2 : LOGIN using a valid email & valid password
#===============================================================================
    def test2_login_valid(self):
        self.log.info("=== Test_2_valid_Login ===")

        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPages(self.driver)
        time.sleep(1)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
     
        time.sleep(3)
        page_url = self.driver.current_url
        if page_url=='https://www.populix.co/study':
            if self.driver.find_element(By.ID, "topnav-btn-avatar").is_displayed():
                assert True
                self.log.info("=== test 2_Valid Login Test: PASS")
                self.driver.close()
        else:
            self.log.error("=== test 2_Valid Login Test: FAIL")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_valid.png")
            self.driver.close()
            assert False 

#=========================================================================================
# TESTCASE 3 : LOGIN by pressing the Enter key with a valid email and password
#=========================================================================================

    def test3_login_valid_enter_key(self):
        self.log.info("=== Test_3_valid_Login ===")

        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPages(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.enterLogin()

        time.sleep(3)
        page_url = self.driver.current_url
        if page_url=='https://www.populix.co/study':
            if self.driver.find_element(By.ID, "topnav-btn-avatar").is_displayed():
                assert True
                self.log.info("=== test 3_Valid enterLogin Test: PASS")
                self.driver.close()
        else:
            self.log.error("=== test 3_Valid enterLogin Test: FAIL")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_valid.png")
            self.driver.close()
            assert False 

#===============================================================================
# TESTCASE 4 : Verify clicking on the eye icon to show the password
#===============================================================================

    def test4_password_eye_icon(self):
        self.log.info("=== Test_4_password_eye_icon ===")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPages(self.driver)
        self.lp.setPassword(self.password)
        
        self.lp.eyePassword()
        time.sleep(2)
        self.log.info("=== test 4_password eye Test: PASS")
        self.driver.quit()

#===================================================================================================
# TESTCASE 5 : Verify user should be able to move input fields via pressing the TAB key
#===================================================================================================

    # def test5_valid_tab_key(self):
    #     self.log.info("=== Test_5_valid TAB key ===")
    #     self.driver.find_element(By.ID, "input_email").click()
    #     self.driver.find_element(By.ID, "input_email").send_keys("tito@gmail.com")
    #     self.driver.find_element(By.ID, "input_email").send_keys(Keys.TAB)
    #     self.driver.find_element(By.ID, "input_password").send_keys("bingung")
    #     self.driver.find_element(By.ID, "btn_to-forgot-password").send_keys(Keys.TAB)
    #     self.driver.find_element(By.ID, "submit_login").send_keys(Keys.TAB)
    #     self.driver.find_element(By.ID, "login_facebook").click()
    #     time.sleep(2)

    #     assert 'Facebook' in driver.find_element(By.CLASS_NAME, 'fb_logo').text
    #     log.info("=== test 5_valid TAB key Test: PASS")