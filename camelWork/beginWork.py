#coding=utf-8
import sys
import os
import webbrowser
import subprocess
import _thread
evn_list = os.environ
work_path = evn_list.get('WorkPath')
# print(evn_list)
# print (work_path)
unity_init_path = "C:\\dev_2017\\Assets\\Scenes\\InitialScene.unity"
sublime_text_path = "\"C:\Program Files\Sublime Text 3\sublime_text.exe \""
chrome_path = "\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\""
mantis_url = "http://192.160.1.201:8080/mantis/my_view_page.php"
wechat_path = "D:\\微信\\WeChat\\WeChat.exe"
beginWorkPath = "\"C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2019.1.1\\bin\\idea64.exe C:\\Users\\Wangguojun\\Desktop\\pythonScripts\\camelWork\\todayTask.txt\"" #"C:\\Users\\Wangguojun\\Desktop\\pythonScripts\\camelWork\\todayTask.txt"
work_codePath = "C:\\dev_2017\\Assets\\HotRes"
screen_capture = 'C:\\Users\\Wangguojun\\Desktop\\SETUNA.exe'
IDEAPath = "\"C:\Program Files\JetBrains\Intelli~1\bin\idea64.exe\""

openUnityProjectCmd = u"C:\\Progra~1\\Unity17_434\\Editor\\Unity.exe  -projectPath C:\\dev2017_4\\dev"

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
		print("cmd done")
	else:
		os.system(cmd)
	# os.Popen(cmd)
	 # subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def openUrl(url):
	webbrowser.open(url,new=1,autoraise=True)

def newThread(func,args,str=None):
	_thread.start_new_thread(func,(args,False))
	if str:
		print(str)
if __name__ == '__main__':
	#打开办公软件
	useCmd(openUnityProjectCmd)
	# newThread(useCmd,unity_init_path,"unity 	done!")
	#打开微信
	useCmd(wechat_path)
	# newThread(useCmd,wechat_path,"wechat 	done!")
	useCmd(screen_capture)
	newThread(useCmd,work_codePath,"workdir   done")
	# print("work snapshot done!")
	#打开chrome mantis
	openUrl(mantis_url)
	print("mantis 	done!")
	# _thread.start_new_thread(openUrl,(mantis_url,))
	# useCmd(beginWorkPath)
	# newThread(useCmd,OpenUnityWith17_1_4,"sublime 	done!")
	useCmd(IDEAPath)
