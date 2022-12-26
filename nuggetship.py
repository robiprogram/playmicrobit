from microbit import display, button_a, button_b, sleep, Image
import random
import music

def new_nugget():
    global nugget_x, nugget_y
    nugget_x = random.randint(0, 4)
    nugget_y = 0

def new_game():
    global player_x, score, speed, life
    display.show(Image("99999"))
    player_x = 2
    score = 0
    speed = 800
    life = 3
    new_nugget()

new_game()

# main loop
while True:
    # player moving left/right
    if button_a.was_pressed():
        if not (player_x == 0):
            player_x = player_x-1
    if button_b.was_pressed():
        if not (player_x == 4):
            player_x = player_x+1
    # show player
    for x in range(5):
        display.set_pixel(x, 4, 0)
    display.set_pixel(player_x, 4, 3 * life)
    # nugget falling
    nugget_y = nugget_y + 1
    # show nugget
    if nugget_y < 5:
        if nugget_y > 1:
            display.set_pixel(nugget_x, nugget_y - 1, 0)
        display.set_pixel(nugget_x, nugget_y, 4)
    sleep(speed)
    # nugget end
    if nugget_y == 5:
        life = life - 1
        if life == 0:
            music.play(music.WAWAWAWAA, wait=False)
            display.scroll("GAME OVER", delay=40)
            display.show(score)
            sleep(2000)
            new_game()
        else:
            music.play(music.POWER_DOWN)
            speed = speed + 200
            new_nugget()
    elif nugget_y == 4 and nugget_x == player_x:
        score = score + 1
        if speed > 250:
            speed = speed - 70
        new_nugget()
