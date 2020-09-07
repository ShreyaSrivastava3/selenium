from Locators.Locator import Locat
class Login_page():
    def __init__(self,driver):
        self.driver=driver

        self.Username_textbox_id=Locat.Username_textbox_id
        self.Password_textbox_id="txtPassword"
        self.tittle="OrangeHRM"
        self.button_id="btnLogin"

    def test_username(self,username):
        self.driver.find_element_by_id(self.Username_textbox_id).clear()
        self.driver.find_element_by_id(self.Username_textbox_id).send_keys(username)


    def test_password(self,password):
        self.driver.find_element_by_id(self.Password_textbox_id).clear()
        self.driver.find_element_by_id(self.Password_textbox_id).send_keys(password)

    def test_button(self):
        self.driver.find_element_by_id(self.button_id).click()


