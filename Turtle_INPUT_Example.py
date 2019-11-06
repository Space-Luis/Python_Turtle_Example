import turtle

turtle.bgcolor("black") #배경의 색깔을 검은색으로 변경

t = turtle.Turtle()

t.shape("turtle")
t.color("yellow")

t.speed(0) # 거북이의 이동속도를 최대로 지정

d = 5 #거북이의 이동거리

Angle = turtle.textinput("거북이의 예술","거북이가 꺽을 각도를 입력하세요.")
for i in range(200):
    if i%4 == 0:
        t.color("red")

    elif i%4 == 1:
        t.color("yellow")

    elif i%4 == 2:
        t.color("blue")

    elif i%4 == 3:
        t.color("green")

    t.forward(d)
    t.rt(89)
    d = d+5
