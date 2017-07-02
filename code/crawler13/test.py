# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

from PIL import Image
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import io


# 打开浏览器
def openbrowser(url):
    global browser

    # 声明谷歌浏览器
    browser = webdriver.Chrome()
    # 限制加载时间不能超过90秒
    browser.set_page_load_timeout(90)

    try:
        # 输入网址
        browser.get(url)
        if "400 Bad request" in browser.page_source:
            browser.get(url)
    except:
        # 超过90秒强制停止加载
        browser.execute_script('window.stop()')
        if "400 Bad request" in browser.page_source:
            browser.get(url)
        else:
            pass
    time.sleep(5)


# 输入关键字并查询
def inputKeyword(keyword):
    # 清空输入框
    browser.find_element_by_id("keyword").clear()
    # 输入查找的关键字
    browser.find_element_by_id("keyword").send_keys(keyword)
    time.sleep(5)
    # 点击查询按钮
    browser.find_element_by_id("btn_query").click()
    time.sleep(5)


# 拖放滑块
def drag_and_drop(x_offset, y_offset):
    # 找到滑块并滑动
    source = browser.find_element_by_class_name("gt_slider_knob")
    # 调用鼠标操作并且拖动
    ActionChains(browser).drag_and_drop_by_offset(source, x_offset, y_offset).perform()
    time.sleep(8)


# 截取验证码图片
def screenShotImage():
    try:
        # 定位到验证码的框
        captchaElement = browser.find_element_by_class_name("gt_box")
    except:
        inputKeyword(keyword)
        # 定位到验证码的框
        captchaElement = browser.find_element_by_class_name("gt_box")
    locations = captchaElement.location
    sizes = captchaElement.size

    left = int(locations["x"])
    top = int(locations["y"])
    right = left + int(sizes["width"])
    bottom = top + int(sizes['height'])

    # 截图
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(io.BytesIO(screenshot))
    png = screenshot.crop((left, top, right, bottom))
    png.save(str(int(time.time())) + ".png")
    return png


# 获取滑动偏移量
def getOffset():
    img1 = screenShotImage()
    drag_and_drop(x_offset=5, y_offset=0)
    img2 = screenShotImage()
    w1, h1 = img1.size
    w2, h2 = img2.size
    print("wh")
    print(w1, h1, w2, h2)

    if w1 != w2 or h1 != h2:
        return False

    aa = 60

    print("开始循环", w1, h1)
    for x in range(0, w1):
        for y in range(0, h1):
            pix1 = img1.getpixel((x, y))
            pix2 = img2.getpixel((x, y))
            # 如果相差超过50则就认为找到了缺口的位置
            print("diff", abs(pix1[0] - pix2[0]), abs(pix1[1] - pix2[1]), abs(pix1[2] - pix2[2]))
            if abs(pix1[0] - pix2[0]) >= aa and abs(pix1[1] - pix2[1]) >= aa and abs(pix1[2] - pix2[2]) >= aa:
                return x
    return 55


# mian函数前的准备工作
def readyMain(url, keyword):
    openbrowser(url)
    inputKeyword(keyword)
    screenShotImage()
    offset = getOffset()
    print(offset)
    drag_and_drop(x_offset=offset, y_offset=0)


if __name__ == "__main__":
    url = "http://www.gsxt.gov.cn/index.html"
    keyword = "中国联通"
    readyMain(url, keyword)
