#coding=utf-8
import sys
import os
import shutil

fileName = "ServerAPI.txt"

srcfilePath = "D:\\work\\client\\schema\\"
dstfilePath = "C:\\dev_2017\\Assets\\HotRes\\Lua\\Network\\"

def showMenuList():
	print ("*"*10)
	print ("  select item to do:")
	print ("  y : commit text")
	print ("  q or any key to esc ")

if __name__ == '__main__':
	#打开办公软件
	os.chdir(dstfilePath)
	os.system("svn up")
	os.chdir(srcfilePath)
	os.system("svn up")
	shutil.copyfile(srcfilePath+fileName,dstfilePath+fileName)
	showMenuList()
	inputA = input()
	if inputA == "y":
		os.chdir(dstfilePath)
		os.system("svn commit -m \"update ServerAPI\"")
		print("update string_zh_CN done!!")
	else:
		sys.exit()