coffee = 0
coffee = int(input("어떤 음료를 원하나요? (1: 아메리카노, 2: 카페라떼, 3:아이스티):"))

print()
print("# 1. 물을 준비한다.");
print("# 2. 종이컵을 준비한다.");

if coffee == 1 :
    print("# 3. 원두를 간다")
    print("# 4. 물을 탄다.")
elif coffee == 2 :
    print("# 3. 원두를 간다")
    print("# 4. 우유를 탄다.")
elif coffee == 3 :
    print("# 3. 아이스티가루를 탄다.")
    print("# 4. 물을 탄다.")
else :
    print("# 3. 아무거나 탄다.")
    print("# 4. 물을 탄다.\n")

print("# 5. 스푼으로 저어서 녹인다");
print()
print("주문하신 음료 나왔습니다~~!!");
