from selenium.webdriver.support.wait import WebDriverWait
from utils import UtilsDriver
# 创建对象库层基类
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_mis_driver()
    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element
# 创建操作层基类
class BaseHandle:
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)