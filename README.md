**This is a work in progress**

This program can act as a simple chat server that sends messages over pings.
Or, if the server side enters a comand (ex: 'ls', 'whoami', 'reboot') The packet will be coded in such a way that the client will execute the command and return the results.
I have very little time, currently, any recognized command will just be interpreted as an 'ls'

The computer running the server must have its own public IP address

You will likely need to disable the OS's responses to pings on the server side  
`sysctl -w net.ipv4.icmp_echo_ignore_all=1`
