import os

file = "/your/log/file/path"
statinfo = os.stat(file)

if statinfo.st_size >= 10485760000:  #10GB file. 
    os.system('echo "" >' + file)
else :
    print ("File still not large enough to be removed.")
