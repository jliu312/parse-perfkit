#!/bin/bash
powerstat -z -d 0 0.5 960 >> 20_pstat8.out &
sleep 10;
yes > /dev/null & sudo cpulimit -p $! --limit 20 &
yes > /dev/null & sudo cpulimit -p $! --limit 20 &
yes > /dev/null & sudo cpulimit -p $! --limit 20 &
yes > /dev/null & sudo cpulimit -p $! --limit 20 &
yes > /dev/null & sudo cpulimit -p $! --limit 20 &
yes > /dev/null & sudo cpulimit -p $! --limit 20 &
yes > /dev/null & sudo cpulimit -p $! --limit 20 &
yes > /dev/null & sudo cpulimit -p $! --limit 20 & sleep 180;
pkill yes;
sleep 10;

powerstat -z -d 0 0.5 960 >> 40_pstat8.out &
sleep 10;
yes > /dev/null & sudo cpulimit -p $! --limit 40 &
yes > /dev/null & sudo cpulimit -p $! --limit 40 &
yes > /dev/null & sudo cpulimit -p $! --limit 40 &
yes > /dev/null & sudo cpulimit -p $! --limit 40 &
yes > /dev/null & sudo cpulimit -p $! --limit 40 &
yes > /dev/null & sudo cpulimit -p $! --limit 40 &
yes > /dev/null & sudo cpulimit -p $! --limit 40 &
yes > /dev/null & sudo cpulimit -p $! --limit 40 & sleep 180;
pkill yes;
sleep 10;

powerstat -z -d 0 0.5 960 >> 60_pstat8.out &
sleep 10;
yes > /dev/null & sudo cpulimit -p $! --limit 60 &
yes > /dev/null & sudo cpulimit -p $! --limit 60 &
yes > /dev/null & sudo cpulimit -p $! --limit 60 &
yes > /dev/null & sudo cpulimit -p $! --limit 60 &
yes > /dev/null & sudo cpulimit -p $! --limit 60 &
yes > /dev/null & sudo cpulimit -p $! --limit 60 &
yes > /dev/null & sudo cpulimit -p $! --limit 60 &
yes > /dev/null & sudo cpulimit -p $! --limit 60 & sleep 180;
pkill yes;
sleep 10;

powerstat -z -d 0 0.5 960 >> 80_pstat8.out &
sleep 10;
yes > /dev/null & sudo cpulimit -p $! --limit 80 &
yes > /dev/null & sudo cpulimit -p $! --limit 80 &
yes > /dev/null & sudo cpulimit -p $! --limit 80 &
yes > /dev/null & sudo cpulimit -p $! --limit 80 &
yes > /dev/null & sudo cpulimit -p $! --limit 80 &
yes > /dev/null & sudo cpulimit -p $! --limit 80 &
yes > /dev/null & sudo cpulimit -p $! --limit 80 &
yes > /dev/null & sudo cpulimit -p $! --limit 80 & sleep 180;
pkill yes;
sleep 10;

powerstat -z -d 0 0.5 960 >> 100_pstat8.out &
sleep 10;
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 & sleep 180;
pkill yes;
sleep 10;
