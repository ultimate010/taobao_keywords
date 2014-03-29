#-*- coding: utf-8 -*-


import requests
import sys
import time
import lxml.html as H

TAOBAO_REQ_URL = 'http://suggest.taobao.com/sug'
YHD_REQ_URL = 'http://www.yhd.com/ctg/get_new_keywords.do'
YHDXPATH = '//ul[1]/li/a/span/text()'

def getYHD(word,retry = 3):
    time.sleep(3)
    if --retry > 0:
        par = {'keyword' : word }
        try:
            req = requests.get(YHD_REQ_URL,params = par)
            if req.status_code != requests.codes.ok:
                yield getYHD(word,--retry)
            ans = req.json()[u'value']
            #print ans.encode('utf-8')
            dom_words = H.fromstring(ans)
            html_words = dom_words.xpath(YHDXPATH)
            for word in html_words:
                yield word
        except Exception as err:
            sys.stderr.write("ERR:%s " % err.encode('utf-8'))
    else:
        sys.stderr.write("Get %s wrong" % word.encode('utf-8','ignore'))

def main():
    if len(sys.argv) != 2:
        print "Usage :python %s querryFile 1> outFile 2> logFile" % sys.argv[0]
        exit(1)
    count = 0
    with open(sys.argv[1],'r') as myInput:
        for line in myInput:
            line = line.strip('\r\n')
            if len(line) == 0:
                continue
            line = line.decode('utf-8','ignore')
            count += 1
            if(count % 10 == 0):
                sys.stderr.write("Doing %d %s\n" % (count,line.encode('utf-8')))
            words = getYHD(line)
            for word in words:
                print word.encode('utf-8','ignore')



if __name__ == "__main__":
    main()

