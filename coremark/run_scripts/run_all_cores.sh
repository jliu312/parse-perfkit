#!/bin/sh
make REBUILD=1 ITERATIONS=1000000 XCFLAGS="-DMULTITHREAD=1 -DUSE_PTHREAD -DPERFORMANCE_RUN=1"
for i in 0 1 2 3 4 5 6 7
do
    taskset -c $i ./coremark.exe > out_core$i.log
    sleep 10
done
