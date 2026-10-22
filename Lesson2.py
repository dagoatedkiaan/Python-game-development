import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDPIAware()
import pgzrun
WIDTH =1000
HEIGHT=600
sky=(7,9,35)
ground=(0,70,20)
tree_1=(0,145,0)
tree_2=(0,125,0)
tree_3=(0,105,0)
bark=(92,52,20)
house=(151,76,16)
roof=(112,48,4)
door=(77,35,5)
window=(255,247,92)
fence=(184,132,67)
smoke=(145,145,140)
moon=(245,245,218)
starry=(220,225,240)
firefly=(255,244,60)
def rectangle(x,y, width , height , color):
    for yy in range(int(y),int(y+height)):
        screen.draw.line((int(x), yy), (int(x+width),yy),color)
def triangle(x1, y1, x2, y2, x3, y3, color):
    top = min(y1, y2, y3)
    bottom = max(y1, y2, y3)

    for y in range(int(top), int(bottom) + 1):

        points = []

        if y1 != y2:
            if min(y1, y2) <= y <= max(y1, y2):
                x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                points.append(x)

        if y2 != y3:
            if min(y2, y3) <= y <= max(y2, y3):
                x = x2 + (y - y2) * (x3 - x2) / (y3 - y2)
                points.append(x)

        if y3 != y1:
            if min(y3, y1) <= y <= max(y3, y1):
                x = x3 + (y - y3) * (x1 - x3) / (y1 - y3)
                points.append(x)

        if len(points) >= 2:
            left = int(min(points))
            right = int(max(points))

            screen.draw.line((left, y), (right, y), color)
stars = [(20, 25), (43, 48), (65, 18), (89, 58), (112, 35), (135, 12), (158, 52), (181, 28), (205, 70), (230, 40), (255, 18), (280, 62), (305, 30), (330, 12), (355, 48), (380, 25), (405, 67), (430, 38), (455, 15), (480, 55), (505, 28), (530, 10), (555, 46), (580, 70), (605, 30), (630, 52), (655, 20), (680, 64), (705, 37), (730, 12), (755, 55), (780, 28), (805, 68), (830, 42), (855, 17), (880, 50), (905, 30), (930, 12), (955, 58), (980, 35), (15, 95), (45, 120), (75, 88), (105, 140), (135, 110), (165, 128), (195, 92), (225, 150), (255, 105), (285, 135), (315, 95), (345, 145), (375, 112), (405, 155), (435, 105), (465, 135), (495, 92), (525, 125), (555, 102), (585, 145), (615, 110), (645, 135), (675, 98), (705, 145), (735, 115), (765, 135), (795, 95), (825, 145), (855, 105), (885, 135), (915, 100), (945, 125), (975, 105)]
def draw_stars():
    for x,y in stars:
         screen.draw.filled_circle((x,y),1,starry)
def draw_moon():
  screen.draw.filled_circle((790,85),43,moon)
def draw_tree(x,top):
     rectangle(x-12,top+75,24,145,bark)
     triangle(x,top+30,x-65,top+125,x+65,top+125,tree_3)
     triangle(x,top,x-53,top+95,x+53, top+95,tree_2)
     triangle(x,top-25,x-42,top+65,x+42,top+65,tree_1)
def draw_house():
    rectangle(350,275,210,200,house)
    triangle(315,278,455,165,595,278,roof)
    rectangle(315,270,280,10,roof)
    rectangle(380,320,43,43,window)
    rectangle(480,320,43,43,window)
    rectangle(440,385,53,75,door)
    screen.draw.filled_circle((482,422),2,(220,150,50))
def draw_ground():
    rectangle(0, 478, 1000, 122, ground)
def draw_fence():
    fence_y = 440

    rectangle(0, fence_y, 1000, 8, fence)
    rectangle(0, fence_y + 27, 1000, 8, fence)

    x = 20

    while x < 1000:
        rectangle(x, fence_y - 12, 13, 55, fence)
        x = x + 38
def draw_fire():
    triangle(700, 430, 680, 475, 720, 475, (255, 123, 0))
    triangle(700, 440, 690, 474, 710, 474, (255, 224, 0))
    rectangle(682, 472, 36, 7, (190, 55, 0))
def draw_smoke():
    screen.draw.filled_circle((700, 425), 10, smoke)
    screen.draw.filled_circle((713, 395), 11, smoke)
    screen.draw.filled_circle((707, 365), 11, smoke)
    screen.draw.filled_circle((709, 335), 12, smoke)
    screen.draw.filled_circle((700, 305), 13, smoke)
    screen.draw.filled_circle((687, 275), 13, smoke)
    screen.draw.filled_circle((683, 245), 14, smoke)
    screen.draw.filled_circle((686, 215), 15, smoke)
def draw_fireflies():

    fireflies = [
        (133, 320),
        (310, 310),
        (350, 330),
        (470, 320),
        (610, 280),
        (850, 380),
        (785, 400),
        (700, 370),
        (585, 450),
        (340, 450),
        (140, 470),
        (370, 520),
        (700, 500),
        (725, 515),
        (800, 530),
        (795, 465),
    ]

    for x, y in fireflies:
        screen.draw.filled_circle((x, y), 2,firefly)
def draw():
    screen.fill(sky)
    draw_stars()
    draw_moon()
    draw_tree(150, 315)
    draw_tree(275, 315)
    draw_tree(850, 315)
    draw_tree(950, 315)
    draw_house()
    draw_ground()
    draw_fire()
    draw_fence()
    draw_smoke()
    draw_fireflies()
pgzrun.go()