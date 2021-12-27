# Author: Hannah Cartier cartier.hannah@utah.edu
# 12/26/2021

# This file stores variables that are shared between the cllient and server
SESSION_ID = int(1028)
FIRST_SEQ = int(90)
RETURNED_DATA_SEQ = int(91)

cmdtable = dict({'reboot': (100, 'reboot'),
            'ls': (101, 'ls'),
             'ifconfig': (102, 'ifconfig'),
             'whoami': (103, 'whoami')})
