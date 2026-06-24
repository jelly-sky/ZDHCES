import json
import time
from selenium import webdriver
from appium import webdriver as app_driver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
# 定义工具类
class UtilsDriver:
    # 表示自媒体运营系统的浏览器驱动
    _mp_driver = None
    # 表示后台管理系统的浏览器驱动
    _mis_driver = None
    # 表示App用户端的浏览器驱动
    _app_driver = None
    # 后台管理系统退出驱动的标识
    __quit_mis_driver = True
    # 定义修改私有属性的方法
    @classmethod
    def set_quit_driver(cls, mark):
        cls.__quit_mis_driver = mark
    # 定义获取自媒体运营系统的浏览器驱动
    @classmethod
    def get_mp_driver(cls):
        if cls._mp_driver is None:
            cls._mp_driver = webdriver.Chrome()
            cls._mp_driver.maximize_window()
            cls._mp_driver.get("http://pc-toutiao-python.itheima.net/#/login")
        return cls._mp_driver
    # 定义退出自媒体运营系统的浏览器驱动
    @classmethod
    def quit_mp_driver(cls):
        if cls._mp_driver is not None:
            cls.get_mp_driver().quit()
            cls._mp_driver = None
    # 定义获取后台管理系统的浏览器驱动
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = webdriver.Chrome()
            cls._mis_driver.maximize_window()
            cls._mis_driver.get("http://mis-toutiao-python.itheima.net/#/")
        return cls._mis_driver
    # 定义退出后台管理系统操作的浏览器驱动
    @classmethod
    def quit_mis_driver(cls):
        if cls._mis_driver and cls.__quit_mis_driver:
            cls.get_mis_driver().quit()
            cls._mis_driver = None
    # 定义获取App用户端的浏览器驱动
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            options = UiAutomator2Options()
            options.platform_name = "android"
            options.platform_version = "12"
            options.device_name = "MuMu"
            options.app_package = "com.android.chromium"
            options.app_activity = "com.google.android.apps.chrome.Main"
            options.no_reset = True
            options.reset_keyboard = True
            options.unicode_keyboard = True
            options.set_capability("appium:adbExecPath", r"D:\MuMu模拟器\MuMu Player 12\shell\adb.exe")
            cls._app_driver = app_driver.Remote("http://localhost:4723/wd/hub", options=options)
        return cls._app_driver
    # 定义退出App用户端浏览器驱动的方法
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls.get_app_driver().quit()
            cls._app_driver = None
# 封装自媒体运营系统选择频道的方法
def choice_channel(driver, element, channel):
    element.click()
    time.sleep(1)
    xpath = "//*[@class='el-select-dropdown__wrap el-scrollbar__wrap']" \
            "//*[text()='{}']".format(channel)
    driver.find_element(By.XPATH, xpath).click()
# 封装一个方法，用于判断元素是否存在
def is_exist(driver, text):
    xpath = "//*[contains(text(), '{}')]".format(text)
    try:
        time.sleep(2)
        return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        return False
# 封装获取测试数据的方法
def get_case_data(filename):
    with open(filename, encoding='utf-8') as f:
        case = json.load(f)
    list_case_data = []
    for case_data in case.values():
        list_case_data.append(tuple(case_data.values()))
    return list_case_data
# 定义app中边滑动边查找的方法
def app_swipe_find(driver, element, target_ele):
    """
    :param driver: 表示App的驱动
    :param element: 表示滑动的元素对象
    :param target_ele: 表示要查找的元素的定位的值
    :return:
    """
    # 获取元素的坐标点位置
    location = element.location
    # 获取X坐标点的值
    x = location["x"]
    # 获取Y坐标点的值
    y = location["y"]
    size = element.size
    width = size["width"]
    height = size["height"]
    start_x = x + width*0.9
    end_y = y + height * 0.5
    end_x = x + width * 0.1
    while True:
        page_source = driver.page_source
        try:
            time.sleep(2)
            driver.find_element(*target_ele).click()
            return True
        except Exception as e:
            driver.swipe(start_x, end_y, end_x, end_y, duration=1500)
        if page_source == driver.page_source:
            print("已滑屏到最后的页面，没有找到对应频道！")
            return False