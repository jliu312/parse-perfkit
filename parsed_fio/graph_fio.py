import matplotlib.pyplot as plt
import pandas as pd
import math

colors = [
    "#20BF55",
    "#3C6997",
    "#F3A712",
    "#D64933"
]
plt.rcParams.update({'font.size': 20})
# --- Random read test --- #

#kvm
def graph(name,fname,test,ms=False):
    fig=plt.gcf()
    fig.set_size_inches(12,8)
    c=colors[0]
    if name=="t4g.small":
        c=colors[1]
    elif name=="t4g.2xlarge":
        c=colors[2]
    df = pd.read_csv(f"{fname}")
    dfp = df[df['Percentile']!=-1]
    extras = df[df['Percentile']==-1]
    print(f"---------- {test} ----------")
    for i in range(len(extras)):
        e=extras.iloc[i]
        v=e['Value']
        u=e['Units']
        vt=e['Value type']
        print(f"{name}: {test} {vt} - {v} ({u})")
    print(f"----------------------------")        
    units=list(set([u for u in dfp['Units']]))
    if len(units)>1:
        print("HMM not good - units")
    y = dfp['Percentile']
    x = dfp['Value']
    if ms:
        x = [n/1000 for n in x]    
    plt.ylabel("Percentile")
    vt = dfp.iloc[0]['Metric']
    #plt.xlabel(f"{vt} ({units[0]})")
    if ms:
        plt.xlabel("Latency (ms)")
    else:
        plt.xlabel("Latency (us)")
    plt.scatter(x,y,color=c)
    plt.plot(x,y,label=name,color=c,linewidth=3.5)
    #plt.title(test)

graph("KVM on Android","kvm/fio_KVM-App_random_read_test.csv","Random read test")
#graph("t4g.small","t4gsmall/fio_AWS-t4g.small_random_read_test.csv","Random read test")
graph("t4g.2xlarge","t4g2xlarge/fio_AWS-t4g.2xlarge_random_read_test.csv","Random read test")
plt.legend()
plt.grid(axis='y',linestyle='dotted',linewidth=2)
#plt.xlim(-100,5000)
plt.savefig(f"random_read_test.png")
plt.show()
# -- Random read test parallel -- #
graph("KVM on Android","kvm/fio_KVM-App_random_read_test_parallel.csv","Random read test parallel")
#graph("t4g.small","t4gsmall/fio_AWS-t4g.small_random_read_test_parallel.csv","Random read test parallel")
graph("t4g.2xlarge","t4g2xlarge/fio_AWS-t4g.2xlarge_random_read_test_parallel.csv","Random read test parallel")
plt.legend()
plt.grid(axis='y',linestyle='dotted',linewidth=2)
#plt.xlim(-100,50000)
plt.savefig(f"random_read_test_parallel.png")
plt.show()

# -- Random read test parallel: zoomed in -- #
graph("KVM on Android","kvm/fio_KVM-App_random_read_test_parallel.csv","Random read test parallel")
#graph("t4g.small","t4gsmall/fio_AWS-t4g.small_random_read_test_parallel.csv","Random read test parallel")
graph("t4g.2xlarge","t4g2xlarge/fio_AWS-t4g.2xlarge_random_read_test_parallel.csv","Random read test parallel")
plt.legend()
plt.grid(axis='y',linestyle='dotted',linewidth=2)
plt.xlim(-100,50000)
plt.savefig(f"random_read_test_parallel_zoomed.png")
plt.show()

# -- Write test -- #
graph("KVM on Android","kvm/fio_KVM-App_random_write_test.csv","Random write test")
#graph("t4g.small","t4gsmall/fio_AWS-t4g.small_random_write_test.csv","Random write test")
graph("t4g.2xlarge","t4g2xlarge/fio_AWS-t4g.2xlarge_random_write_test.csv","Random write test")
plt.legend()
plt.grid(axis='y',linestyle='dotted',linewidth=2)
plt.savefig(f"random_write_test.png")
plt.show()

# -- Sequential read -- #
graph("KVM on Android","kvm/fio_KVM-App_sequential_read.csv","Sequential read",ms=True)
#graph("t4g.small","t4gsmall/fio_AWS-t4g.small_sequential_read.csv","Sequential read",ms=True)
graph("t4g.2xlarge","t4g2xlarge/fio_AWS-t4g.2xlarge_sequential_read.csv","Sequential read",ms=True)
plt.legend()
plt.grid(axis='y',linestyle='dotted',linewidth=2)
plt.xlim(-1,400)
plt.savefig(f"sequential_read.png")
plt.show()

COLOR='black'
# -- Sequential write -- #
graph("KVM on Android","kvm/fio_KVM-App_sequential_write.csv","Sequential write",ms=True)
#graph("t4g.small","t4gsmall/fio_AWS-t4g.small_sequential_write.csv","Sequential write",ms=True)
graph("t4g.2xlarge","t4g2xlarge/fio_AWS-t4g.2xlarge_sequential_write.csv","Sequential write",ms=True)
plt.legend()
plt.grid(axis='y',linestyle='dotted',linewidth=2)
plt.xlim(-1,400)
plt.savefig(f"sequential_write.png")
plt.show()
