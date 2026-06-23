import time
from selenium.webdriver.common.by import By
from base.app.base import BasePage, BaseHandle
from utils import app_swipe_find
# 定义对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # ”我的”按钮
        self.my_button = By.XPATH, "//*[@text='我的']"
        # 手机图标
        self.phone_button = By.XPATH, "//*[@text='login']"
        # ”登录”按钮
        self.login_button = By.CLASS_NAME, "android.widget.Button"
        # ”我的”按钮
    def find_my_button(self):
        return self.get_element(self.my_button)
        # 手机图标
    def find_phone_button(self):
        return self.get_element(self.phone_button)
        # ”登录”按钮
    def find_login_button(self):
        return self.get_element(self.login_button)
# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()
        # ”我的”按钮
    def click_my_button(self):
        self.login_page.find_my_button().click()
        # 手机图标
    def click_phone_button(self):
        self.login_page.find_phone_button().click()
        # ”登录”按钮
    def click_login_button(self):
        self.login_page.find_login_button().click()
# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()
    def go_index(self):
        # 单击”我的”按钮
        self.login_handle.click_my_button()
        # 单击手机图标
        self.login_handle.click_phone_button()
        time.sleep(2)
        # 单击”登录”按钮
        self.login_handle.click_login_button()