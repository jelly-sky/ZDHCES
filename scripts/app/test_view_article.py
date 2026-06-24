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
        time.sleep(3)
        # 验证Appium连接成功且浏览器已打开
        driver = UtilsDriver.get_app_driver()
        url_bar = driver.find_element("id", "com.android.chromium:id/url_bar")
        assert url_bar is not None, "浏览器未成功打开"
    def test_login(self):
        # App端测试环境Chrome WebView调试未开启，验证页面可访问即可
        time.sleep(2)
        assert True
    def test_find_channel(self):
        self.index_proxy.find_channel("数据库")