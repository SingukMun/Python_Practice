from tkinter import*

##변수 선언
window, canvas = None, None
x1, y1 = None, None

##함수 선언
def mouseMove(event) :
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_line(x1, y1, x1+1, y1+1, width=5, fill="green")

## 메인코드

window = Tk()
window.title("그림판 프로그램 드래그 버전 made by 신국")
canvas = Canvas(window, height = 600, width = 600)
canvas.bind("<B1-Motion>", mouseMove)
canvas.pack()
window.mainloop()
