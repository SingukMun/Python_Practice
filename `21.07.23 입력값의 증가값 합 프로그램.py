i, hap = 0, 0
num1, num2, num3 = 0, 0, 0

num1 = int(input("시작값을 입력하시오 : "))
num2 = int(input("끝값을 입력하시오 : "))
num3 = int(input("증가할 값을 입력하시오 : "))

for i in range(num1, num2+1, num3):
    hap += i

print("%d 에서 %d 까지 %d 씩 증가한 값의 합은 %d 입니다." % (num1, num2, num3, hap))
