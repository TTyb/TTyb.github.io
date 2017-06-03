#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

if __name__=='__main__':

    # options = webdriver.ChromeOptions()
    # # 设置中文
    # options.add_argument('lang=zh_CN.UTF-8')
    # # 更换头部
    # options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    # # 无图模式
    # prefs = {
    #     'profile.default_content_setting_values': {
    #         'images': 2
    #     }
    # }
    # options.add_experimental_option('prefs', prefs)
    #
    # browser = webdriver.Chrome(chrome_options=options)
    #
    # url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=21&oq=21&rsp=-1"
    #
    # # 设置最长加载时间为90秒
    # browser.set_page_load_timeout(90)
    # try:
    #     # 输入网址
    #     browser.get(url)
    #     time.sleep(10)
    # except:
    #     # 超过90秒强制停止加载
    #     browser.execute_script('window.stop()')
    #
    #
    # # newwindow = "window.open('https://www.baidu.com');"
    # # 通过js新打开一个窗口
    # # browser.execute_script(newwindow)
    # # 全屏
    # # browser.maximize_window()
    #
    # # 1200*800分辨率
    # # browser.set_window_size(1200,800)
    # # 捕获所有的句柄
    # # handles = browser.window_handles
    # # 窗口切换，切换为新打开的窗口
    # # browser.switch_to_window(handles[-1])
    # # 切换回最初打开的窗口
    # # browser.switch_to_window(handles[0])
    #
    # # 截图
    # # browser.save_screenshot("E:/img.png")
    #
    # # 翻页到最后面
    # browser.execute_script("""
    #     (function () {
    #         var y = 0;
    #         var step = 100;
    #         window.scroll(0, 0);
    #
    #         function f() {
    #             if (y < document.body.scrollHeight) {
    #                 y += step;
    #                 window.scroll(0, y);
    #                 setTimeout(f, 100);
    #             } else {
    #                 window.scroll(0, 0);
    #                 document.title += "scroll-done";
    #             }
    #         }
    #
    #         setTimeout(f, 1000);
    #     })();
    # """)
    # print("下拉中...")
    # # time.sleep(180)
    # while True:
    #     if "scroll-done" in browser.title:
    #         break
    #     else:
    #         print("还没有拉到最底端...")
    #         time.sleep(10)

    browser = webdriver.Chrome()
    url = "https://www.baidu.com/"
    browser.get(url)

    browser.find_element_by_id("kw").clear()

    # 填写TTyb
    browser.find_element_by_id("kw").send_keys("TTyb")
    # 填写完后按回车键
    browser.find_element_by_id("kw").send_keys(Keys.ENTER)