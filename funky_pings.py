
# Written by Hannah Cartier hcartier@activecountermeasures.com
# this script generated an icmp beacon using Echo requests
# the payload can be configured with a random string (-r) and a random size (-s size)
# or can be made to send a custom message
from scapy.all import *
import time, os, random
import string
import argparse


interval = 2 # time between ping in seconds
payload_len = 32  #MAX 1472 bytes
rand = False

def send_random():
    _seq = 1
    while True:
        payload = ''.join(random.choice(string.ascii_lowercase) for _ in range(payload_len))
        icmp_send(payload)

def send_data():
    _seq = 1
    while True:
        payload = input("enter message > ")
        payload_len = len(payload)
        icmp_send(payload)

def icmp_send(payload):
    _seq = 1
    send(IP(dst=addr)/ICMP(type="echo-request", id=0x0001, seq=_seq)/payload)
    time.sleep(interval)
    _seq += 1
    _seq = _seq % 128


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Passer version ')
    parser.add_argument('-a', '--address', help='ip address to send packets too', required=False, default="157.230.93.100")
    parser.add_argument('-s', '--size', help='payload size for beacon', required=False, default=32)
    parser.add_argument('-r', '--random', action='store_true', help='payload size for beacon', required=False, default=False)
    (parsed, unparsed) = parser.parse_known_args()
    args = vars(parsed)
    addr = args['address']
    payload_len = args['size']
    if args['random']:
        send_random()
    else:
        send_data()
