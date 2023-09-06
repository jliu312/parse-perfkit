import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# native phone
color1 = "#3C6997"
plt.rcParams.update({'font.size': 21})
fig, ax = plt.subplots()
fig.set_size_inches(10,8)
plt.grid(axis="y",linestyle="dotted",linewidth=2,zorder=0)

multi_score = 93153.0/1000
labels = ["0","1","2","3","4","5","6","7","Multi"]
df = pd.read_csv("native_parsed.csv")
df = df.sort_values(by=['Core'])
iterations = [i/1000 for i in df['Iterations/s']]
iterations.append(multi_score)
ax.bar(labels[:-1],iterations[:-1],zorder=3,color="white",edgecolor=color1)
ax.bar(labels[-1],iterations[-1],zorder=3,color=color1)

ax.set_yticks([x*10 for x in range(10)])
#plt.ylabel("kIterations/s")
#plt.tight_layout()
plt.savefig("coremark_bycore.png")
plt.show()

# 155678

# #2xlarge
# plt.rcParams.update({'font.size': 20})
# fig, ax = plt.subplots()
# fig.set_size_inches(12,8)
# plt.grid(axis="y",linestyle="dotted",linewidth=2,zorder=0)

# multi_score = 155678/1000
# labels = ["C0","C1","C2","C3","C4","C5","C6","C7","Multi"]
# df = pd.read_csv("2xlarge_parsed.csv")
# df = df.sort_values(by=['Core'])
# iterations = [i/1000 for i in df['Iterations/s']]
# iterations.append(multi_score)
# ax.bar(labels[:-1],iterations[:-1],zorder=3,color="white",edgecolor="#3C6997")
# ax.bar(labels[-1],iterations[-1],zorder=3,color="#3C6997")

# ax.set_yticks([x*10 for x in range(16)])
# plt.ylabel("kIterations/s")
# plt.savefig("coremark_2xlarge.png")
# plt.show()
