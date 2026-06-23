from selenium.webdriver.common.by import By
from base.mis.base import BasePage, BaseHandle
from utils import UtilsDriver
# 定义对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = By.NAME, "username"
        # 密码输入框
        self.password = By.NAME, "password"
        # “登录”按钮
        self.login_btn = By.ID, "inp1"
    # 定位用户名输入框
    def find_username(self):
        return self.get_element(self.username)
    # 定位密码输入框
    def find_password(self):
        return self.get_element(self.password)
    # 定位“登录”按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)
# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()
    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)
    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)
    # 单击“登录”按钮
    def click_login_btn(self):
        # 定义JS，取消滑动验证码
        js = "document.getElementById('inp1').removeAttribute('disabled')"
        # 通过execute_script方法执行JS
        self.login_page.driver.execute_script(js)
        # 单击“登录”按钮
        self.login_page.find_login_btn().click()
# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()
    # 登录业务操作
    def login(self, username, password):
        # 输入管理员用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 单击“登录”按钮
        self.login_handle.click_login_btn()