#!/bin/bash
  
destip=$1
if [ -z "$destip" ]
then
       echo 'arg1: destip'
       exit -1
fi
cmd="
sudo wget 'https://raw.githubusercontent.com/ch8o/rawfile/main/meson.sh'
sudo wget 'https://raw.githubusercontent.com/ch8o/rawfile/main/spawn.sh'

sudo chmod +x meson.sh
sudo chmod +x spawn.sh

sudo ./meson.sh 80 ！！！[meson-token]！！！
"
echo $cmd

ssh -o StrictHostKeyChecking=no -i aws.key root@$destip "$cmd"
