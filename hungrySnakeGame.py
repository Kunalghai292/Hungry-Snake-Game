""" imports """
import turtle
import random
from pygame import mixer

""" adjusts the width, height of the playable screen area, also controls the size of the food """
w = 1400
h = 780
food_size = 30
delay = 100 
colors = ("blue", "red", "pink", "yellow", "violet", "white")
flag = True

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0) }

""" defines the movement of the snake when the game starts, or when the snake bites itself"""
def reset():
    global snake, snake_dir, food_position, pen, score, highscore, file

    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()
    
""" function to move the snake turtle"""
def move_snake():
    global snake_dir

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
    
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

    
        if not food_collision():
            snake.pop(0)


        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h


        pen.clearstamps()

        
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        
        screen.update()

        turtle.ontimer(move_snake, delay)


""" function defines how snake eats the food """
def food_collision():
    global food_position, score

    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()

        screen.update()
        pen.color(colors[random.randint(0, len(colors) - 1)])
        
        food.color(colors[random.randint(0, len(colors) - 1)])
        food.goto(food_position)

        return True
    return False

""" generates food at random location in the playable screen space """
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)

""" snake up, left, down, right, movement definitions """
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir!= "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

"""screen setup including the game title, bg color etc"""
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Hungry Snake Game")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)

""" pen = snake turtle """
pen = turtle.Turtle("circle")
pen.color("yellow")
pen.penup()
pen.speed(100)

""" food = snake food"""
food = turtle.Turtle()
food.shape("circle")
food.color("black")
food.shapesize(food_size / 20)
food.penup()

""" calling fuctions so that they respond to key presses """
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()