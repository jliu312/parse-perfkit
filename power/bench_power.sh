#!/bin/bash

echo '--- begin idle-ish ---'
sleep 60
echo '--- end idle-ish ---'

echo '--- begin 10% cpu ---'
yes > /dev/null & sudo cpulimit -p $! --limit 10 &
yes > /dev/null & sudo cpulimit -p $! --limit 10 &
yes > /dev/null & sudo cpulimit -p $! --limit 10 &
yes > /dev/null & sudo cpulimit -p $! --limit 10 &
yes > /dev/null & sudo cpulimit -p $! --limit 10 &
yes > /dev/null & sudo cpulimit -p $! --limit 10 &
yes > /dev/null & sudo cpulimit -p $! --limit 10 &
yes > /dev/null & sudo cpulimit -p $! --limit 10 & sleep 60;
echo '--- end 10% cpu, wait 10s ---'
pkill yes;
sleep 10;

echo '--- begin 50% cpu ---'
yes > /dev/null & sudo cpulimit -p $! --limit 50 &
yes > /dev/null & sudo cpulimit -p $! --limit 50 &
yes > /dev/null & sudo cpulimit -p $! --limit 50 &
yes > /dev/null & sudo cpulimit -p $! --limit 50 &
yes > /dev/null & sudo cpulimit -p $! --limit 50 &
yes > /dev/null & sudo cpulimit -p $! --limit 50 &
yes > /dev/null & sudo cpulimit -p $! --limit 50 &
yes > /dev/null & sudo cpulimit -p $! --limit 50 & sleep 60;
echo '--- end 50% cpu, wait 10s ---'
pkill yes;
sleep 10;

echo '--- begin 100% cpu ---'
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 &
yes > /dev/null & sudo cpulimit -p $! --limit 100 & sleep 60;
echo '--- end 100% cpu, wait 10s ---'
pkill yes;
sleep 10;
