inStr, outStr = "", ""

inStr = input("문장을 입력하세요 : ")

for i in range(0, len(inStr)) :
    if inStr[i].isdigit() == False :
        outStr += inStr[i]

print("원 문자열 --> " + '[' + inStr + ']')
print("숫자 제거한 문자열 --> " + '['+outStr+']')
