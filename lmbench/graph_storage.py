import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
colors = [
    "#20BF55",
    "#3C6997",
    "#F3A712",
    "#D64933"
]
plt.rcParams.update({'font.size': 20})
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.grid(axis='y',linewidth=2,linestyle='dotted',zorder=0)
#KB/sec
plt.bar(["Pixel 3a"],[103521/1000.0],color=colors[0],zorder=3)
plt.bar(["6a-KVM"],[226325/1000.0],color='black',zorder=3)
plt.bar(["6a-KVM-LXD"],[228049/1000.0],color=colors[1],zorder=3)
plt.bar(["6a-native"],[232426/1000.0],color=colors[2],zorder=3)
plt.bar(["t4g.2xlarge"],[128356/1000.0],color=colors[3],zorder=3)

plt.ylabel("I/O Bandwidth (MB/s)")

plt.tight_layout()

plt.savefig('lmbench_io.png')
plt.show()
        
