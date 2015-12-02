import arcpy,os
from arcpy import env

targetSchool = 'Tulane University' ##raw_input('Enter School Name ')
targetYear = 2015 ##raw_input('Enter Year of Interest ')

root = '\\\\sora\\strpublic\\Kyle VanderBush\\GIS\\'
targetDir = root+targetSchool
targetGdb = targetSchool+'_'+str(targetYear)+'.gdb'

if not os.path.isdir(targetDir):
    os.mkdir(targetDir)
if not os.path.isdir(targetDir+'\\'+targetGdb:
    arcpy.CreateFileGDB_management(targetDir,targetGdb)

env.workspace = targetDir+targetGdb

print "Dir verified and workspace set to %s" % env.workspace

