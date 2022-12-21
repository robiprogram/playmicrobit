from microbit import *
import music
import random

# helpers

def wait_touched():
    while not(pin_logo.is_touched()):
        sleep(50)

def start_music(enable_music):
    if enable_music:
        music.play(music.ODE,wait=False,loop=True)

def show_player(x,life):
    for i in range(5):
        display.set_pixel(i,4,0)
    display.set_pixel(x,4,life)

def show_nugget(x,y):
    if y > 1:
        display.set_pixel(x,y-1,0)
    display.set_pixel(x,y,4)

# init
x=2
life=9
score=0
speed=1000

# main

sablier1=Image("99999:09990:00900:09990:99999")
sablier2=Image("90009:99099:99999:99099:90009")
display.show([sablier1,sablier2,sablier1,sablier2,sablier1,sablier2],delay=1000)

music.play(music.PRELUDE,wait=False)

display.scroll("NUGGET SHIP")

display.scroll("music ?")
fleche_D=Image("00900:00090:99999:00090:00900")
fleche_G=Image("00900:09000:99999:09000:00900")
display.show([fleche_D],delay=1500)
display.scroll("yes")
display.show([fleche_G],delay=1500)
display.scroll("no")

enable_music=False

# ignore buttons pressed before now
button_a.was_pressed()
button_b.was_pressed()

while not(button_a.was_pressed()):
    if button_b.was_pressed():
        enable_music=True
        break
    sleep(50)

START=Image("00900:09990:90909:00900:00900")
display.show([START],delay=500)
display.scroll("START")
display.show([START])
wait_touched()

start_music(enable_music)

display.show("321",delay=1000)
display.scroll("GO!")

display.show(Image("99999"))
nugget_x=random.randint(0,4)
nugget_y=1

while True:
    if button_a.was_pressed():
        if not(x==0):
            x=x-1
    if button_b.was_pressed():
        if not(x==4):
            x=x+1
    show_player(x,life)
    show_nugget(nugget_x,nugget_y)
    nugget_y=nugget_y+1
    if nugget_y==5:
        if nugget_x==x:
            score=score+1
            speed=speed-15
            if speed<100:
                speed=100
        else:
            life=life-2
            if life==-1:
                music.play(music.WAWAWAWAA)
                display.scroll("GAME OVER")
                display.show(score,delay=2000)
                display.show(Image("99999"))
                life=9
                x=2
                score=0
                speed=1000
                start_music(enable_music)
            else:
                music.play(music.POWER_DOWN)
                start_music(enable_music)
            display.set_pixel(nugget_x,nugget_y-1,0)
        nugget_x=random.randint(0,4)
        nugget_y=1
    sleep(speed)

