ss=input("문자열을 입력하세요 -->")

print(ss.replace('o','$'))


ss2 = input("문자열을 또 입력하세요 -->")
print("출력할 문자열 -->", end = '')
for i in range(0, len(ss2)) :
    if ss2[i] != 'o' :
        print(ss[i], end= '')
    else :
        print('$', end= '')
