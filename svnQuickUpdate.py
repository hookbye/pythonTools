#coding=utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

def svnCmd(cmd):
	os.system("" + cmd)

def svnUp():
	svnCmd("svn update")
	print ("update done!")
if __name__ == '__main__':
	try:
		svnUp()
		print ("enter to quit!")
		raw_input()
	except Exception,ex:
		print (ex)