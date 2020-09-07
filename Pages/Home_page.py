class Homepage():
    def __init__(self,driver):
        self.driver=driver

        self.tittle="OrangeaHRM"

    def test_tittleofthepage(self):
        assert(self.tittle, self.driver.title)

