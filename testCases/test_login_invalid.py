from selenium import webdriver
from utilities.dataLog import Log_Data
from utilities import excel

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

def readData():
        list = []
        path='.//TestData/LoginData_invalid.xlsx'
        
        # workbook = openpyxl.load_workbook(path)

        # sheet = workbook.get_sheet_by_name("Sheet1")

        # rows = sheet.max_row
        rows = excel.getRowCount(path, 'Sheet1')

        for r in range(2, rows+1):
            username=excel.readData(path, 'Sheet1',r,1)
            password=excel.readData(path, 'Sheet1',r,2)
            # username = sheet.cell(r, 1).value
            # password = sheet.cell(r, 2).value

            tuple = (username,password)
            list.append(tuple)

        print(list)
        return list
        
log = Log_Data.custom_logger()

def readDataEmailEmpty():
        list = []
        path='.//TestData/LoginData_invalid.xlsx'
    
        rows = excel.getRowCount(path, 'Sheet1')

        for r in range(2, rows+1):
            username=excel.readData(path, 'Sheet1',r,4)
            password=excel.readData(path, 'Sheet1',r,5)
            # username = sheet.cell(r, 1).value
            # password = sheet.cell(r, 2).value

            tuple = (username,password)
            list.append(tuple)

        print(list)
        return list

#===============================================================================================
# TESTCASE INVALID 1 : LOGIN with wrong email format (exp: @gamil.com) and unregistered email
#===============================================================================================
@pytest.mark.parametrize("username,password", readData())
def test_invalidEmail_login(driver, username, password): #DataDrivenTest
        
        log.info("=== Test_3_invalid_Login_EMAIL ===")
        driver.find_element(By.ID, "input_email").send_keys(username)

        driver.find_element(By.ID, "input_password").send_keys(password)
        driver.find_element(By.ID, "submit_login").click()
        # time.sleep(4)

        check = driver.find_element(By.ID, "input_email-helper-text").text
        if check == "Email yang anda masukan salah atau tidak terdaftar":
            assert True
            log.info("=== test 3_invalid Login Email Test: PASS")
        else:
            log.error("=== test 3_invalid Login Email Test: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "test_login_invalid_email.png")
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