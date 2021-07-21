## 변수 선언
money, coin500, coin100, coin50, coin10 = 0, 0, 0, 0, 0

##메인 코트
money = int(input("교환할 돈은 얼마 ? :"))

coin500 = money // 500
money = money % 500

coin100 = money // 100
money = money % 100

coin50 = money // 50
money = money %  50

coin10 = money // 10
money = money % 10

##출력부분
print(" 500원 짜리 동전 >> %d 개" % coin500)
print(" 100원 짜리 동전 >> %d 개" % coin100)
print(" 50원 짜리 동전 >> %d 개" % coin50)
print(" 10원 짜리 동전 >> %d 개" % coin10)
print(" 바꾸지 못한 잔돈 >> %d 원" % money)
