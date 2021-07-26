##변수 선언
i, k, heartNum, numStr, ch, heartStr = 0, 0, 0, "", "", ""

##메인 코드
numStr = input("숫자를 여러개 입력하시오 : ")
print("")

i = 0
ch = numStr[i]
while True :
    heartNum = int(ch)

    heartStr = ""
    for k in range (0, heartNum):
        heartStr += "\u2665"

    print(heartStr)

    i = i + 1
    if (i>len(numStr)-1) :
        break

    ch = numStr[i]
