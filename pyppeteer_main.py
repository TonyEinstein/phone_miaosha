#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import logging
import sys
import time
import datetime
import pyppeteer
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
import re
from retrying import retry  # 需第三方库，需pip进行安装

pyppeteer.DEBUG = True  # 将隐藏的错误打印为错误日志
pyppeteer_level = logging.WARNING
logging.getLogger('pyppeteer').setLevel(pyppeteer_level)
logging.getLogger('websockets.protocol').setLevel(pyppeteer_level)
pyppeteer_logger = logging.getLogger('pyppeteer')
pyppeteer_logger.setLevel(logging.WARNING)



def get_time(time_precision=-1):
    current_time = datetime.datetime.now()
    # 精度：默认去掉后四位
    current_time = str(current_time)[:time_precision]
    # print("current_time({}): \t".format(type(current_time)) + current_time)
    return current_time

def screen_size():
    # 使用tkinter获取屏幕大小
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def main():
    width, height = screen_size()
    browser = await launch(headless=False,userDataDir='./userdata',dumpio=True, autoClose=False, args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])
    page = await browser.newPage()
    # 页面大小一致
    await page.setViewport({"width": width,"height": height})
    # js为设置webdriver的值，防止网站检测
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.setUserAgent("....")
    await page.goto('....',)
    # ...  do something

    # 在登录页跳转之后添加;等待页面跳转
    # await page.waitForNavigation()
    await asyncio.sleep(100)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())




