#!/usr/bin/env python
import sys, xmlrpclib, csv

# activate the API in your interface
# change the following line, this APIKEY is a fake key
APIKEY = '58WVkXfh2i84F3g39jTJuwVU'
# set the domain name information
domain = 'mydomainname.com'

# here is the production api. the development url is https://rpc.ote.gandi.net/xmlrpc/
api = xmlrpclib.ServerProxy("https://rpc.gandi.net/xmlrpc/");

reader = csv.reader(open("accounts.csv","rb"))

for row in reader:
    try:
        params = {'password': row[1]}
        create_mail = api.domain.mailbox.create(APIKEY, domain, row[0], params)
    except:
        print 'error while creating account'
