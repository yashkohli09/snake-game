import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('lightgreen')
screen.setup(width=600, height=600)
screen.tracer(0)

snake_head = turtle.Turtle()
snake_head.color('blue')
snake_head.shape('square')
snake_head.penup()
snake_head.speed(0)
snake_head.direction = 'stop'

snake_body = []

snake_food = turtle.Turtle()
snake_food.color('red')
snake_food.shape('circle')
snake_food.penup()
snake_food.speed(0)
snake_food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.up()
pen.hideturtle()
pen.goto(0, 260)
pen.write('SCORE: 0\tHIGH SCORE: 0', align = 'center', font = ('Courier', 24, 'normal')) 

def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'

def go_down():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'

def go_left():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'

def go_right():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

def move():
    
    if snake_head.direction == 'up':
        snake_head.sety(snake_head.ycor() + 20)

    if snake_head.direction == 'down':
        snake_head.sety(snake_head.ycor() - 20)

    if snake_head.direction == 'left':
        snake_head.setx(snake_head.xcor() - 20)

    if snake_head.direction == 'right':
        snake_head.setx(snake_head.xcor() + 20)

turtle.listen()
turtle.onkeypress(go_left, 'Left')
turtle.onkeypress(go_right, 'Right')
turtle.onkeypress(go_up, 'Up')
turtle.onkeypress(go_down, 'Down')

while True:

    screen.update()

    if (snake_head.xcor() > 290) or (snake_head.xcor() < -290) or (snake_head.ycor() > 290) or (snake_head.ycor() < -290):
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = 'stop'

        for i in snake_body:
            i.goto(1000,1000)

        snake_body.clear()

        score = 0
        
        pen.clear()
        pen.write('SCORE: {}\tHIGH SCORE: {}'.format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))

        delay = 0.1

    if snake_head.distance(snake_food) < 20:
        score += 1
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snake_food.goto(x,y)

        body = turtle.Turtle()
        body.speed(0)
        body.shape('square')
        body.color('grey')
        body.penup()
        snake_body.append(body)

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write('SCORE: {}\tHIGH SCORE: {}'.format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))

        delay -= 0.001

    for i in range(len(snake_body)-1, 0, -1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].goto(x, y)

    if len(snake_body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x, y)

    move()

    for i in snake_body:
        if(i.distance(snake_head) < 20):
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = 'stop'

            for i in snake_body:
                i.goto(1000,1000)

            snake_body.clear()
            
    time.sleep(delay)

screen.mainloop()
