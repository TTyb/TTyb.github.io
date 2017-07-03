# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

from PIL import Image
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import io
from PIL import ImageChops

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
    time.sleep(1)
    return png

# 获取滑块的图片，是为了得到滑块的宽度gt_slice gt_show

# 获取滑动偏移量
def getOffset():
    img1 = screenShotImage()
    drag_and_drop(x_offset=5, y_offset=0)
    img2 = screenShotImage()
    # 判断两张图片不同的地方
    img3 = ImageChops.difference(img1, img2)
    img3.save(str(int(time.time())) + ".png")
    w1, h1 = img1.size
    w2, h2 = img2.size
    w3, h3 = img3.size
    print("wh")
    print(w1, h1, w2, h2)

    if w1 != w2 or h1 != h2:
        return False

    aa = 52
    print("开始循环", w3, h3)
    for x in range(aa+1, w3):
        print(x)
        for y in range(0, h3):
            pix3 = img3.getpixel((x, y))
            print(pix3[0],pix3[1],pix3[2])
            # 如果相差超过50则就认为找到了缺口的位置
            if pix3[0] > 50 and pix3[1] > 50 and pix3[2] > 50:
                return x-2
    return 55


# mian函数前的准备工作
def readyMain(url, keyword):
    openbrowser(url)
    inputKeyword(keyword)
    offset = getOffset()
    print(offset)
    drag_and_drop(x_offset=offset, y_offset=0)


if __name__ == "__main__":
    url = "http://www.gsxt.gov.cn/index.html"
    keyword = "中国联通"
    readyMain(url, keyword)
