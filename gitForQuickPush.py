# -*- coding : utf-8 -*-

import sys
import os

def gitCmd(cmd):
	os.system("" + cmd)

def gitPush():
	gitCmd("git add -A")
	gitCmd("git ci -m \"quick commit for save\"")
	gitCmd("git pl")
	gitCmd("git ps")
if __name__ == '__main__':
	gitPush()