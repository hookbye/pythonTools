#coding=utf-8
import sys
import os
import webbrowser
import subprocess
evn_list = os.environ
work_path = evn_list.get('WorkPath')
# print(evn_list)
# print (work_path)
unity_init_path = "D:\\work\\dev_2017\\Assets\\Scenes\\InitialScene.unity"
sublime_text_path = "\"C:\Program Files\Sublime Text 3\sublime_text.exe \""
chrome_path = "\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\""
mantis_url = "http://192.160.1.201:8080/mantis/my_view_page.php"
wechat_path = "D:\\微信\\WeChat\\WeChat.exe"
beginWorkPath = "C:\\Users\\Wangguojun\\Desktop\\pythonScripts\\camelWork\\todayTask.txt"

# cmds = [sublime_text_path,chrome_path,wechat_path,unity_init_path]

# def contractCmd(cmd1,cmd2):
# 	return cmd1 + " && " + cmd2
# cmd = ""
# for _cmd in cmds:
# 	cmd = contractCmd(cmd,_cmd)
noStart = False
def useCmd(cmd,noStart=False):
	if not noStart:
		os.system("start " + cmd)
	else:
		os.system(cmd)
	# os.Popen(cmd)
	 # subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if __name__ == '__main__':
	#打开办公软件
	useCmd(unity_init_path)
	print("unity 	done!")
	#打开微信
	useCmd(wechat_path)
	print("wechat 	done!")
	useCmd(beginWorkPath)
	print("sublime 	done!")
	#打开chrome mantis
	# useCmd(chrome_path)
	webbrowser.open(mantis_url,new=1,autoraise=True) 
	print("mantis 	done!")