from selenium.webdriver.common.by import By
from base.app.base import BasePage, BaseHandle
# 定义对象库层
class BrowserPage(BasePage):
    def __init__(self):
        super().__init__()
        # 浏览器输入框
        self.browser_input_element = By.ID, "com.android.chromium:id/url_bar"
        # 浏览器”回车”按钮
        self.browser_enter_element = By.CLASS_NAME, "android.widget.ImageButton"
    # 浏览器输入框
    def find_browser_input_element(self):
        return self.get_element(self.browser_input_element)
    # 浏览器”回车”按钮
    def find_browser_enter_element(self):
        return self.get_element(self.browser_enter_element)
# 定义操作层
class BrowserHandle(BaseHandle):
    def __init__(self):
        self.browser_page = BrowserPage()
        # 浏览器输入框
    def input_browser_input_element(self, browser_input_element):
        self.input_text(self.browser_page.find_browser_input_element(), browser_input_element)
        # 浏览器”回车”按钮
    def click_browser_enter_element(self):
        self.browser_page.find_browser_enter_element().click()
# 定义业务层
class BrowserProxy:
    def __init__(self):
        self.browser_handle = BrowserHandle()
    # 在输入框进行输入
    def go_hm_page(self, browser_input_element):
        self.browser_handle.input_browser_input_element(browser_input_element)
        # 单击”回车”按钮
        self.browser_handle.click_browser_enter_element()