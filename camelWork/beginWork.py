#coding=utf-8
import sys
import os
import webbrowser
evn_list = os.environ
work_path = evn_list.get('WorkPath')
# print(evn_list)
# print (work_path)
unity_init_path = "D:\\work\\dev_2017\\Assets\\Scenes\\InitialScene.unity"
sublime_text_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
mantis_url = "http://192.160.1.201:8080/mantis/my_view_page.php"
wechat_path = "D:\\微信\\WeChat\\WeChat.exe"
if __name__ == '__main__':
	#打开办公软件
	os.system(unity_init_path)
	os.system(sublime_text_path)
	#打开chrome mantis
	webbrowser.open(mantis_url,new=1,autoraise=True) 
	#打开微信
	os.system(wechat_path)