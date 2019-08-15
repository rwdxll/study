
from airtest.core.api import *
import time

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

start_app('com.movies.hydq')
time.sleep(5)
poco("com.android.packageinstaller:id/permission_allow_button").wait(5).click()
poco("com.android.packageinstaller:id/permission_allow_button").wait(5).click()


poco(text="我的").click()
poco(text="点击登录/注册").click()
# poco.device.wake()
text("yuuuuu2016@163.com")
text("12345678")
time.sleep(3)
poco("com.movies.hydq:id/login_bt").click()
if poco('yuuuuu2016@163.com ').exists:
    print('login is successful')