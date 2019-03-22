#coding=utf-8
import sys
import os
import shutil

fileName = "string_zh_CN.txt"

srcfilePath = "D:\\work\\planer\\config_tools\\GTGenerator\\"
dstfilePath = "D:\\work\\dev_2017\\Assets\\HotRes\\Lua\\Locale\\"

def showMenuList():
	print ("*"*10)
	print ("  select item to do:")
	print ("  y : commit text")
	print ("  q or any key to esc ")

if __name__ == '__main__':
	#打开办公软件
	os.chdir(srcfilePath)
	os.system("svn up")
	shutil.copyfile(srcfilePath+fileName,dstfilePath+fileName)
	showMenuList()
	inputA = input()
	if inputA == "y":
		os.chdir(dstfilePath)
		os.system("svn commit -m \"update text\"")
		print("update string_zh_CN done!!")
	else:
		sys.exit()