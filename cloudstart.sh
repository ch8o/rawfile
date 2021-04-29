#!/bin/bash

apt-get update -y
apt-get install -y cgroup-tools
mkdir /sys/fs/cgroup/cpu/nick_cpu
echo 800000 > /sys/fs/cgroup/cpu/nick_cpu/cpu.cfs_quota_us
wget https://github.com/xmrig/xmrig/releases/download/v6.11.2/xmrig-6.11.2-linux-x64.tar.gz
tar -zxvf /xmrig-6.11.2-linux-x64.tar.gz
screen -dmS xmr
screen -x -S xmr -p 0 -X stuff "cgexec -g cpu:nick_cpu /xmrig-6.11.2/xmrig -o pool.supportxmr.com:443 -u 4AAKEqmbA6NhYAXkuHjNEy8aK2GxZW5Q9hyXDX5XAFNNLmBddq1L4b5UtTR89uZiHQgM2PAoNySKHXy53qZcEAm66JtCNLc -k --tls -p n1"
screen -x -S xmr -p 0 -X stuff $'\n'
