import time
from selenium.webdriver.common.by import By
from base.mis.base import BasePage, BaseHandle
# 定义对象库层
class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 定位“退出”按钮
        self.quit_info = By.PARTIAL_LINK_TEXT, "退出"
        #定位“信息管理”
        self.content_manage = By.XPATH, "//*[@class='side_bar']/ul/li[3]/a"
        #定位“内容审核”
        self.content_audit = By.XPATH, "//*[@class='current3']/li[3]/a"
    # 定位“退出”按钮
    def find_quit_info(self):
        return self.get_element(self.quit_info)
    # 定位“信息管理”
    def find_content_manage(self):
        return self.get_element(self.content_manage)
    # 定位“内容审核”
    def find_content_audit(self):
        return self.get_element(self.content_audit)
# 定义操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()
    # 获取“退出”按钮文本信息
    def get_quit_info(self):
        return self.home_page.find_quit_info().text
    # 单击“信息管理”
    def click_content_manage(self):
        self.home_page.find_content_manage().click()
    # 单击“内容审核”
    def click_content_audit(self):
        self.home_page.find_content_audit().click()
# 定义业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()
    # 获取“退出”按钮文本信息
    def get_quit(self):
        return self.home_handle.get_quit_info()
    # 跳转到”内容审核“页面
    def go_content_audit(self):
        # 单击”信息管理“
        self.home_handle.click_content_manage()
        time.sleep(1)
        # 单击”内容审核“
        self.home_handle.click_content_audit()
