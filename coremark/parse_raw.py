import sys
import os
import csv
if len(sys.argv)<3:
    print("no")
    exit()
fname = sys.argv[1]
name = sys.argv[2]
outname=name+'_parsed.csv'
outfile=open(outname,'w+')
writer = csv.writer(outfile)
writer.writerow(["Core","Iterations/s"])
def extract_val(fileis):
    with open(fileis,'r') as f:
        for l in f.readlines():
            if "Iterations/Sec   :" in l:
                val=l.split(':')[1].strip()
                return val
for filename in os.listdir(fname):
    f = os.path.join(fname, filename)
    if os.path.isfile(f):
        if "log" not in f:
            continue
        cnumber = f[-5]
        value = extract_val(f)
        writer.writerow([cnumber,value])
outfile.close()
        



