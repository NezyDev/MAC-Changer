#mac address changer python script.
#made by NezyGhoul#8130

import subprocess 
import optparse
import re
import random
from random import randint, randrange

wifi = "wlan0"
cabel = "eth0"


def change_mac(interface, mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])
    print("[+] Succesfully Changed!")


def generate_mac():
    fir = random.randint(10, 90)
    sec = random.randint(10, 90)
    third = random.randint(10, 90)
    four = random.randint(10, 90)
    five = random.randint(10, 90)
    six = random.randint(10, 90)

    generated_mac = str(fir) + ":" + str(sec) + ":" + str(third) + ":" + str(four) + ":" + str(five) + ":" + str(six)
    return generated_mac


print("1-> MAC Custom")
print("2-> MAC Randomly")

choose = input("-> ")

if choose == "1":
    print("1-> WIFI Network")
    print("2-> Cabel Network")

    choose_var = input("-> ")

    if choose_var == "1":
        new_mac = input("Enter new MAC: ")
        
        try:
            change_mac(wifi, new_mac)
        except:
            print("[-] Something went wrong!")
    elif choose_var == "2":
        new_mac = input("Enter new MAC: ")
        
        try:
            change_mac(cabel, new_mac)
        except:
            print("[-] Something went wrong!")
    else:
        print("[-] Incorrect Keybind")
elif choose == "2":
    print("1-> WIFI Network")
    print("2-> Cabel Network")

    choose_var = input("-> ")

    if choose_var == "1":
        try:
            change_mac(wifi, generate_mac())
        except:
            print("[-] Something went wrong.")

    elif choose_var == "2":
        try:
            change_mac(cabel, generate_mac())
        except:
            print("[-] Something went wrong")
    else:
        print("[-] Incorrect keybind")
else:
    print("[-] Incorrect Keybind")
