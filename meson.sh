#!/bin/bash

wget 'https://coldcdn.com/api/cdn/f2cobx/terminal/v2.5.1/meson-linux-amd64.tar.gz'
tar -zxf meson-linux-amd64.tar.gz

sudo apt-get update -y
sudo apt-get install -y expect

./spawn.sh $1
cd ./meson-linux-amd64
sudo ./meson service-start
sudo ./meson service-status
