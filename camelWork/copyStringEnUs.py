#coding=utf-8
import sys
import os
import shutil

fileName = "string_en_US.txt"

srcfilePath = "D:\\work\\planer\\config_tools\\GTGenerator\\"
dstfilePath = "D:\\work\\dev_2017\\Assets\\HotRes\\Lua\\Locale\\"

def showMenuList():
	print ("*"*10)
	print ("  select item to do:")
	print ("  commit text")
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
	if inputA != "q":
		os.chdir(dstfilePath)
		os.system("svn commit -m \""+inputA+"\"")
		print("update string_en_US done!!")
	else:
		sys.exit()