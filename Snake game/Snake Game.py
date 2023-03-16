import tkinter as tk
import random

root = tk.Tk()

canvas_width = 1200
canvas_height = 600
w, h = canvas_width // 2, canvas_height // 2
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

dir=2


def keypress(event):
    global dir
    if event.keycode == 37:
        #left
        if(not dir==2):
           dir=1
    elif event.keycode == 39:
        #right
        if (not dir == 1):
            dir = 2
    elif event.keycode == 38:
        #up
        if (not dir == 4):
            dir = 3
    elif event.keycode == 40:
        #down
        if (not dir == 3):
            dir = 4


def motion(event):
    return

root.bind("<Key>", keypress)
root.bind("<Motion>", motion)

snake = [(35,30), (34,30), (33,30), (32,30), (31, 30), (30, 30)]
food = (random.randint(0,119), random.randint(0,59))
gameOver =0
score = 0

objList = []

for it in snake:
    r=canvas.create_rectangle(it[0]*10, it[1]*10, it[0]*10 + 10, it[1]*10 + 10, fill='red')
    objList.append(r)

foodObj= canvas.create_rectangle(food[0]*10, food[1]*10, food[0]*10+10, food[1]*10+10, fill='green')


def eat():
    return snake[0]==food

def genFood():
    global food
    food = (random.randint(0, 119), random.randint(0, 59))
    print(food)
    canvas.coords(foodObj, food[0] * 10, food[1] * 10, food[0] * 10 + 10, food[1] * 10 + 10)

def frame():
    global gameOver
    head = (snake[0][0], snake[0][1])
    if dir==1:
        # left
        if head[0]==0:
            head = (119, head[1])
        else:
            head = (head[0] - 1, head[1])
    elif dir==2:
        # right
        head = ((head[0] + 1)%120, head[1])
    elif dir==3:
        # up
        if head[1]==0:
            head = (head[0], 59)
        else:
            head = (head[0], head[1] - 1)

    elif dir==4:
        # down
        head = (head[0], (head[1] + 1)%60)
    # canvas.move(objList[0], x, y)

    for it in snake:
        if it==head:
            gameOver=1
            print("GAME OVER")

    snake.insert(0, head)
    if (eat()):
        global score
        score+=1
        r = canvas.create_rectangle(it[0] * 10, it[1] * 10, it[0] * 10 + 10, it[1] * 10 + 10, fill='red')
        objList.append(r)
        genFood()
    else:
        snake.pop()



    i = 0
    for it in snake:
        canvas.coords(objList[i], it[0] * 10, it[1] * 10, it[0] * 10 + 10, it[1] * 10 + 10)
        i += 1

    if not gameOver:
        root.after(100, frame)
    else:
        canvas.create_text(w, h-50, fill="darkblue", font="Times 30  bold",
                           text="GAME OVER")
        canvas.create_text(w, h, fill="black", font="Times 30  bold",
                           text="SCORE: "+ str(score))
        canvas.update()


frame()
root.mainloop()
