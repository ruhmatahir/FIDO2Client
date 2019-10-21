#!/usr/bin/expect -f
spawn fido2-cred -M -i cred_param /dev/hidraw0
expect "Enter PIN for /dev/hidraw0:" { send "12345678\r" }
interact
