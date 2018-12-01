#create by guojun at 2018.11.10
#file name : beginWork.py

#bugs while developping
#1 os.system block the progress,when use many os.system commands,it turns that only close the first cmd,the next is the valide.
# fixed: use prefix command 'start' to start a new command

#2 use the python thread module to fix the block problem,but a new problem appeared.when useing more than two threads, it dosn't work until rebot the windows 
# fixed:only when it must to use thread,use it 