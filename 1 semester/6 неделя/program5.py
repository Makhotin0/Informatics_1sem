from tkinter import *
import random
WIDTH = 300
HEIGHT = 200

def color_func():
    num_colors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','F','E']
    color = ['#']
    for i in range(6):
        color.append(random.choice(num_colors))
    color = ''.join(color)
    return color

class Ball:
    def __init__(self):
        self.R = random.randint(10, 30)
        self.x = random.randint(self.R, WIDTH - self.R)
        self.y = random.randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (2, 2)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill = color_func())
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(10, tick)

def click_handler(event):
    new_ball = Ball()
    balls.append(new_ball)

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for i in range(5)]
tick()
root.mainloop()
