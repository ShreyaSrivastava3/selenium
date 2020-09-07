from selenium import webdriver
import pytest
from Pages.Login_page import Login_page
from Pages.Home_page import Homepage
import pytest_html

class Test_OrangeHrm():
    @pytest.fixture()
    def setUpClass(self):
        self.driver=webdriver.Chrome(executable_path="/Users/shreya/PycharmProjects/Selenium/test/chromedriver")
        self.driver.maximize_window()
        yield
        self.driver.quit()
    #if two test cases krnge toh kaise run hoga
    def test_homePage(self,setUpClass):
        driver=self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        Home=Homepage(driver)
        Home.test_tittleofthepage()
        assert('OrangeHRM', self.driver.title)


        #self.assertEqual('OrangeHRM',self.driver.title)

    def test_LoginTest(self,setUpClass):#every test cases mein isliye likhe the get method qki jb bhi ek test cases run krta hai toh link open hoke band ho jata hai toh dusra test case run krne ke liye hume link ko open krna pdega
        driver=self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        Login = Login_page(driver)
        Login.test_username("Admin")
        Login.test_password("admin123")
        Login.test_button()

        #Home=Homepage(driver)
        #Home.test_tittleofthepage()


        self.driver.get("https://opensource-demo.orangehrmlive.com")
        #self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_id("btnLogin").click()
        #self.assertEqual('OrangeHRM', self.driver.title)

#pytest -v -s --html=report.html --self-contained-html Test_testDemo.py--to run the report
#--html=report.html --by default
#pytest -v -s --html=/Users/shreya/PycharmProjects/PytestRepo/Reports/report.html --self-contained-html Test_testDemo.py
#--by default--if location dena hai by choice
#--self-contained-html-- doubt
#pytest -v -s Test_testDemo.py-- to run the pytest


