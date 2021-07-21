##변수 선언
a, b, ch = 0, 0, ""

##메인 코드
a= int(input(" 첫 번째 수를 입력하세요 :"))
ch=input(" 계산할 연산자를 입력하세요 :")
b= int(input(" 첫 번째 수를 입력하세요 :"))

if ch == "+" :
    print("%d + %d = %d 입니다." % (a, b, a+b))
elif ch == "-" :
    print("%d - %d = %d 입니다." % (a, b, a-b))
elif ch == "*" :
    print("%d * %d = %d 입니다." % (a, b, a*b))
elif ch == "/" :
    print("%d / %d = %f 입니다." % (a, b, a/b))
##포매팅 연산자 %d와 %를 같이 사용할때는 연산자% 대신에 %%를 사용해준다
elif ch == "%" :
    print("%d %% %d = %d 입니다." % (a, b, a%b))
elif ch == "//" :
    print("%d // %d = %d 입니다." % (a, b, a//b))
elif ch == "**" :
    print("%d ** %d = %d 입니다." % (a, b, a**b))
else :
    print("알수 없는 연산자 입니다.")
