#http://webhacking.kr/challenge/web/web-05/
'''
---설명---
JOIN 과 LOGIN이 있으나 로그인만 가능
url : http://webhacking.kr/challenge/web/web-05/mem/ 로 이동하면 로그인 스크립트 존재
해당 파일을 다운로드하면 join.php 소스가 난독화가 되어 있는 것을 확인
1. 구글크롬 개발자 모드를 활용하여 변수를 선언하고 대입하면 난독화를 쉽게 바꿀 수 있다.
2. 정상소스를 보면 cookie phpssessid 변수에 oldzombiea 문자포함 때문에 쿠키변조
3. URL내에 mode=1이여야 하므로 URL내 추가 : http://webhacking.kr/challenge/web/web-05/mem/join.php?mode=1
4. admin%20 및 원하는 패스워드를 넣고 회원가입(개발자도구로 글자수 제한 늘리기)
5. login.php 에서 가입한 정보로 로그인 (계정명:admin)
'''

#난독화된 소스
ord='''<html>
<title>Challenge 5</title></head><body bgcolor=black><center>
<script>
l='a';ll='b';lll='c';llll='d';lllll='e';llllll='f';lllllll='g';llllllll='h';lllllllll='i';llllllllll='j';lllllllllll='k';llllllllllll='l';lllllllllllll='m';llllllllllllll='n';lllllllllllllll='o';llllllllllllllll='p';lllllllllllllllll='q';llllllllllllllllll='r';lllllllllllllllllll='s';llllllllllllllllllll='t';lllllllllllllllllllll='u';llllllllllllllllllllll='v';lllllllllllllllllllllll='w';llllllllllllllllllllllll='x';lllllllllllllllllllllllll='y';llllllllllllllllllllllllll='z';I='1';II='2';III='3';IIII='4';IIIII='5';IIIIII='6';IIIIIII='7';IIIIIIII='8';IIIIIIIII='9';IIIIIIIIII='0';li='.';ii='<';iii='>';lIllIllIllIllIllIllIllIllIllIl=lllllllllllllll+llllllllllll+llll+llllllllllllllllllllllllll+lllllllllllllll+lllllllllllll+ll+lllllllll+lllll;
lIIIIIIIIIIIIIIIIIIl=llll+lllllllllllllll+lll+lllllllllllllllllllll+lllllllllllll+lllll+llllllllllllll+llllllllllllllllllll+li+lll+lllllllllllllll+lllllllllllllll+lllllllllll+lllllllll+lllll;if(eval(lIIIIIIIIIIIIIIIIIIl).indexOf(lIllIllIllIllIllIllIllIllIllIl)==-1) { bye; }if(eval(llll+lllllllllllllll+lll+lllllllllllllllllllll+lllllllllllll+lllll+llllllllllllll+llllllllllllllllllll+li+'U'+'R'+'L').indexOf(lllllllllllll+lllllllllllllll+llll+lllll+'='+I)==-1){alert('access_denied');history.go(-1);}else{document.write('<font size=2 color=white>Join</font><p>');document.write('.<p>.<p>.<p>.<p>.<p>');document.write('<form method=post action='+llllllllll+lllllllllllllll+lllllllll+llllllllllllll+li+llllllllllllllll+llllllll+llllllllllllllll
+'>');
document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name='+lllllllll+llll+' maxlength=5></td></tr>');document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name='+llllllllllllllll+lllllllllllllllllllllll+' maxlength=10></td></tr>');document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');}
</script>
</body>
</html>'''
#정상 소스
new='''
<html>
<title>Challenge 5</title></head><body bgcolor=black><center>
<script>
if(eval(document.cookie).indexOf(oldzombie)==-1){
    bye;
}
if(eval(document.URL).indexOf(mode=1)==-1){
alert('access_denied');
history.go(-1);
}else{
    document.write('<font size=2 color=white>Join</font><p>');
    document.write('.<p>.<p>.<p>.<p>.<p>');
    document.write('<form method=post action=join.php>');
    document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name=id maxlength=5></td></tr>');
    document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name=pw maxlength=10></td></tr>');
    document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');}
</script>
</body>
</html>
'''