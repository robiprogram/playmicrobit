from microbit import display, button_a, button_b, sleep, Image
import random

# new nugget
nugget_x = random.randint(0, 4)
nugget_y = 0

# init
display.show(Image("99999"))
player_x = 2

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
    display.set_pixel(player_x, 4, 9)
    # nugget falling
    nugget_y = nugget_y + 1
    # show nugget
    if nugget_y < 5:
        if nugget_y > 1:
            display.set_pixel(nugget_x, nugget_y - 1, 0)
        display.set_pixel(nugget_x, nugget_y, 4)
    sleep(800)
    # nugget end
    if nugget_y == 5:
        display.scroll("GAME OVER", delay=40)
        break
    elif nugget_y == 4 and nugget_x == player_x:
        display.show(Image.HAPPY)
        break
