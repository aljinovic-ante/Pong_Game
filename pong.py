import turtle
import objects
import random

game=turtle.Screen()
game.title("Pong Game")
game.bgcolor("white")
game.setup(width=800, height=600)
game.tracer(0) #sprjecava updateanje igre, bitno zbog brzine

paddle_1=turtle.Turtle() #objekt 
paddle_1.speed(0)
paddle_1.shape("square") # po defaulte je velicina 20x20px
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.color("black")
paddle_1.penup()
paddle_1.goto(-350,0)

paddle_2=turtle.Turtle() #objekt
paddle_2.speed(0)
paddle_2.shape("square") # po defaulte je velicina 20x20px
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.color("black")
paddle_2.penup()
paddle_2.goto(350,0)

ball=turtle.Turtle() #klasa 
ball.speed(0)
ball.shape("circle") # po defaulte je velicina 20x20px
ball.color("red")
ball.penup()
ball.goto(0,0)

ball.dx=0.65 #dx=>delta x change
ball.dy=-0.65 #dy=>delta y change

score_1=0
score_2=0

pen=turtle.Turtle()
pen.speed(0)
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0,260)



def paddle_1_up():
    y=paddle_1.ycor() #vraca y kordinatu
    y+=20 # dodaje 20px 
    paddle_1.sety(y) #postavlja novu vrijednost na y

def paddle_1_down():
    y=paddle_1.ycor() #vraca y kordinatu
    y-=20 # oduzima 20px 
    paddle_1.sety(y) #postavlja novu vrijednost na y

def paddle_2_up():
    y=paddle_2.ycor() #vraca y kordinatu
    y+=20 # dodaje 20px 
    paddle_2.sety(y) #postavlja novu vrijednost na y

def paddle_2_down():
    y=paddle_2.ycor() #vraca y kordinatu
    y-=20 # oduzima 20px 
    paddle_2.sety(y) #postavlja novu vrijednost na y

game.listen()
game.onkeypress(paddle_1_up, "w") #pritiskom w ide gore...
game.onkeypress(paddle_1_down, "s") #pritiskom s ide dole...
game.onkeypress(paddle_2_up, "Up") #pritiskom up ide gore...
game.onkeypress(paddle_2_down, "Down") #pritiskom down ide dole...
random_number1 = random.choice([1, -1])
random_number2 = random.choice([1, -1])

while True:
    game.update()
    pen.clear()
    pen.write("Player 1: "+str(score_1)+" \t  Player B: "+str(score_2)+"",align="center",font=("Arial",24,"normal"))

    ball.setx(ball.xcor() + ball.dx*random_number1)
    ball.sety(ball.ycor() + ball.dy*random_number2)

    if paddle_1.ycor()>240: #ograniciti kretnje paddlova
        paddle_1_down()
    if paddle_1.ycor()<-240:
        paddle_1_up()
    if paddle_2.ycor()>240:
        paddle_2_down()
    if paddle_2.ycor()<-240:
        paddle_2_up()

    if ball.ycor()> 290: #ogranicavanje loptice
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_1+=1

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_2+=1

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_2.ycor()+50 and ball.ycor()>paddle_2.ycor() + 0): #kolizija loptice i paddlova
        ball.setx(340)
        ball.dx*=-1  
        ball.dy*=1 

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_2.ycor()+0 and ball.ycor()>paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx*=-1 
        ball.dy*=-1 

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_1.ycor()+50 and ball.ycor()>paddle_1.ycor() + 0):
        ball.setx(-340)
        ball.dx*=-1  
        ball.dy*=1 

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_1.ycor()+0 and ball.ycor()>paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx*=-1 
        ball.dy*=-1 

   

 