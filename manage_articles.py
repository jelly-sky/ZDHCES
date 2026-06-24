"""
清理旧文章 + 发布项目相关文章（含图片）
运行方式: python manage_articles.py
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 项目内图片路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "images")
SCREENSHOTS = {
    "Jenkins持续集成实践": os.path.join(IMG_DIR, "jenkins_plugins.png"),
    "Allure测试报告生成": os.path.join(IMG_DIR, "jenkins_report.png"),
    "Jenkins环境配置详解": os.path.join(IMG_DIR, "jenkins_config.png"),
}

# 要发布的项目相关文章
NEW_ARTICLES = [
    {"title": "自动化测试环境配置", "content": "本文介绍如何搭建Python+Selenium+Pytest自动化测试环境，包括JDK、ChromeDriver、Allure等工具的安装与配置。", "channel": "数据库"},
    {"title": "Jenkins持续集成实践", "content": "通过Jenkins实现自动化测试的持续集成，配置构建任务、Allure报告生成和邮件通知。以下是Jenkins插件管理页面截图。", "channel": "数据库"},
    {"title": "Jenkins环境配置详解", "content": "详细记录Jenkins的系统配置过程，包括JDK路径、Git路径、Python路径、Allure工具路径以及邮件通知的SMTP配置。", "channel": "数据库"},
    {"title": "PO模式在自动化测试中的应用", "content": "采用Page Object设计模式封装页面元素和操作，提高测试代码的可维护性和复用性。", "channel": "数据库"},
    {"title": "pytest测试框架入门", "content": "pytest是一款强大的Python测试框架，支持参数化、fixture、插件扩展等特性。", "channel": "数据库"},
    {"title": "Selenium元素定位技巧", "content": "总结Selenium常用的元素定位方法：ID、CSS选择器、XPath等，以及动态元素的处理策略。", "channel": "数据库"},
    {"title": "Allure测试报告生成", "content": "使用Allure生成可视化测试报告，展示用例通过率、执行耗时、失败截图等关键信息。以下是Jenkins中Allure报告页面截图。", "channel": "数据库"},
    {"title": "Git版本控制基础", "content": "掌握Git常用命令：init、add、commit、push、pull，理解工作区、暂存区、版本区的区别。", "channel": "数据库"},
    {"title": "数据驱动测试实战", "content": "使用DDT数据驱动框架实现参数化测试，将测试数据与脚本分离，提升代码复用性。", "channel": "数据库"},
    {"title": "Web自动化测试框架设计", "content": "从零搭建Web自动化测试框架，包含工具类封装、基类设计、日志配置和异常处理。", "channel": "数据库"},
    {"title": "Appium移动端测试入门", "content": "使用Appium+MuMu模拟器进行Android应用自动化测试，配置desired capabilities和元素定位。", "channel": "数据库"},
    {"title": "自动化测试用例设计方法", "content": "等价类划分、边界值分析、判定表、因果图等测试用例设计方法在自动化测试中的应用。", "channel": "数据库"},
    {"title": "持续集成流水线搭建", "content": "从代码提交到自动构建、自动测试、报告生成的完整持续集成流水线搭建指南。", "channel": "数据库"},
]

def upload_image(driver, wait, image_path):
    """在发布页面上传封面图片"""
    if not os.path.exists(image_path):
        print(f"  图片不存在: {image_path}")
        return False
    
    try:
        # 查找文件上传input（通常是hidden的）
        file_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
        if file_inputs:
            file_inputs[0].send_keys(image_path)
            time.sleep(2)
            print(f"  图片上传成功: {os.path.basename(image_path)}")
            return True
        else:
            print("  未找到文件上传入口")
            return False
    except Exception as e:
        print(f"  图片上传失败: {e}")
        return False

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    # 1. 登录
    print("正在登录...")
    driver.get("http://pc-toutiao-python.itheima.net/#/login")
    time.sleep(2)
    
    # 页面已预填手机号和验证码，直接点击登录
    driver.execute_script("document.querySelector('.el-button--primary').click()")
    time.sleep(3)
    print(f"登录成功，当前URL: {driver.current_url}")
    
    # 2. 进入内容管理 -> 内容列表
    print("进入文章列表...")
    content_manage = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='内容管理']")))
    content_manage.click()
    time.sleep(1)
    
    content_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='内容列表']")))
    content_list.click()
    time.sleep(3)
    
    # 3. 删除旧文章
    print("开始清理旧文章...")
    deleted = 0
    while True:
        delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".el-button--danger")
        if not delete_buttons:
            break
        try:
            delete_buttons[0].click()
            time.sleep(0.5)
            confirm_btns = driver.find_elements(By.CSS_SELECTOR, ".el-button--primary")
            for btn in confirm_btns:
                if btn.is_displayed() and ('确定' in btn.text or '确认' in btn.text):
                    btn.click()
                    break
            time.sleep(1)
            deleted += 1
            print(f"已删除第 {deleted} 篇文章")
        except Exception as e:
            print(f"删除出错: {e}")
            break
    
    # 4. 发布新文章
    print(f"\n开始发布 {len(NEW_ARTICLES)} 篇新文章...")
    published = 0
    
    for i, article in enumerate(NEW_ARTICLES):
        try:
            # 进入发布页面
            driver.get("http://pc-toutiao-python.itheima.net/#/publish")
            time.sleep(2)
            
            # 输入标题
            title_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@placeholder='文章名称']")))
            title_input.clear()
            title_input.send_keys(article["title"])
            time.sleep(0.5)
            
            # 输入内容（切换到iframe）
            iframe = wait.until(EC.presence_of_element_located((By.ID, "publishTinymce_ifr")))
            driver.switch_to.frame(iframe)
            content_body = driver.find_element(By.CSS_SELECTOR, ".mce-content-body")
            content_body.clear()
            content_body.send_keys(article["content"])
            driver.switch_to.default_content()
            time.sleep(0.5)
            
            # 如果有对应图片，上传封面
            if article["title"] in SCREENSHOTS:
                print(f"  正在上传封面图片...")
                upload_image(driver, wait, SCREENSHOTS[article["title"]])
                time.sleep(1)
            else:
                # 没图片选择"无图"
                cover_options = driver.find_elements(By.XPATH, "//*[@role='radiogroup']/label")
                if len(cover_options) >= 4:
                    cover_options[3].click()
            time.sleep(0.5)
            
            # 选择频道
            channel_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@placeholder='请选择']")))
            channel_select.click()
            time.sleep(0.5)
            channel_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{article['channel']}']")))
            channel_option.click()
            time.sleep(0.5)
            
            # 点击发表
            publish_btn = driver.find_element(By.CSS_SELECTOR, "[class='el-button filter-item el-button--primary']")
            publish_btn.click()
            time.sleep(2)
            
            published += 1
            print(f"✅ 第 {i+1} 篇发布成功: {article['title']}")
        except Exception as e:
            print(f"❌ 第 {i+1} 篇发布失败: {article['title']} - {e}")
    
    print(f"\n完成！共删除 {deleted} 篇旧文章，成功发布 {published} 篇")
    driver.quit()

if __name__ == "__main__":
    main()
