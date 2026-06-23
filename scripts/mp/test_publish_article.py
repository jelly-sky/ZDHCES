import logging
import allure
import pytest
from config import BaseDir
import time
from selenium.webdriver.common.by import By
from page.mp.home_page import HomeProxy
from page.mp.login_page import LoginProxy
from page.mp.publish_page import PublishProxy
from utils import UtilsDriver, is_exist, get_case_data
case_data = get_case_data(BaseDir + "/data/mp/test_login_data.json")
# 定义测试类
@pytest.mark.run(order=1)
class TestPublishArticle:
    # 定义类级别的fixture初始化操作方法
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.publish_proxy = PublishProxy()
    # 定义类级别的fixture销毁操作方法
    def teardown_class(self):
        UtilsDriver.quit_mp_driver()
    # 定义登录的测试用例方法
    @pytest.mark.parametrize("username, code, expect", case_data)
    def test_login(self, username, code, expect):
        logging.info("用例的数据如下：用户名：{}， 验证码：{}，"
                     " 预期结果：{}".format(username, code, expect))
        self.login_proxy.login(username, code)
        driver = UtilsDriver.get_mp_driver()
        # 等待弹窗自动消失（2.5秒）
        time.sleep(2.5)
        # 再等3秒确保页面加载完成
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),
                      "登录截图", allure.attachment_type.PNG)
        # 验证登录成功：页面URL不再是登录页
        assert "login" not in driver.current_url.lower()
        time.sleep(2)
    # 定义发布文章功能的测试用例方法
    def test_publish_article(self):
        time.sleep(2)
        # 跳转到“发布文章”页面
        self.home_proxy.go_publish_page()
        time.sleep(2)
        # 发布文章的内容
        self.publish_proxy.publish_article("测试发布文章", "测试发布文章内容", "数据库")
        assert is_exist(UtilsDriver.get_mp_driver(), "新增文章成功")
        allure.attach(UtilsDriver.get_mp_driver().get_screenshot_as_png(),
                      "发布文章截图", allure.attachment_type.PNG)