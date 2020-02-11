import requests

headers={'Content-Type':'application/x-www-form-urlencoded'}
def check(url):
    try:
        rep1=requests.get(url,headers=headers,allow_redirects=False)
        if rep1.status_code==200:
            print url+'      yes'
    except Exception,e:
        pass
test=0
with open('hello_world.txt','r') as f:
    for i in f.readlines():
        test+=1
        url=i.strip('\n')
        test_url_1=url+'/include/config.properties'
        check(test_url_1)
