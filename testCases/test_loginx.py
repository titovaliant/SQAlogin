from selenium import webdriver
from pageObject.LoginPage import LoginPages
from utilities.readProperties import ReadConfig
from utilities.dataLog import Log_Data
import pytest
import time


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    log = Log_Data.custom_logger()

    def test_loginPageTitle(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        
        get_title=self.driver.title
        
        if get_title=='Populix':
            assert True
            self.log.info("=== test 1_Login Page Title: PASS ===")
            self.driver.close()
        else:
            self.log.error("=== test 1_Login Page Title: FAIL ===")
            self.driver.close()
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
            assert False 

    def test_valid_login(self):
   
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
            assert True
            self.log.info("=== test 2_Valid Login Test: PASS ===")
            self.driver.close()
        else:
            self.log.error("=== test 2_Valid Login Test: FAIL ===")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False 
            
        

# import pytest
# from selenium import webdriver
# from pageObject.LoginPage import LoginPage
# # from utilities.readProperties import ReadConfig
# # from utilities.customLogger import LogGen

# baseURL = 'https://www.populix.co/login'
# email = 'valiantartwear@gmail.com'
# passw = 'batangcoklat'

# @pytest.fixture
# def driver():
#         driver = webdriver.Chrome()
#         driver.get('https://www.populix.co/login')
#         driver.implicitly_wait(10)
#         driver.set_window_size(697, 720)
#         yield driver
#         driver.quit()

# def test_homePageTitle(driver):
#         driver.get(baseURL)
#         act_title=driver.title

#         if act_title=='Populix':
#             driver.close()
#             assert True
#         else:
#             assert False 

# def test_login(driver):
#         driver.get(baseURL)
#         lp=LoginPage(driver)
#         lp.setUserName(username)
#         lp.setPassword(password)
#         lp.clickLogin()
#         page_url=driver.current_url
#         if page_url=='https://www.populix.co/study':
#             driver.close()
#             assert True
#         else:
#             assert False 