## 변수선언
drinks = { "소주" : "삼겹살", "맥주" : "치킨", "와인" : "치즈", "양주" : "과일"};

## 메인 코드
while(True) :
    mydrink = input(str(list(drinks.keys())) + " 중 좋아하는 것은?? : ")
    if mydrink in drinks :
        print(" %s 궁합주류는 %s 입니다." % (mydrink, drinks.get(mydrink)))
        print("프로그램을 종료하고 싶다면 ctrl + c를 누르시오")
    elif mydrink == "끝" :
        break
    else :
        print("그런 술은 없습니다. 다시확인해보세요.")
