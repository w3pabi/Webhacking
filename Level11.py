#http://webhacking.kr/challenge/codeing/code2.html
'''
---설명---
if(preg_match($pat,$_GET[val])) { echo("Password is ????"); }
위 문구 확인하면 $pat 과 val 값이 같으면 됨
url주소에 ?val=pat 데이터를 표현하면 됨
$pat="/[1-3][a-f]{5}_.*59.4.217.166.*\tp\ta\ts\ts/";
'''

import urllib.request

phpsessid = "805defb40aabf56fc3bdc3336a183499"
url="http://webhacking.kr/challenge/codeing/code2.html"

req=urllib.request.Request(url)
req.add_header('Cookie', "PHPSESSID=%s" % (phpsessid))
html=urllib.request.urlopen(req).read().decode('ISO-8859-1')

# ip가져오기
rw1=html.find('.*')
rw2=html.find('.*',rw1+1)
ip=html[rw1+2:rw2]

# val 조건
query="?val=1aaaaa_"+ip+"%09p%09a%09s%09s"

# val값 집어 넣기
req=urllib.request.Request(url+query)
req.add_header('Cookie', "PHPSESSID=%s" % (phpsessid))
html=urllib.request.urlopen(req).read().decode('ISO-8859-1')
print(html)
