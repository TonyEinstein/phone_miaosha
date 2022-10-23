#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from retrying import retry  # 需第三方库，需pip进行安装
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
eager：等待整个dom树加载完成，即DOMContentLoaded这个事件完成，也就是只要 HTML完全加载和解析完毕就开始执行操作。放弃等待图片、样式、子帧的加载。
none：等待html下载完成，哪怕还没开始解析就开始执行操作。
"""



def get_time(time_precision=-1):
    current_time = datetime.datetime.now()
    # 精度：默认去掉后四位
    current_time = str(current_time)[:time_precision]
    # print("current_time({}): \t".format(type(current_time)) + current_time)
    return current_time

@retry(wait_fixed=0.3, stop_max_attempt_number=1)
def click_one(driver,path):
    # driver.find_element(By.XPATH, path).click()
    # 使用显示等待的方法
    element = WebDriverWait(driver, timeout=0.3, poll_frequency=0.05).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    element.click()


def miaosha(options,commodity_link):
    # 首先获取cookies保存至本地
    # 构造模拟浏览器并登录以及打开要抢的商品链接-----------------------------------------------
    # 通过driver.set_page_load_timeout()来设置页面加载超时时间
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_page_load_timeout(3)
    page_url = '登录页面扫码链接粘贴处'
    driver.get(page_url)
    # 进行扫码登录
    time.sleep(6)
    driver.get(commodity_link)
    time.sleep(5)
    driver.refresh()
    def fast(driver):
        flag = True
        while flag:
            try:
                # 开始抢商品---------------------------------------------------
                click_one(driver,'//*[@id="content"]//div[@class="prod-base-info-commodity clearfix"]/div[@class="prod-amount-normal clearfix"]/button')
                print("正在秒杀商品............... \t现在的时间：",get_time())
                # driver.refresh()
            except Exception as e:
                print(e)
                flag = False
        try:
            # 提交订单
            click_one(driver,'//div[@class="confirm-btn-box"]//div[@class="btn-submit"]')
            print("{} 已经提交商品订单成功！请前去付款!{}".format(get_time(), "---------" * 5))
        except Exception as e:
            print(e)
            # 提交订单
            click_one(driver,'//div[@class="confirm-btn-box"]//div[@class="btn-submit"]')
            print("{} 已经提交商品订单成功！请前去付款!{}".format(get_time(),"---------"*5))
        finally:
            # 提交订单
            click_one(driver, '//div[@class="confirm-btn-box"]//div[@class="btn-submit"]')
        try:
            click_one(driver,'//div[@class="confirm-btn-box"]//div[@class="btn-submit"]')
            print("{} 已经提交商品订单成功！请前去付款!{}".format(get_time(), "---------" * 5))
        except Exception as e:
            print(e)
            click_one(driver,'//div[@class="confirm-btn-box"]//div[@class="btn-submit"]')
        fast(driver)
    fast(driver)


if __name__ == '__main__':
    # 相关设置---------------------------------------------------
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')      # 设置无界面  可选
    # options.add_argument('--disable-gpu')  # 不加载gpu，规避bug
    # 设置禁止显示chrome正在受到自动测试软件控制
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-infobars")
    # 设置禁止扩展
    options.add_experimental_option('useAutomationExtension', False)
    #设置全屏
    options.add_argument("--start-maximized")
    # 设置user-agent
    # options.add_argument('user-agent=....')
    # 就是这一行告诉chrome去掉了webdriver痕迹，让服务器不知道是机器人
    options.add_argument("disable-blink-features=AutomationControlled")
    #  设置浏览器窗口永不关闭（有些时候浏览器在没有close的情况下会自己关闭）
    options.add_experimental_option("detach", True)

    # 设置 等待模式。none是显式模式，eager是隐式模式。
    # options.page_load_strategy = 'eager'
    options.page_load_strategy = 'none'

    # 设置秒杀结束时间
    price_miaosha = 0
    miaosha(options,commodity_link='秒杀商品链接粘贴处')

