import time
import pytest
from config import BaseDir
from page.mis.audit_page import AuditProxy
from page.mis.home_page import HomeProxy
from page.mis.login_page import LoginProxy
from utils import UtilsDriver, get_case_data
case_data = get_case_data(BaseDir + "/data/mis/test_login_data.json")
@pytest.mark.run(order=2)
class TestLogin:
    # 定义类级别的fixture初始化操作
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.audit_proxy = AuditProxy()
    # 定义类级别的fixture销毁操作
    def teardown_class(self):
        UtilsDriver.quit_mis_driver()
    # 定义测试方法
    @pytest.mark.parametrize("username, password, expect", case_data)
    def test_login(self, username, password, expect):
        self.login_proxy.login(username, password)
        time.sleep(2)
        result = self.home_proxy.get_quit()
        assert expect in result
    # 定义测试方法
    def test_audit_article(self):
        time.sleep(3)
        self.home_proxy.go_content_audit()
        self.audit_proxy.audit_article("测试发布文章", 
                                       "审核通过", "2021-11-10 00:00:00")
        result = self.audit_proxy.audit_article_pass("测试发布文章")
        assert result
