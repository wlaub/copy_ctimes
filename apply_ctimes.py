import math, sys, os #it's just my preference
import json
import time

from win32_setctime import setctime

data = json.load(open(sys.argv[1], 'r'))

try:
    logfile = sys.argv[2]
except:
    logfile = 'apply_ctimes_log.txt'

logfp = open(logfile, 'w')
def log(text):
    print(text)
    logfp.write(f'{text}\n')

for filename, stat in data.items():
    try:
        ostat = os.stat(filename)
        setctime(filename, stat['st_ctime'])
    except Exception as e:
        log(f'ERROR: Failed to set ctime on {filename}: {e}')
    else:
        strf = '%Y-%m-%d %H:%M:%S'
        otime = time.strftime(strf, time.localtime(ostat.st_ctime))
        ntime = time.strftime(strf, time.localtime(stat['st_ctime']))
        log(f'{filename}: {otime} change to {ntime}')


logfp.close()

