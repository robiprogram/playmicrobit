from microbit import display, button_a, button_b, sleep

# init
player_x = 2

# main loop
while True:
    if button_a.was_pressed():
        if not (player_x == 0):
            player_x = player_x-1
    if button_b.was_pressed():
        if not (player_x == 4):
            player_x = player_x+1
    for x in range(5):
        display.set_pixel(x, 4, 0)
    display.set_pixel(player_x, 4, 9)
    sleep(800)
