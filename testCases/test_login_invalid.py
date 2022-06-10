from selenium import webdriver
from utilities.dataLog import Log_Data
from utilities import excel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time


#==================================================================
#       FIXTURE
#==================================================================
@pytest.fixture()
def driver():
        driver = webdriver.Chrome()
        driver.get('https://www.populix.co/login')
        driver.implicitly_wait(10)
        driver.set_window_size(697, 720)
        yield driver
        driver.quit()

log = Log_Data.custom_logger()

def readDataInvalidEmail():
        list = []
        path='.//TestData/LoginData_invalid.xlsx'
        
        # workbook = openpyxl.load_workbook(path)

        # sheet = workbook.get_sheet_by_name("Sheet1")

        # rows = sheet.max_row
        # rows = excel.getRowCount(path, 'Sheet1')

        for r1 in range(2, 4):
            username=excel.readData(path, 'Sheet1',r1,1)
            password=excel.readData(path, 'Sheet1',r1,2)
            tuple = (username,password)
            list.append(tuple)

        print(list)
        return list

def readDataEmailEmpty():
        list = []
        path='.//TestData/LoginData_invalid.xlsx'

        for r2 in range(2, 4):
            username=excel.readData(path, 'Sheet1',r2,4)
            password=excel.readData(path, 'Sheet1',r2,5)
            # username = sheet.cell(r, 1).value
            # password = sheet.cell(r, 2).value
            tuple = (username,password)
            list.append(tuple)

        print(list)
        return list

def readDataInvalidPassword():
        list = []
        path='.//TestData/LoginData_invalid.xlsx'
        rows = excel.getRowCount(path, 'Sheet1')

        for r3 in range(8, rows+1):
            username=excel.readData(path, 'Sheet1',r3,1)
            password=excel.readData(path, 'Sheet1',r3,2)
            tuple = (username,password)
            list.append(tuple)

        print(list)
        return list

#===============================================================================================
# TESTCASE INVALID 1 : LOGIN with wrong email format (exp: @gamil.com) and unregistered email
#===============================================================================================
@pytest.mark.parametrize("username,password", readDataInvalidEmail())
def test1_invalidEmail_login(driver, username, password): #DataDrivenTest
        
        log.info("=== Test_1_invalid_Login_wrong format EMAIL ===")
        driver.find_element(By.ID, "input_email").send_keys(username)

        driver.find_element(By.ID, "input_password").send_keys(password)
        driver.find_element(By.ID, "submit_login").click()
        time.sleep(1)

        check = driver.find_element(By.ID, "input_email-helper-text").text
        if check == "Email yang anda masukan salah atau tidak terdaftar":
            assert True
            log.info("=== test 1_invalid wrong format Email Login Test: PASS")
        else:
            log.error("=== test 1_invalid wrong format Email Login Test: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "test1_login_invalid_wrong_email.png")
            assert False

#===============================================================================================
# TESTCASE INVALID 2 : LOGIN by leaving email field empty
#===============================================================================================
@pytest.mark.parametrize("password", readDataEmailEmpty())
def test2_invalidEmpty_Email_login(driver, password): #DataDrivenTest
        
        log.info("=== Test_2_invalid_Login_empty EMAIL ===")
        driver.find_element(By.ID, "input_email").click()
        driver.find_element(By.ID, "input_email").send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element(By.ID, "input_password").send_keys(password)
        driver.find_element(By.ID, "submit_login").click()

        check = driver.find_element(By.ID, "input_email-helper-text").text
        time.sleep(1)
        if check == "Email yang anda masukan salah atau tidak terdaftar":
            if "Password yang anda masukan salah" in driver.find_element(By.ID, "input_password-helper-text").text:
                assert True
                log.info("=== test 2_invalid empty Email Login Test: PASS")
        else:
            log.error("=== test 2_invalid empty Email Login Test: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "test2_login_invalid_empty_email.png")
            assert False

#===============================================================================================
# TESTCASE INVALID 3 : LOGIN by leaving password field empty
#===============================================================================================
@pytest.mark.parametrize("username", readDataInvalidPassword())
def test3_invalidEmpty_Password_login(driver, username): #DataDrivenTest
        
        log.info("=== Test_3_invalid_Login_empty PASSWORD ===")
        driver.find_element(By.ID, "input_email").send_keys(username)
        driver.find_element(By.ID, "submit_login").click()
        time.sleep(1)
        check = driver.find_element(By.ID, "input_email-helper-text").text
        
        if check == "Email yang anda masukan salah atau tidak terdaftar":
            if "Password yang anda masukan salah" in driver.find_element(By.ID, "input_password-helper-text").text:
                assert True
                log.info("=== test 3_invalid empty PASSWORD Login Test: PASS")
        else:
            log.error("=== test 3_invalid empty PASSWORD Login Test: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "test3_login_invalid_empty_password.png")
            assert False

#===============================================================================================
# TESTCASE INVALID 4 : LOGIN by leaving email field & password field empty
#===============================================================================================
def test4_invalidEmpty_login(driver):
        
        log.info("=== Test_4_invalid_Login_empty EMAIL & PASSWORD ===")
        driver.find_element(By.ID, "input_email").click()
        driver.find_element(By.ID, "input_password").click()
        driver.find_element(By.ID, "submit_login").click()
        time.sleep(1)
        check = driver.find_element(By.ID, "input_email-helper-text").text
        
        if check == "Email yang anda masukan salah atau tidak terdaftar":
            if "Password yang anda masukan salah" in driver.find_element(By.ID, "input_password-helper-text").text:
                assert True
                log.info("=== Test 4_invalid_Login_empty EMAIL & PASSWORD: PASS")
        else:
            log.error("=== Test 4_invalid_Login_empty EMAIL & PASSWORD: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "test4_login_invalid_empty_EmailPassword.png")
            assert False

#===============================================================================================
# TESTCASE INVALID 5 : LOGIN with valid email and wrong/unvalid password
#===============================================================================================
@pytest.mark.parametrize("username,password", readDataInvalidPassword())
def test5_invalidPassword_login(driver, username, password): #DataDrivenTest
        
        log.info("=== Test_5_invalid_Login_PASSWORD ===")
        driver.find_element(By.ID, "input_email").send_keys(username)

        driver.find_element(By.ID, "input_password").send_keys(password)
        driver.find_element(By.ID, "submit_login").click()
        time.sleep(1)

        check = driver.find_element(By.ID, "input_password-helper-text").text
        if check == "Password yang anda masukan salah":
            assert True
            log.info("=== test 5_invalid_Login_PASSWORD: PASS")
        else:
            log.error("=== test 5_invalid_Login_PASSWORD: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "test5_invalid_Login_PASSWORD.png")
            assert False

        
        # page_url = driver.current_url
        # if page_url=='https://www.populix.co/login':
        #     assert True
        #     log.info("=== test 3_invalid Login Email Test: PASS")
        # if  page_url=='https://www.populix.co/study':
        #     log.error("=== test 3_invalid Login Email Test: FAIL")
        #     driver.save_screenshot(".\\Screenshots\\" + "test_login_invalid_email.png")
        #     assert False


        #     assert True
        #     log.info("=== test invalid Login Test: PASS")
        #     # self.driver.close()
        # else:
        #     driver.save_screenshot(".\\Screenshots\\" + "test_invalid_login.png")  
        #     log.error("=== test invalid Login Test: FAIL")
        #     assert False

        # try:
        # assert "Email yang anda masukan salah" in driver.find_element(By.ID, "input_email-helper-text").text
        # finally:
        #     if(AssertionError):
        #         assert True
        #         log.info("=== test invalid Login Test: PASS ===")
        #     else:
        #         driver.save_screenshot(".\\Screenshots\\" + "test_invalid_login_email.png")  
        #         log.error("=== test invalid Login Test: FAIL ===")
        #         assert False    