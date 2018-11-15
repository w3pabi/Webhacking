#http://webhacking.kr/challenge/web/web-04/

'''
---설명---
해결해야 할코드 : YzQwMzNiZmY5NGI1NjdhMTkwZTMzZmFhNTUxZjQxMWNhZWY0NDRmMg==
암호 문제
base64 와 sha-1 문제
'''

#해쉬는 복호화 할 수 없으므로 복호화 사이트에서 해야 하나 코드를 역순으로 돌려봄
import base64
import hashlib

encrypted1=hashlib.sha1(b'test')
print(encrypted1.hexdigest())

encrypted2=hashlib.sha1(b'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3')
print(encrypted2.hexdigest())

encrypted3=base64.b64encode(b'c4033bff94b567a190e33faa551f411caef444f2')
print(encrypted3)


