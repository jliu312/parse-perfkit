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

def logit(x):
    return [math.log2(i) for i in x]

def graph(rw):
    fig=plt.gcf()
    fig.set_size_inches(12,8)
    
    kvm_df = pd.read_csv(f"lmbench_kvm_{rw}.csv")
    native_df = pd.read_csv(f"lmbench_native_{rw}.csv")
    t4g2xl_df = pd.read_csv(f"lmbench_t4g2xlarge_{rw}.csv")
    kvm2_df = pd.read_csv(f"lmbench_kvm2_{rw}.csv")
    pix3_df = pd.read_csv(f"lmbench_pixel3a_{rw}.csv")

    
    plt.plot(logit(pix3_df["Index"]),pix3_df["Latency"],label="Pixel 3a",color=colors[1],linewidth=4)
    plt.scatter(logit(pix3_df["Index"]),pix3_df["Latency"],color=colors[1])

    plt.plot(logit(list(t4g2xl_df["Index"])[:-1]),list(t4g2xl_df["Latency"])[:-1],label="t4g.2xlarge",color=colors[3],linewidth=4)
    plt.scatter(logit(list(t4g2xl_df["Index"])[:-1]),list(t4g2xl_df["Latency"])[:-1],color=colors[3])
        
    plt.plot(logit(native_df["Index"]),native_df["Latency"],label="6a-Native", color=colors[0],linewidth=4)
    plt.scatter(logit(native_df["Index"]),native_df["Latency"],color=colors[0])

    plt.plot(logit(kvm2_df["Index"]),kvm2_df["Latency"],label="6a-KVM-LXD",color='black',linewidth=4)
    plt.scatter(logit(kvm2_df["Index"]),kvm2_df["Latency"],color='black')    
    
    plt.plot(logit(kvm_df["Index"]),kvm_df["Latency"],label="6a-KVM",color=colors[2],linewidth=4)
    plt.scatter(logit(kvm_df["Index"]),kvm_df["Latency"],color=colors[2])
    
    
    plt.grid(linestyle="dotted",linewidth=2)
    #plt.title(f"{rw}")
    plt.xlabel("Array size (MB) log scale")
    plt.ylabel("Latency (ns)") #maybe
    plt.legend()
    ax = plt.gca()
    xlabels=[-11,-9,-7,-5,-3,-1,1,3,5,7,9,11]
    nicelabels=[r'$\frac{1}{2048}$',r'$\frac{1}{512}$',r'$\frac{1}{128}$',r'$\frac{1}{32}$',r'$\frac{1}{8}$',r'$\frac{1}{2}$',2,8,32,128,512,2048]
    ax.set_xticks(xlabels,labels=nicelabels)
    plt.tight_layout()
    plt.savefig(f"lmbench_latency_{rw}.png")
    plt.show()

graph("loadlat")
graph("randlat")
    
