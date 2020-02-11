import requests

def check(url):
    try:
        rep=requests.get(url,allow_redirects=False)
        if rep.status_code==200:
            print url
    except Exception,e:
        pass
test=0
with open('1.txt','r') as f:
    for i in f.readlines():
        test+=1
        print test
        url=i.strip('\n')
        test_url_1=url+'/cmd.jsp'
        test_url_2=url+'/mtc.jsp'
        check(test_url_1)
        check(test_url_2)
        
