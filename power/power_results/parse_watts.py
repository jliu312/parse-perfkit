import sys
import csv
import matplotlib.pyplot as plt
fname = sys.argv[1]
fout = open(f"{fname}.csv","w+")
writer=csv.writer(fout)
writer.writerow(["timestamp","watts"])
ts=0
y=[]
x=[]
with open(fname) as file:
    lines = file.readlines()
    for line in lines:
        watts=line.split(',')[0][7:]
        writer.writerow([ts,float(watts)])
        x.append(ts)
        y.append(float(watts))
        ts+=1


plt.plot(x,y)
plt.show()

