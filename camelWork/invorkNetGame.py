#coding=utf-8
import sys
import os
import webbrowser
import subprocess
import _thread
evn_list = os.environ
work_path = evn_list.get('WorkPath')
openProjectCmd = u"C:\\Progra~1\\Unity\\Editor\\Unity.exe  -projectPath C:\\Users\\hook\\Documents\\OpenWorld"

noStart = False
def useCmd(cmd,noStart=False):
	if not noStart:
		os.system("start " + cmd)
		print("cmd done")
	else:
		os.system(cmd)

def openUrl(url):
	webbrowser.open(url,new=1,autoraise=True)

def newThread(func,args,str=None):
	_thread.start_new_thread(func,(args,False))
	if str:
		print(str)
if __name__ == '__main__':
        useCmd("git pl")
        useCmd(openProjectCmd)
        

