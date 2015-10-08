#!/usr/bin/env python
# MIT License, (c) Chris Pates chris@pates.me.uk
# https://github.com/chrispates/httpsverify
import sys
import requests

def usage():
    print "Usage: httpsverify.py [OPTIONS] [URL]"
    print "-c ca.pem - use supplied certificate authority pem file for verification."

if __name__ == '__main__':

    opt_ca_pem = None
    opt_url = None

    if len(sys.argv) == 1:
        usage()
        sys.exit(0)

    args = sys.argv[1:]
    it = iter(args)
    for i in it:
        if i == '-c':
            opt_ca_pem = next(it)
            continue
        else:
            opt_url = i

    if opt_ca_pem:
	response = requests.get(opt_url, verify=True, cert=opt_ca_pem)
    else:
	response = requests.get(opt_url, verify=True)
	
print(response.status_code)
