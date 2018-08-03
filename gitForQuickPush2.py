#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os

def gitCmd(cmd):
	os.system("" + cmd)

def gitPush():
	gitCmd("git add -A")
	print "git add all done!"
	print u"输入提交日志:",
	commitInfo = raw_input()
	if commitInfo == "":
		commitInfo = "\"quick commit for save\""
	gitCmd("git ci -m "+commitInfo)
	print "git commit done!"
	gitCmd("git pl")
	gitCmd("git ps")
	print "git push done!"
if __name__ == '__main__':
	try:
		gitPush()
	except Exception,ex:
		print ex
		raw_input()