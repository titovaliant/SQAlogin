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
        self.log.info("=== Test_1_valid_Title_Login ===")
        
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        
        get_title=self.driver.title

        if get_title=='Populix':
            assert True
            self.log.info("=== test 1_Login Page Title: PASS")
        else:
            self.log.error("=== test 1_Login Page Title: FAIL")
            self.driver.save_screenshot(".\\Screenshots\\" + "test 1_loginTitle.png")
            assert False
        self.driver.quit()

#===============================================================================
# TESTCASE 2 : LOGIN using a valid email & valid password
#===============================================================================
    def test2_login_valid(self):
        self.log.info("=== Test_2_valid_Login ===")

        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPages(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
     
        time.sleep(5)
        page_url = self.driver.current_url
        if page_url=='https://www.populix.co/study':
            if self.driver.find_element(By.CLASS_NAME, "sidebar-img-profile").is_displayed():
                assert True
                self.log.info("=== test 2_Valid Login Test: PASS")
        else:
            self.log.error("=== test 2_Valid Login Test: FAIL")
            self.driver.save_screenshot(".\\Screenshots\\" + "test 2_login_valid.png")
            assert False 
        self.driver.quit()

#===============================================================================
# TESTCASE 3 : Verify clicking on the eye icon to show the password
#===============================================================================

    def test3_password_eye_icon(self):
        self.log.info("=== Test_3_valid_password_eye_icon ===")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPages(self.driver)
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        
        self.lp.eyePassword()
        time.sleep(2)
        self.log.info("=== test 3_password eye Test: PASS")
        self.driver.quit()

#=========================================================================================
# TESTCASE 4 : LOGIN by pressing the Enter key with a valid email and password
#=========================================================================================

    def test4_login_valid_enter_key(self):
        self.log.info("=== Test_4_valid_Login_EnterKey ===")

        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPages(self.driver)
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.enterLogin()

        time.sleep(5)
        page_url = self.driver.current_url
        if page_url=='https://www.populix.co/study':
            if self.driver.find_element(By.CLASS_NAME, "sidebar-img-profile").is_displayed():
                assert True
                self.log.info("=== Test_4_valid_Login_EnterKey: PASS")
        else:
            self.log.error("=== Test_4_valid_Login_EnterKey: FAIL")
            self.driver.save_screenshot(".\\Screenshots\\" + "test 4_login_valid Enter.png")
            assert False 
        self.driver.quit()    

#===================================================================================================
# TESTCASE 5 : Verify user should be able to move input fields via pressing the TAB key
#===================================================================================================

    def test5_valid_tab_key(self):
        self.log.info("=== Test_5_valid TAB key ===")
        
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPages(self.driver)

        self.lp.TABkey(self,username,password)
        self.lp.clickFBLogin()
        time.sleep(2)

        check = self.driver.find_element(By.CLASS_NAME, 'fb_logo').text
        if check=='Facebook':
            assert True
            self.log.info("=== Test_5_valid TAB key Test: PASS")
        else:
            self.log.error("=== Test_5_valid TAB key Test: PASS")
            self.driver.save_screenshot(".\\Screenshots\\" + "test 5_login_valid TAB.png")
            assert False 
        self.driver.quit()    