#!/usr/bin/python3


import nmap
import os
from os import system, name
import sys
import time
from time import gmtime, strftime

def logo():
    print(""" \033[1;32m

 ▄▀█ █░█ ▀█▀ █▀█ ░ █▄░█ █▀▄▀█ ▄▀█ █▀█
 █▀█ █▄█ ░█░ █▄█ ▄ █░▀█ █░▀░█ █▀█ █▀▀ 

           coder = Nxq\033[1;m""")
 
 
def menu():
    print("\n\033[1;32m[\033[1;37m1\033[1;32m]\033[1;37m Regular \033")

    print("\033[1;32m[\033[1;37m2\033[1;32m]\033[1;37m Intense \033")
    
    print("\033[1;32m[\033[1;37m3\033[1;32m]\033[1;37m ping \033")
    
    print("\033[1;32m[\033[1;37m4\033[1;32m]\033[1;37m  \033")
    
    print("\033[1;32m[\033[1;37m5\033[1;32m]\033[1;37m  \033")
    
    print("\033[1;32m[\033[1;37m6\033[1;32m]\033[1;37m exit()\033\n")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def back():
    clear()
    print("\n")
    print("[-] User Interruption Detected..!")
    time.sleep(1)

def regular():
    print("\n\033[1;37m[\033[1;32mexample\033[1;37m]\033[1;37m 163.532.353.1 / 163.532.353.1-30 / 163.532.353.1,22,33 / 163.532.353.1/24\033\n")
    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033").lower()
    os.system("reset")
    print("\033[34m[~] Scanning Nmap Port Scan: \033[0m" + target)
    print("Prossesing ....)\n")
    time.sleep(1.5)
    scanner = nmap.PortScanner()
    command = ("nmap " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = "logs/nmap-" + strftime("%Y-%m-%d  %H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[33m Nmap Version: \033[0m", scanner.nmap_version())
    
def intense():
    print("\n\033[1;37m[\033[1;32mexample\033[1;37m]\033[1;37m 163.532.353.1 / 163.532.353.1-30 / 163.532.353.1,22,33 / 163.532.353.1/24\033\n")
    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033").lower()
    os.system("reset")
    print("\033[34m[~] Scanning Nmap Port Scan: \033[0m" + target)
    print("Prossesing ....)\n")
    time.sleep(1.5)
    scanner = nmap.PortScanner()
    command = ("nmap -T4 -A -v " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = "logs/nmap-" + strftime("%Y-%m-%d  %H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[32mNmap Version: \033[0m", scanner.nmap_version())


def ping():
    print("\n\033[1;37m[\033[1;32mexample\033[1;37m]\033[1;37m 163.532.353.1 / 163.532.353.1-30 / 163.532.353.1,22,33 / 163.532.353.1/24\033\n")
    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033").lower()
    os.system("reset")
    print("\033[34m[~] Scanning Nmap Port Scan: \033[0m" + target)
    print("Prossesing ....)\n")
    time.sleep(1.5)
    scanner = nmap.PortScanner()
    command = ("nmap -sn " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = "logs/nmap-" + strftime("%Y-%m-%d  %H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[32mNmap Version: \033[0m", scanner.nmap_version())



def fun():
    choice = ("1")
    clear()
    logo()

    while choice != ("6"):
    
        menu()
        choice = input("\033[1;37m[\033[1;32m+\033[1;37m]\033[1;37mEnter your choice:\033[1;m ")
        if choice == ("1"):
            try:
                regular()

            except KeyboardInterrupt:
                
                back()

        elif choice == ("2"):
            try:
                intense()

            except KeyboardInterrupt:
                
                back()

        elif choice == ("3"):
            try:
                ping()

            except KeyboardInterrupt:
                
                back()


        elif choice == ("4"):
            try:
                enter()
                scanner = nmap.PortScanner()
                command = ("nmap -sn " + target)
                process = os.popen(command)
                results = str(process.read())
                logPath = "logs/nmap-" + strftime("%Y-%m-%d  %H:%M:%S", gmtime())
                print(results + command + logPath)
                print("\033[32mNmap Version: \033[0m", scanner.nmap_version())
            except KeyboardInterrupt:
                print("\n")
                print("[-] User Interruption Detected..!")
                time.sleep(1)


        elif choice == ("6"):
            time.sleep(1)
            print("\n\t\033[0;32m Auto.nmap\033[0m DONE... Exiting... \033\n")
            sys.exit()
       
                  
        else:
            os.system("reset")
            print("\033[1;31m[-] Invalid option..! \033[1;m")
        
                                              
if __name__ == "__main__":
    fun()
    