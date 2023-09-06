import json
import sys

fname = sys.argv[1]

with open(f"{fname}.json") as jf:
    obj = json.load(jf)
    jobs = obj['jobs']
    for job in jobs:
        print(job['jobname'])
        # if job['jobname']=='sequential_write':
        #     print(job.keys())
            
