import turtle as t
from itertools import cycle

# 거북이 모양으로 변경
#t.shape('turtle')
# 가로 10 세로 20의 window 크기
#t.setup(10,20,0,0)
# 처음 turtle 커서가 위치하는 곳 지정 
# a, b는 x좌표 y좌표, 처음 위치는 0,0
# t.goto(a,b)
# 특정 코드로 그린 그림 지우기
# t.Screen().reset()

def go_origin():
    t.penup()
    t.goto(0,0)
    t.pendown()

def line(x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)


def turtleBar(data):
    t.Screen().reset()
    color = ['red','blue','orange','green','yellow']
    t.color('black')
    # 테두리 굵기
    t.pensize(1)
    index = 0
    # 축생성
    line(0,0,250,0)
    line(0,0,0,250)
    go_origin()
    # 눈금선
    # x축 눈금 그리기
    i=0
    while i<250:
        i+=25
        line(i,-5,i,5)
    go_origin()
    t.pensize(3)
    for h in data:
        t.fillcolor(color[index])
        index += 1
        t.begin_fill()
        # rising edge
        t.left(90)
        t.forward(h)
        t.right(90)
        t.forward(50)
        # 범례
        t.penup()
        t.forward(-25)
        t.write(str(h),align='center',font=('Times New Roman',15,'bold'))
        t.forward(+25)
        t.pendown()
        # falling edge
        t.right(90)
        t.forward(h)
        t.left(90)
        t.end_fill()

def turtlePie(data):
    t.Screen().reset()
    color = cycle(['red','blue','orange','green','yellow'])
    t.color('black')
    t.penup()
    # 초기 시작을 위해 반지름만큼 밑으로 펜을 위치
    t.sety(-200)
    s = sum(data)
    t.pendown()
    # 파이 차트
    for d in data:
        t.fillcolor(next(color))
        t.begin_fill()
        t.circle(200,360 * (d/s))
        # 현재 좌표를 point에 저장
        point = t.position()
        t.goto(0,0)
        t.end_fill()
        t.setposition(point)
    #범례
    t.penup()
    t.sety(-100)
    for d in data:
        t.circle(100, (360 * (d/s)) / 2)
        t.write(str(d), align="center", font=('Times New Roman',15,'bold'))
        t.circle(100, (360 * (d/s)) / 2)

data = [10,20,30,20,10]
turtleBar(data)
turtlePie(data)
# 창 닫힘방지
t.exitonclick()


