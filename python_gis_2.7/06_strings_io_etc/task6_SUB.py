#!/usr/bin/env python
import os, re, sys

#########################################
# TASK 6,EX 3.12
#########################################
#e.g. HOMEPATH
#path = sys.argv[1]
path = 'HOME'
path_env = "os.environ['" + path + "']"
#print path_env

#Set up fnc that checks if match, then prints to consol.
def includes_tmp(arg, dirname, files):
    for file_name in files:
        #print files
        match_tmp = re.match('tmp',file_name)
        if match_tmp:# is not None:
            print dirname, 'has tmp-file:', file_name

#os.path.walk(os.environ['USERPROFILE'], includes_tmp, None)
#os.path.walk(os.environ['HOMEPATH'], includes_tmp, None)

#putting in path, and calls includes_tmp on each path file 
#reached from the 'path-crawler'
os.path.walk(eval(path_env), includes_tmp, None)

