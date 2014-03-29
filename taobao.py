#-*- coding: utf-8 -*-


import requests
import sys
import time
import lxml.html as H

TAOBAO_REQ_URL = 'http://suggest.taobao.com/sug'
YHD_REQ_URL = 'http://www.yhd.com/ctg/get_new_keywords.do'
YHDXPATH = '//ul[1]/li/a/span/text()'

def getTaobao(word,retry = 3):
    time.sleep(1)
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
            sys.stderr.write("ERR:%s " % err)
    else:
        sys.stderr.write("Get %s wrong" % word.encode('utf-8','ignore'))


def main():
    if len(sys.argv) != 2:
        print "Usage :python %s querryFile 1> outFile 2> logFile" % sys.argv[0]
        exit(1)
    with open(sys.argv[1],'r') as myInput:
        for line in myInput:
            line = line.strip('\r\n')
            if len(line) == 0:
                continue
            words = getTaobao(line.decode('utf-8','ignore'))
            for word in words:
                print word.encode('utf-8','ignore')



if __name__ == "__main__":
    main()
