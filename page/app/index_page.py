from selenium.webdriver.common.by import By
from base.app.base import BasePage, BaseHandle
from utils import app_swipe_find
# 定义对象库层
class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 滑动的框
        self.scroll_element = By.CLASS_NAME, "android.view.View"
        # 单击的频道
        self.channel = By.XPATH, "//android.view.View/*[contains(@text, '{}')]"
        # 查找滑动框
    def find_scroll_element(self):
        return self.get_element(self.scroll_element)
# 定义操作层
class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()
    # 边滑动边查找对应的频道
    def click_channel(self, channel):
        xpath = self.index_page.channel[0], self.index_page.channel[1].format(channel)
        app_swipe_find(self.index_page.driver, 
                       self.index_page.find_scroll_element(), xpath)
# 定义业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()
    def find_channel(self, channel):
        # 滑动频道元素框单击对应的频道
        self.index_handle.click_channel(channel)