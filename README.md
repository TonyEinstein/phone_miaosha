# phone_misaosha
蓝厂手机商城商品秒杀
<p align="center">
   <img alt="Python 3.7" src="https://img.shields.io/badge/python-3.7-green.svg?style=plastic">
  <img alt="selenium" src="https://img.shields.io/badge/selenium-green.svg?style=plastic">
  <img alt="retrying" src="https://img.shields.io/badge/retrying-green.svg?style=plastic">
  <img alt="pyppeteer 1.0.2" src="https://img.shields.io/badge/pyppeteer-1.0.2-green.svg?style=plastic">
  <img alt="asyncio" src="https://img.shields.io/badge/asyncio-green.svg?style=plastic">
  <img alt="pyppeteer_stealth 2.7.4" src="https://img.shields.io/badge/pyppeteer_stealth-2.7.4-green.svg?style=plastic">
</p>

## 使用前提
- 需要你有一个某商城已经注册的账号，并且填好收货信息。
### 提示：本仓库仅用为学习用途使用。

## 依赖包
- Python 3.7
- selenium
- retrying
- pyppeteer
- asyncio
- pyppeteer_stealth==2.7.4

可以使用以下命令安装依赖项::
```bash
pip install -r requirements.txt
```
注意：'requirements.txt'文件带的环境是我用来学习的虚拟环境，很多依赖包，使用上面这个命令的话会安装过程比较久。
建议直接pip安装上面所需要的4个库，asyncio记得是自带的，如果没有的话就安装上。
```bash
pip install selenium
pip install retrying
pip install pyppeteer
pip install pyppeteer_stealth
```
## 使用步骤

### 1.配置环境
- 创建虚拟环境，在虚拟环境中安装好上面的库。
- 下载chromedriver，根据自己的浏览器版本选择chromedriver的版本，我的是chromedriver_win32_106.0.5249.61.zip。
- 打开pycharm直接选择 已经存在的环境。

### 2.配置秒杀网址
由于pyppeteer_main文件还未完善(这个速度更快，需要者可提issue催更)，故而本配置是针对selenium_main文件的配置说明。
- 打开商品首页，点击登录之后点击选择 微信扫码登录，然后复制二维码页面的链接，粘贴到miaosha函数的page_url变量处赋值。
- 打开某商城秒杀活动页面，在秒杀倒计时10分钟的时候，点击商品的“即将开始”按钮进入商品页面。
- 复制商品页面的网址到mian函数中调用miaosha(options,commodity_link)的commodity_link处赋值。
- 进行运行即可。
- 运行之后，快速使用微信扫码登录，然后等待秒杀结果即可。




