#coding=utf-8
import sys
import os
import webbrowser
import subprocess
import _thread
evn_list = os.environ
work_path = evn_list.get('WorkPath')

unity_init_path = "C:\\Users\\hook\\Documents\\dev\\Assets\\Scenes\\InitialScene.unity"

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
	useCmd(unity_init_path)
	# os.system(OpenUnityWith17_1_4)
	# newThread(useCmd,OpenUnityWith17_1_4,"sublime 	done!")
