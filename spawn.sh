#!/usr/bin/expect

set size [lindex $argv 0];
set token [lindex $argv 1];

cd ./meson-linux-amd64
spawn sudo ./meson service-install
expect "Please enter your token"
send "$token\r"

expect "Please enter your port,CAN NOT be 80 or 443(default 19091)"
send "\r"

expect "40GB disk space is the minimum, default will be 80GB. Please make sure you have enough free space"
send "$size\r"

expect eof
expect eof
