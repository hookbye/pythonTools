# -*- coding : utf-8 -*-

import sys
import os

spliterLen = 35
printPrompt = " done-------------"

def donePrint(str = None):
	if str:
		print (str+printPrompt)
	else:
		print( printPrompt)

def gitCmd(cmd):
	os.system("" + cmd)

def initGitHub(proName):
	if proName:
		try:
			gitCmd("echo \"# " + proName + "\" >> README.md")
			gitCmd("git init")
			gitCmd("git config --global user.name hookbye")
			gitCmd("git config --global user.email \"weljun@sina.com\"")
			gitCmd("git add README.md")
			gitCmd("git commit -m \"initGitDone\"")
			gitCmd("git remote add origin https://github.com/hookbye/" + proName)
			gitCmd("git push -u origin master")
			genIgnore()
		except Exception as ex:
			print ('init project Exception:\r\n')
			print (ex)
	else:
		print ("No valide project")

def genIgnore():
	gitCmd("echo #ignoreFiles >> .gitignore")
	donePrint()
	showMenuList()

def setAlias():
	gitCmd("git config --global alias.co checkout")
	gitCmd("git config --global alias.ci commit")
	gitCmd("git config --global alias.pl pull")
	gitCmd("git config --global alias.ps push")
	gitCmd("git config --global alias.st status")
	donePrint()
	showMenuList()

def showMenuList():
	print ("*"*spliterLen)
	print ("  select item to do:")
	print ("  1 : initGitHub(weljun@sina.com)")
	print ("  2 : set git alias")
	print ("  3 : genIgnore")
	print ("  q : exit")
	print ("*"*spliterLen)
	print ("input :",)
	
if __name__ == '__main__':
	showMenuList()
	while True:
		itemSelect = input()
		if itemSelect == '1':
			print( "input projectName:",)
			pro_name = input()
			if pro_name:
				initGitHub(pro_name)
		elif itemSelect == '2':
			setAlias()
		elif itemSelect == '3':
			genIgnore()
		elif itemSelect == "q":
			sys.exit()

