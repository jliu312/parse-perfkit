make REBUILD=1 ITERATIONS=1000000 XCFLAGS="-DMULTITHREAD=8 -DUSE_PTHREAD -DPERFORMANCE_RUN=1"
mv run1.log run1_multi.log
mv run2.log run2_multi.log
make REBUILD=1 ITERATIONS=1000000 XCFLAGS="-DMULTITHREAD=1 -DUSE_PTHREAD -DPERFORMANCE_RUN=1"
mv run1.log run1_single.log
mv run2.log run2_single.log
