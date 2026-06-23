from selenium.webdriver.common.by import By
from base.mp.base import BasePage, BaseHandle
from utils import UtilsDriver, choice_channel
# 定义对象库层
class PublishPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章名称输入框
        self.title = By.XPATH, "//*[@placeholder='文章名称']"
        # iframe元素对象
        self.iframe_ele = By.ID, "publishTinymce_ifr"
        # 文章内容输入框
        self.content = By.CSS_SELECTOR, ".mce-content-body "
        # 封面选择单选项
        self.cover = By.XPATH, "//*[@role='radiogroup']/label[4]/span[2]"
        # 频道选择下拉框
        self.channel = By.XPATH, "//*[@placeholder='请选择']"
        # “发表”按钮
        self.publish_btn = By.CSS_SELECTOR, \
                           "[class='el-button filter-item el-button--primary']"
    # 定位文章标题输入框
    def find_title(self):
        return self.get_element(self.title)
    # 定位切换的iframe
    def find_iframe(self):
        return self.get_element(self.iframe_ele)
    # 定位文章内容输入框
    def find_input_kw(self):
        return self.get_element(self.content)
    # 定位选择封面
    def find_cover(self):
        return self.get_element(self.cover)
    # 定位频道选择框
    def find_channel_choice(self):
        return self.get_element(self.channel)
    # 定位“发表”按钮
    def find_publish_btn(self):
        return self.get_element(self.publish_btn)
# 定义操作层
class PublishHandle(BaseHandle):
    def __init__(self):
        self.publish_page = PublishPage()
        self.driver = UtilsDriver.get_mp_driver()
    # 输入文章标题
    def input_title(self, title):
        self.input_text(self.publish_page.find_title(), title)
    # 输入文章内容
    def input_content(self, content):
        # 切换到iframe中
        self.driver.switch_to.frame(self.publish_page.find_iframe())
        # 输入文章内容
        self.input_text(self.publish_page.find_input_kw(), content)
        # 切回到默认首页
        self.driver.switch_to.default_content()
    # 选择封面
    def choice_cover(self):
        self.publish_page.find_cover().click()
    # 选择频道
    def choice_channel(self, channel):
        choice_channel(self.driver, 
                       self.publish_page.find_channel_choice(), channel)
    # 单击“发表”按钮
    def click_publish_btn(self):
        self.publish_page.find_publish_btn().click()
# 定义业务层
class PublishProxy:
    def __init__(self):
        self.publish_handle = PublishHandle()
    # 发布文章
    def publish_article(self, title, content, channel):
        # 输入文章标题
        self.publish_handle.input_title(title)
        # 输入文章内容
        self.publish_handle.input_content(content)
        # 选择封面
        self.publish_handle.choice_cover()
        # 选择频道
        self.publish_handle.choice_channel(channel)
        # 单击“发表”按钮
        self.publish_handle.click_publish_btn()
