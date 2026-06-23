from selenium.webdriver.common.by import By
from base.mp.base import BasePage, BaseHandle
# 定义对象库层
class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名显示元素
        self.username = By.CSS_SELECTOR, ".user-name"
        # “内容管理”菜单
        self.content_manage = By.XPATH, "//*[text()='内容管理']"
        # “发布文章”
        self.publish_btn = By.XPATH, \
                           "//*[@class='sidebar-el-menu el-menu']/div[2]/li/ul/li[1]"
    # 定位用户名显示元素
    def find_username(self):
        return self.get_element(self.username)
    # 定位“内容管理”菜单
    def find_content_manage(self):
        return self.get_element(self.content_manage)
    # 定位“发布文章”菜单
    def find_publish(self):
        return self.get_element(self.publish_btn)
# 定义操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()
    # 获取用户名信息
    def get_username(self):
        return self.home_page.find_username().text
    # 单击“内容管理”菜单
    def click_content_manage(self):
        self.home_page.find_content_manage().click()
    # 单击“发布文章”
    def click_publish_btn(self):
        self.home_page.find_publish().click()
# 定义业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()
    # 获取用户名信息
    def get_username_msg(self):
        return self.home_handle.get_username()
    # 跳转到“发布文章”页面
    def go_publish_page(self):
        self.home_handle.click_content_manage()
        self.home_handle.click_publish_btn()