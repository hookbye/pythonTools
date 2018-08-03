#coding=utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

def gitCmd(cmd):
	os.system("" + cmd)

def gitPush():
	gitCmd("git add -A")
	gitCmd("git st")
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
	print u"回车关闭...."
	raw_input()
if __name__ == '__main__':
	try:
		gitPush()
	except Exception,ex:
		print ex
		raw_input()