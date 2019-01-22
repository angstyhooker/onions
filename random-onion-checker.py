#!/usr/bin/python2

import socket
import socks
from random import choice
from threading import Thread, current_thread
from time import sleep

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

import httplib



def crawlOnionSpace():
    tn = 0
    nom = 0
    for x in xrange(0, 100000):
        nom = nom + 1
        a = "".join([choice('abcdefghijklmnopqrstuvwxyz234567') for n in xrange(16)])
        a = a + ".onion"
        #print "%i %i Connecting to: %s" % (tn, nom, a)
        try:
            params = ""
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5",}
            conn = httplib.HTTPConnection(a,timeout=5)
            conn.request("HEAD","/robots.txt",headers=headers)
            response = conn.getresponse()
            print "%i %i Success: %s - %i" % (tn, nom, a, response.status)
            with open('success.txt', 'a') as f:
                f.write(a + "\n")
        except (httplib.HTTPException, socket.error) as e:
            print "%i %i Failed: %s - %s" % (tn, nom, a, e)
            #with open('failed.txt', 'a') as f:
            #    f.write(a + "\n")

def main():
    connectTor()
    for i in xrange(0,16):
        t = Thread(target=crawlOnionSpace)
        t.daemon = True
        t.start()
        sleep(1)

    while True:
        #crawlOnionSpace()
        sleep(1)

if __name__ == "__main__":
    main()
