inStr = ""
outStr = ""

inStr = input("띄어쓰기가 가득 들어있는 문자열을 입력하세요 : ")
for i in range(0, len(inStr)):
    if inStr[i] != ' ' :
        outStr += inStr[i]

print("원래의 문자열 --> " + "[" + inStr + "]")
print("공백을 제거한 문자열 --> " + "[" + outStr + "]")
