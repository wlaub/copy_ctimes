import math, sys, os #it's just my preference
import glob
import json

data = {}

for filename in glob.iglob(os.path.join(sys.argv[1],'**'), recursive=True):
    stat = os.stat(filename)
    stat_dict = {k: getattr(stat, k) for k in dir(stat) if k.startswith('st_')}
    data[filename] = stat_dict

try:
    outfile = sys.argv[2]
except:
    outfile = 'out.json'



json.dump(data, open(outfile, 'w'))

