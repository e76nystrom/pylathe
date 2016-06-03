#!/cygdrive/c/Python27/Python.exe

import sys
import os
import subprocess

def dbg(txt, fmt):
    txt = txt + "\n"
    f.write(txt % fmt)

path = os.path.dirname(os.path.abspath(__file__))
f = open(path + "/git.log", "a")
sys.stdout = f
sys.stderr = f

if len(sys.argv) < 7:
    exit()

filePath = sys.argv[1]
fileDir = sys.argv[2]
file = sys.argv[3]
op = sys.argv[4]
date = sys.argv[5]
time = sys.argv[6]

dbg("%s %s %s %s %s %s", (filePath, fileDir, file, op, date, time))

filePath = filePath.replace('\\', '/')
#os.chdir(filePath)
filePath = filePath.replace('C:', '/cygdrive/c')

workTree = "--work-tree=" + filePath
repo = "--git-dir=" + filePath + "/.git"
file = fileDir + '/' + file
arg = '-m "%s on %s at %s"' % (op, date, time)

# print workTree
# print repo
# print file
# print arg

result = None
try:
    result = subprocess.check_output(["git", workTree, repo, "status"])
    # dbg("%s", (result))
except subprocess.CalledProcessError as e:
    dbg("status error %s", (e))

if file in result:
    try:
        result = subprocess.check_output(["git", workTree, repo, \
                                      "commit", file, arg])
        dbg("%s", (result))
    except subprocess.CalledProcessError as e:
        dbg("commit error %s", (e))

f.close()
