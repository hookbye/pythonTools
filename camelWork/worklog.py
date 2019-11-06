#coding=utf-8
import sys
import os
import shutil
import time
import re

dailayFile = "dailyLog.txt"
weeklyFile = "weeklyLog.txt"
todayFile = "todayLog.txt"


svnPath = "D:\\work\\dev_2017\\Assets\\HotRes"
logPath = "C:\\Users\\Wangguojun\\Desktop"

def showMenuList():
	print ("*"*10)
	print ("  select log to show:")
	print ("  0 : today log")
	print ("  1 : daily log")
	print ("  ...")
	print ("  num for day to show Log")
	print ("  ...")
	print ("  7 : weekly log ")
	print ("  q to exit ")

def outPutLog(interal):
	fileName = dailayFile
	addTime = 0
	if interal > 1 :
		fileName = weeklyFile
		addTime = 86400
	localTime = time.time()
	endTime = localTime-localTime%86400+addTime
	endStr = time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(endTime))
	beginTime = endTime-86400*interal
	beginStr = time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(beginTime))
	timeStr = "{"+ beginStr +"}:"+"{"+ endStr +"}"
	logFileName = logPath+"\\" + fileName
	cmdStr = "svn log -r "+ timeStr +" --search wangguojun -l 500 > " + logFileName
	print(cmdStr)
	os.system(cmdStr)
	slimLog(logFileName)

deleteArr = [
	"--",
	"|",
]

def isInArr(arr,line):
	for item in arr:
		if item in line:
			return True
	return False

def findTime(str):
	pattern = re.compile(r'\d{2,4}-\d{2}-\d{2} \d{2}:\d{2}')
	match = pattern.search(str)
	if match:
		newStr = match.groups(0)
		return newStr
def slimLog(fileName):
	lineNum = 0
	lineTime = ""
	with open(fileName,"r") as f:
		lines = f.readlines()
	with open(fileName,"w",encoding="utf-8") as f:
		for line in lines:
			if isInArr(deleteArr,line) or line == "\n":
				lineTime = line.find
				tmp = findTime(line)
				if tmp:
					lineTime = tmp
					f.write(lineTime)
					print(lineTime)
				continue
			lineNum = lineNum + 1 
			line = str(lineNum)+" "+line 
			print(line)
			f.write(line)
		# with open(fileName,"w") as fw:
if __name__ == '__main__':
	#打开办公软件
	os.chdir(svnPath)
	os.system("svn up")
	showMenuList()
	inputA = input()
	while inputA:
		try:
			logType = int(inputA)
			if logType:
				outPutLog(logType)
				showMenuList()
				inputA = input()
			elif inputA == 'q':
				sys.exit()
		except expression as identifier:
			pass