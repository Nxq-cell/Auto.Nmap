#!/usr/bin/python3

import nmap, os, sys, time
from os import system, name
from time import gmtime, strftime

example = "\n\033[1;37m[\033[1;32mexample\033[1;37m]\033[1;37m 163.532.353.1 / 163.532.353.1-30 / 163.532.353.1,22,33 / 163.532.353.1/24\033\n"
back = "\033[1;37m[\033[1;32mback\033[1;37m]\033[1;37m ctrl+C\033"

def logo():
    print(""" \033[1;32m
 ▄▀█ █░█ ▀█▀ █▀█ ░ █▄░█ █▀▄▀█ ▄▀█ █▀█
 █▀█ █▄█ ░█░ █▄█ ▄ █░▀█ █░▀░█ █▀█ █▀▀ v1.0.beta
           coded by Nxq\033[1;m""")
 
 
def menu():
    print("\n\033[1;32m[\033[1;37m1\033[1;32m]\033[1;37m Regular \033")

    print("\033[1;32m[\033[1;37m2\033[1;32m]\033[1;37m Intense \033")
    
    print("\033[1;32m[\033[1;37m3\033[1;32m]\033[1;37m ping \033")
    
    print("\033[1;32m[\033[1;37m4\033[1;32m]\033[1;37m quick \033")
    
    print("\033[1;32m[\033[1;37m5\033[1;32m]\033[1;37m quickplus [root]\033")
    
    print("\033[1;32m[\033[1;37m0\033[1;32m]\033[1;37m exit\033\n")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def interrup():
    clear()
    print("\n")
    print("\033[0m[\033[1;31m!\033[0m]\033[1;0m User Interruption Detected..!")
    time.sleep(1)


def regular():

    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033[0m").lower()
    clear()
    print("\033[0m[\033[1;32mregular\033[0m]\033[0m ")
    print("\033[32m[~] Scanning: \033[0m" + target)
    print("Prossesing ....)\n")
    time.sleep(1)
    scanner = nmap.PortScanner()
    command = ("nmap " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = " logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[32m Nmap Version: \033[0m", scanner.nmap_version())
    
def intense():

    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033[0m").lower()
    clear()
    print("\033[0m[\033[1;32mintense\033[0m]\033[0m ")
    print("\033[32m[~] Scanning : \033[0m" + target)
    print("Prossesing ....\n")
    time.sleep(1)
    scanner = nmap.PortScanner()
    command = ("nmap -T4 -A -v " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = " logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[32mNmap Version: \033[0m", scanner.nmap_version())


def ping():

    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033[0m").lower()
    clear()
    print("\033[0m[\033[1;32mping\033[0m]\033[0m ")
    print("\033[32m[~] Scanning : \033[0m" + target)
    print("Prossesing ....\n")
    time.sleep(1)
    scanner = nmap.PortScanner()
    command = ("nmap -sn " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = " logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[32mNmap Version: \033[0m", scanner.nmap_version())


def quick():

    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033[0m").lower()
    clear()
    print("\033[0m[\033[1;32mquick\033[0m]\033[0m ")
    print("\033[32m[~] Scanning : \033[0m" + target)
    print("Prossesing ....\n")
    time.sleep(1)
    scanner = nmap.PortScanner()
    command = ("nmap -T4 -F " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = " logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[32mNmap Version: \033[0m", scanner.nmap_version())


def quickplus():

    target = input("\033[1;37m[\033[1;32m?\033[1;37m]\033[1;37m Enter Domain or IP Address: \033[0m").lower()
    clear()
    print("\033[0m[\033[1;32mquickplus\033[0m]\033[0m ")
    print("\033[32m[~] Scanning : \033[0m" + target)
    print("Prossesing ....\n")
    time.sleep(1)
    scanner = nmap.PortScanner()
    command = ("sudo nmap -sV -T4 -O -F --version-light " + target)
    process = os.popen(command)
    results = str(process.read())
    logPath = " logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    print(results + command + logPath)
    print("\033[32mNmap Version: \033[0m", scanner.nmap_version())


def exit():

    time.sleep(1)
    print("\n\033[1;32m Auto.nmap\033[0m Exiting... \033\n")
    sys.exit()


def fun():
    choice = ("1")
    clear()
    logo()

    while choice != ("0"):
    
        menu()
        choice = input("\033[0;37m[\033[1;32m+\033[0;37m]\033[1;37m Enter your choice \033[1;37m[\033[1;32mNUM\033[1;37m]:\033[1;m ")
        if choice == ("1"):
            try:
                print(back)
                print(example)
                regular()


            except KeyboardInterrupt:
                interrup()

        elif choice == ("2"):
            try:
                print(example)
                intense()

            except KeyboardInterrupt:
                back()

        elif choice == ("3"):
            try:
                print(example)
                print(back)
                ping()

            except KeyboardInterrupt:
                interrup()


        elif choice == ("4"):
            try:
                print(example)
                print(back)
                quick()

            except KeyboardInterrupt:
                interrup()

        elif choice == ("5"):
            try:
                print(example)
                print(back)
                quickplus()

            except KeyboardInterrupt:
                interrup()


        elif choice == ("0"):
            exit()
       
                  
        else:
            clear()
            logo()
            print("\n\t\033[5;31m[-] Invalid option..! \033[0m")
        
                                              
if __name__ == "__main__":
    fun()
