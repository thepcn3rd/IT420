#!/usr/bin/python3

import sys
import getopt

# Example execution
# ./buildList.py -i userlist.txt -d windomain.local

def main():
    inputfile = ''
    # Read the argument for the userlist file and the domain to append
    if len(sys.argv) < 2:
        print("./buildList.py -i --userlist-- -d --domain--")
        exit(1)
    else:
        argv = sys.argv[1:]
        opts, argv = getopt.getopt(argv,"i:d:")
        for opt, arg in opts:
            if opt in ['-i']:
                inputfile = arg
            if opt in ['-d']:
                domain = arg
        # Read in the file from the command line options...
        with open(inputfile) as f:
            for line in f:
                firstname, lastname = line.split(" ")
                firstname = firstname.lower()
                lastname = lastname.lower().strip()
                # first.last
                print(firstname + "." + lastname + "@" + domain)
                # first_last
                print(firstname + "_" + lastname + "@" + domain)
                # f.last
                print(firstname[0:1] + "." + lastname + "@" + domain)
                # first.l
                print(firstname + "." + lastname[0:1] + "@" + domain)

if __name__ == '__main__':
    main()

