#coding=utf-8
#python 3.0
import sys
import os
import shutil

zh_cnName = "string_zh_CN.txt"
en_usName = "string_en_US.txt"
officialZhcn = "Official_strings\\"
srcfilePath = "D:\\work\\planer\\config_tools\\GTGenerator\\"
dstfilePath = "C:\\dev_2017\\Assets\\HotRes\\Lua\\Locale\\"
openGenForlder = "start explorer \"D:\work\planer\config_tools\GTGenerator\""
openForlder = "start explorer \"C:\dev_2017\Assets\HotRes\Lua\Locale\""
def copyStringfiles(name):
	list = os.listdir(srcfilePath)
	for i in range(0,len(list)):
		path = os.path.join(srcfilePath,list[i])
		if os.path.isfile(path) and list[i].find('string_')==0 and list[i]!='string_zh_CN.txt':
			if name :
				if list[i] == name:
					shutil.copyfile(path,dstfilePath+list[i])
			else:
				shutil.copyfile(path,dstfilePath+list[i])
			# print(path)
		# pass

def copyZhCn():
	listPath = srcfilePath+officialZhcn
	list = os.listdir(listPath)
	print(list)
	lastDir = list[len(list)-4]
	print(lastDir)
	path = os.path.join(listPath,lastDir+"//"+zh_cnName)
	print(zh_cnName)
	shutil.copyfile(path,dstfilePath+zh_cnName)

def showMenuList():
	print ("*"*10)
	print ("  select item to do:")
	print ("  0 : copy all")
	print ("  1 : copy zh_cn only")
	print ("  2 : copy us only")
	print ("  3 : copy zh_cn us")
	print ("  q or any key to esc ")

if __name__ == '__main__':
	#打开办公软件
	os.chdir(dstfilePath)
	os.system("svn up")
	os.chdir(srcfilePath)
	os.system("svn up")
	os.system(openGenForlder)
	# shutil.copyfile(srcfilePath+fileName,dstfilePath+fileName)
	showMenuList()
	# sys.exit()
	inputA = int(input())
	if inputA == 0:
		copyStringfiles(False)
		copyZhCn()
	elif inputA == 1:
		copyZhCn()
	elif inputA == 2:
		copyStringfiles(en_usName)
	elif inputA == 3:
		copyStringfiles(en_usName)
		copyZhCn()
		# os.system("svn commit -m \"update text\"")
		# print("update string_zh_CN done!!")
	else:
		pass
	os.system(openForlder)
	inputA = input()