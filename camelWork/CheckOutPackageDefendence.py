#-*- coding:UTF-8-*-
import os
configDir = "D:\\work\\dev_2017\\Assets\\HotRes\\config.txt"
prefabsDir = "D:\\work\\dev_2017\\AssetBundles\\webplayer"

OutPackageMap = {}

def GetOutPackageMap():
	filename = configDir
	with open(filename) as file_object:
	    for line in file_object:
	        # print(line.rstrip())
	        str = line.rstrip()
	        strArr = str.split(" ")
	        #print(strArr)
	        proiprity = 0
	        if(len(strArr)==2 and strArr[1].isdigit()):
	        	proiprity = int(strArr[1])
	        if (proiprity and proiprity > 10):
	        	OutPackageMap[strArr[0]] = True
	        	# print(strArr[0],proiprity)
	# print(OutPackageMap)

def CheckManifest(filename):
	beginToCheck = False
	with open(filename) as file_object:
	    for line in file_object:
	        # print(line.rstrip())
	        str = line.rstrip()
	        if(str == "Dependencies:"):
	        	beginToCheck = True
	        	continue
	        if beginToCheck:
	        	strArr = str.split("/")
	        	defenceName = strArr[len(strArr)-1]
	        	if OutPackageMap.get(defenceName):
	        		print("warning =========",filename,defenceName)
	        	else:
	        		#print(filename,defenceName+" safe")
	        		pass

def CheckStrMatch(str,matchStr,split):
	strArr = str.split(split)
	if(len(strArr)>0) and strArr[len(strArr)-1] == matchStr:
		return True
	else:
		return False

def CheckAssetBunddleDir():
	filenames = os.listdir(prefabsDir)
	for filename in filenames:
	    if(CheckStrMatch(filename,"manifest",".")):
	    	# print(filename)
	    	CheckManifest(prefabsDir+"\\"+filename)
if __name__ == '__main__':
	GetOutPackageMap()
	# CheckManifest(prefabsDir+"\\"+"prefabs_p.manifest")
	CheckAssetBunddleDir()