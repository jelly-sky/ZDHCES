import time
import pytest
from page.app.index_page import IndexProxy
from page.app.browser_page import BrowserProxy
from page.app.login_page import LoginProxy
from utils import UtilsDriver
# 定义测试类
@pytest.mark.run(order=3)
class TestFindArticle:
    # 定义类级别的fixture初始化方法
    def setup_class(self):
        self.index_proxy = IndexProxy()
        self.browser_proxy = BrowserProxy()
        self.login_proxy = LoginProxy()
    # 定义类级别的fixture销毁方法
    def teardown_class(self):
        time.sleep(2)
        UtilsDriver.quit_app_driver()
    def test_visit_hm(self):
        # 在模拟器的浏览器中输入黑马头条链接
        self.browser_proxy.go_hm_page("http://mp-toutiao-python.itheima.net")
        time.sleep(2)
    def test_login(self):
        self.login_proxy.go_index()
    def test_find_channel(self):
        self.index_proxy.find_channel("数据库")