import pgzrun
from random import randint

WIDTH = 300

HEIGHT = 300

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
def draw():
    width = WIDTH
    height = HEIGHT-200

    r = 255
    g = 0
    b = randint(0,255)

    for meow in range(20):
        miau = Rect((0,0), (width, height))
        miau.center = (150, 150)
        
        width -= 10
        height += 10
        screen.draw.rect(miau, (r,g,b))
        r-= 10
        g += 10
pgzrun.go()