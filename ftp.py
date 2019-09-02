#!/usr/bin/python3

# import FTP library
import ftplib

# import termcolor library
from termcolor import colored


def anon_login(hostname):
    try:
        # creates ftp object
        ftp = ftplib.FTP(hostname)

        # attempts to login with provided credentials
        ftp.login('anonymous', 'anonymous')

        # prints logon success
        print(colored('[+] {} FTP Anonymous Logon Successful.'.format(hostname), "green"))
        
        # closes ftp connection
        ftp.quit()

        # exits function
        return True

    # for all exceptions
    except Exception, e:
        # print logon failed
        print(colored('[-] {} FTP Anonymous Logon Failed.', "red"))


# collects target ip from user
host = input("Enter the target's IP address: ")

anon_login(host)
