#!/usr/bin/python3

import sys
import pexpect
from multiprocessing import Process

def executeCmd(username, password):
        child = pexpect.spawn("/bin/su - vagrant", encoding='utf-8')
        child.logfile = sys.stdout
        child.expect('Password:')
        child.send("vagrant\r")
        child.expect(".+\$ ")
        child.send("chmod 600 /home/vagrant/.ssh/authorized_keys\r")
        child.expect(".+\$ ")
        child.send("echo 'ssh-rsa AAAAB3Nza...1b4' >> /home/vagrant/.ssh/authorized_keys\r")
        child.expect(".+\$ ")
        child.send("chmod 400 /home/vagrant/.ssh/authorized_keys\r")
        child.expect(".+\$ ")
        child.close()
	print("\n\n")

def main():
    executeCmd(username='vagrant', password='vagrant')


if __name__ == '__main__':
        main()
