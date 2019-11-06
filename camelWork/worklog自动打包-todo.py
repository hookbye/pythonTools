#coding=utf-8
import sys
import os
import shutil
import time
import re
import webbrowser

url_dev_ios = "http://192.160.3.234:8080/view/WAO-2017/job/WAO-Dev-iOS-2017-Res/build?delay=0sec"
url_dev_android = "http://192.160.3.234:8080/view/WAO-2017/job/WAO-Dev-Android-Res-2017/build?delay=0sec"
if __name__ == '__main__':
	#打开办公软件
	webbrowser.open(url_dev_ios,new=1,autoraise=True)
	webbrowser.open(url_dev_android,new=1,autoraise=True)