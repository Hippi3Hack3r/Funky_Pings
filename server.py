from scapy.all import *
from multiprocessing import Process

SESSION_ID = int(1028)

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
    sequence = 1
    while 1:
        response = input("\n> ")
        icmp_send('127.0.0.1', response, sequence)
        sequence += 1
        sequence = sequence % 128
