import matplotlib.pyplot as plt
import numpy as np

BLUE="#3C6997"
GREEN="#20BF55"
RED="#d64933"
plt.rcParams.update({'font.size': 32})
fig, ax = plt.subplots()
bottom = np.zeros(1)
fig.set_size_inches(14,12)

width = 0.7
#THE t4g.xlarge
t4g2xl_single = 19.697
t4g2xl_multi = 155.678
ax.bar(["t4g.2xlarge"], [t4g2xl_single], width, label="Singlecore", bottom=0,color='white',edgecolor=RED,zorder=3)
ax.bar(["t4g.2xlarge"], [t4g2xl_multi-t4g2xl_single], width, label="Multicore", bottom=t4g2xl_single,color=RED,edgecolor=RED,zorder=3)

#THE t4g.xlarge
t4g_single = 19.711 #test
t4g_multi = 78.649 #test
ax.bar(["t4g.xlarge"], [t4g_single], width, label="Singlecore", bottom=0,color='white',edgecolor=RED,zorder=3)
ax.bar(["t4g.xlarge"], [t4g_multi-t4g_single], width, label="Multicore", bottom=t4g_single,color=RED,edgecolor=RED,zorder=3)

labels = (
    "Pixel6a"
#    "Pixel6a Native"
)
values = {
    "Singlecore": np.array([27.497]),
    "Multicore": np.array([99.698-27.497]),
}
# values = {
#     "Singlecore": np.array([27.497,26.150]),
#     "Multicore": np.array([99.698-27.497,91.704-26.150]),
# }

plt.grid(axis="y",linestyle="dotted",linewidth=2,zorder=0)
for test, value in values.items():
    if test=="Multicore":
        p = ax.bar(labels, value, width, label=test, bottom=bottom,color=BLUE,edgecolor=BLUE,zorder=3)
    elif test=="Singlecore":
        p = ax.bar(labels, value, width, label=test, bottom=bottom,color='white',edgecolor=BLUE,zorder=3)        
    bottom += value

#THE PIXEL 3A
ax.bar(["Pixel 3a"], [12.308], width, label="Singlecore", bottom=0,color='white',edgecolor=GREEN,zorder=3)
ax.bar(["Pixel 3a"], [55.052-12.308], width, label="Multicore", bottom=12.308,color=GREEN,edgecolor=GREEN,zorder=3)

#ax.legend(loc="upper right")
plt.annotate('Solid: Multi core\nWhite: Single core',(1.9,150),color='black',backgroundcolor='white')
plt.annotate('155.7',(-0.2,156.8))
plt.annotate('78.6',(0.8,79.7)) #test
plt.annotate('99.7',(1.8,100.8))
#plt.annotate('91.7',(2.9,92.7))
plt.annotate('55.1',(2.8,56.2))

plt.annotate('19.7',(-0.2,20.8),color='white')
plt.annotate('19.7',(0.8,20.8),color='white') #test
plt.annotate('27.5',(1.8,28.6),color='white')
#plt.annotate('26.2',(2.9,27.2),color='white')
plt.annotate('12.3',(2.8,13.4),color='white')

plt.ylabel("Coremark score (kIterations/s)")
ax.set_yticks([x*20 for x in range(10)])
#plt.legend()
plt.savefig("coremark_compare.png")
plt.show()
