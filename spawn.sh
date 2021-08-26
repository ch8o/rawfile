#!/usr/bin/expect

cd ./meson-linux-amd64
spawn sudo ./meson service-install
expect "Please enter your token"
send "p1LjdTyqASPMVTNo6MKR+w==\r"

expect "Please enter your port,CAN NOT be 80 or 443(default 19091)"
send "\r"

set size [lindex $argv 0];
expect "40GB disk space is the minimum, default will be 80GB. Please make sure you have enough free space"
send "$size\r"

expect eof
expect eof
