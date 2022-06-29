import os, fnmatch, shutil
#get the current working directory and store the value in the variable workdir
workdir = os.getcwd()
#pather=keyword, path=folder path where the files resides  newpath=new path where you want to move the files
def find(pattern, path, newpath):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                shutil.move(os.path.join(root, name), newpath+name)
                result.append(os.path.join(root, name))
    return result
lps1=find('employee*', workdir+'/world/country/', workdir+'/world/employee/')
lps2=find('sales*', workdir+'/world/country/', workdir+'/world\sales/')
lps3=find('marketing*', workdir+'/world/country/', workdir+'/world/marketing/')
print(lps1)
print(lps2)
print(lps3)
#credit Ajit Kumar Singh