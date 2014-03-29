#-*- coding: utf-8 -*-


import requests
import sys
import time
import datetime
import lxml.html as H

TAOBAO_REQ_URL = 'http://suggest.taobao.com/sug'
YHD_REQ_URL = 'http://www.yhd.com/ctg/get_new_keywords.do'
YHDXPATH = '//ul[1]/li/a/span/text()'

def getTaobao(word,retry = 3):
    time.sleep(3)
    if --retry > 0:
       try:
            par = {'code' : 'utf-8', 'q' : word }
            req = requests.get(TAOBAO_REQ_URL,params = par)
            if req.status_code != requests.codes.ok:
                yield getTaobao(word,--retry)
            ans = req.json()[u'result']
            for words in ans:
                yield words[0]
       except Exception as err:
            sys.stderr.write("%s:ERR:%s " % (datetime.datetime.now(),err))
    else:
        sys.stderr.write("%s:Get %s wrong" % (datetime.datetime.now(),word.encode('utf-8','ignore')))


def main():
    if len(sys.argv) != 3:
        print "Usage :python %s querryFile skipNum 1> outFile 2> logFile" % sys.argv[0]
        exit(1)
    count = 0
    with open(sys.argv[1],'r') as myInput:
        for line in myInput:
            line = line.strip('\r\n')
            if len(line) == 0:
                continue
            line = line.decode('utf-8','ignore')
            count += 1
            if(count < int(sys.argv[2])):
                continue
            if(count % 10 == 0):
                sys.stderr.write("%s:Doing %d %s\n" % (datetime.datetime.now(),count,line.encode('utf-8')))
            try:
                words = getTaobao(line)
                for word in words:
                    print word.encode('utf-8','ignore')
            except Exception as err:
                sys.stderr.write("%s:ERR:%s " % (datetime.datetime.now(),err))




if __name__ == "__main__":
    main()

