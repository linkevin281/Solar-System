# name: Kevin Lin
# date: 02/13/21
# purpose: create solar driver

from bodyextra import Body
from systemextra import System
from cs1lib import *
from math import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

TIME_SCALE_INNER = 3.0e6  # real seconds per simulation second for inner planets
TIME_SCALE_INNER_M = 4.0e6  # real seconds per simulation second for menu inner planets
TIME_SCALE_OUTER = 6.0e7 # real seconds per simulation second for outer planets
TIME_SCALE_OUTER_M = 6.0e7 # real seconds per simulation second for menu outer planets
TIME_SCALE_SLING = 3.0e6  # real seconds per simulation second for slingshot
TIME_SCALE_SLING_M = 4.0e6  # real seconds per simulation second for slingshot
TIME_SCALE_DEATH_STAR = 3.0e6  # real seconds per simulation second for death star
TIME_SCALE_DEATH_STAR_M = 4.0e6  # real seconds per simulation second for menu death star

PIXELS_PER_METER_INNER = 18 / 1e10  # distance scale for the inner planets
PIXELS_PER_METER_INNER_M = 4 / 1e10 # distance scale for menu inner planets
PIXELS_PER_METER_OUTER = 7 / 1e11 # distance scale for the outer planets
PIXELS_PER_METER_OUTER_M = 3 / 1e11 # distance scale for menu outer planets
PIXELS_PER_METER_SLING = 20 / 1e10 # distance scale for slingshot
PIXELS_PER_METER_SLING_M = 4 / 1e10 # distance scale for slingshot
PIXELS_PER_METER_DEATH = 20 / 1e10 # distance scale for death star
PIXELS_PER_METER_DEATH_M = 4 / 1e10 # distance scale for death star menu

CENTER_MIP_X = 220 # x center for inner planets menu
CENTER_MIP_Y = 370 # y center for inner planets menu
CENTER_MOP_X = 760 # x center for outer planets menu
CENTER_MOP_Y = 370 # y center for outer planets menu
CENTER_MD_X = 220 # x center for slingshot menu
CENTER_MD_Y = 760 # y center for slingshot menu
CENTER_D_X = 760 # x center for death star menu
CENTER_D_Y = 760 # y center for death star menu

FRAMERATE = 30  # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

KEY1 = "1"
KEY2 = "2"
KEY3 = "3"
KEY4 = "4"
KEY5 = "5"
KEYP = "p"
KEYU = "u"
KEY_SPACE = " "

SLING_SPEED = 50000

time_scale = 0
pixels_per_meter = 0
centerx = 0
centery = 0

mx = 0 # mouse coordinates
my = 0

# body for planets
sun = Body(1.98892e30, 0, 0, 0, 0, 25, 1, 1, 0)
sun_o = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0) # for outer planet sun
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 7, 1, 1, 1)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 15, 0, 1, 0)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 16, .45, 0.6, 1)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 10, 1, 0, 0)
jupiter = Body(1.898e27, -760.28e9, 0, 0, 13060, 10, 1, 0, 0)
saturn = Body(5.683e26, -1490.1e9, 0, 0, 9700, 8, .824, .706, .549)
uranus = Body(86.8e24, -2872.5e9, 0, 0, 6800, 5, .678, .847, .902)
neptune = Body(102e24, -4495.1e9, 0, 0, 5400, 5, 0, 0, 1)
pluto = Body(0.0146e24, -5906.4e9, 0, 0, 4700, 5, 0, 0, .5)

# body for menu planets
sun_m = Body(1.98892e30, 0, 0, 0, 0, 12, 1, 1, 0)
mercury_m = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 1, 1)
venus_m = Body(4.87e24, -108.2e9, 0, 0, 35040, 5, 0, 1, 0)
earth_m = Body(5.97e24, -149.6e9, 0, 0, 29790, 7, .45, 0.6, 1)
mars_m = Body(0.642e24, -227.9e9, 0, 0, 24140, 5, 1, 0, 0)
jupiter_m = Body(1.898e27, -760.28e9, 0, 0, 13060, 6, 1, 0, 0)
saturn_m = Body(5.683e26, -1490.1e9, 0, 0, 9700, 4, .824, .706, .549)
uranus_m = Body(86.8e24, -2872.5e9, 0, 0, 6800, 4, .678, .847, .902)
neptune_m = Body(102e24, -4495.1e9, 0, 0, 5400, 4, 0, 0, 1)
pluto_m = Body(0.0146e24, -5906.4e9, 0, 0, 4700, 2, 0, 0, .7)

# body for slingshot
sun_md = Body(1.98892e30, 0, 0, 0, 0, 30, 1, 1, 0)
mercury_md = Body(0.33e24, -57.9e9, 0, 0, 47890, 7, 1, 1, 1)
venus_md = Body(4.87e24, -108.2e9, 0, 0, 35040, 15, 0, 1, 0)
earth_md = Body(5.97e24, -149.6e9, 0, 0, 29790, 30, .45, 0.6, 1)
mars_md = Body(0.642e24, -227.9e9, 0, 0, 24140, 20, 1, 0, 0)
ship = 0

# body for slingshot menu
sun_mdm = Body(1.98892e30, 0, 0, 0, 0, 12, 1, 1, 0)
mercury_mdm = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 1, 1)
venus_mdm = Body(4.87e24, -108.2e9, 0, 0, 35040, 5, 0, 1, 0)
earth_mdm = Body(5.97e24, 149.6e9, 0, 0, -29790, 7, .45, 0.6, 1)
mars_mdm = Body(0.642e24, 227.9e9, 0, 0, -24140, 5, 1, 0, 0)
ship_m = Body(100e12, 500e9, -140e9, -50000, 00, 4, 0.5, 0.5, 0.5)

# body for death star
sun_d = Body(1.98892e30, 0, 0, 0, 0, 32, 1, 1, 0)
mercury_d = Body(0.33e24, -57.9e9, 0, 0, 47890, 7, 1, 1, 1)
venus_d = Body(4.87e24, -108.2e9, 0, 0, 35040, 10, 0, 1, 0)
earth_d = Body(5.97e24, -149.6e9, 0, 0, 29790, 23, .45, 0.6, 1)
mars_d = Body(0.642e24, -227.9e9, 0, 0, 24140, 15, 1, 0, 0)

# body for death star menu
sun_dm = Body(1.98892e30, 0, 0, 0, 0, 12, 1, 1, 0)
mercury_dm = Body(0.33e24, 0, 57.9e9, 47890, 0, 4, 1, 1, 1)
venus_dm = Body(4.87e24, 0, 108.2e9, 35040, 0, 5, 0, 1, 0)
earth_dm = Body(5.97e24, 0, 149.6e9, 29790, 0, 7, .45, 0.6, 1)
mars_dm = Body(0.642e24, 0, 227.9e9, 24140, 0, 5, 1, 0, 0)

# system lists
inner_planet_list = [sun, mercury, venus, earth, mars]
inner_planet_list_m = [sun_m, mercury_m, venus_m, earth_m, mars_m]
outer_planet_list = [sun_o, jupiter, saturn, uranus, neptune, pluto]
outer_planet_list_m = [sun_m, jupiter_m, saturn_m, uranus_m, neptune_m, pluto_m]
slingshot_list = [sun_md, mercury_md, venus_md, earth_md, mars_md]
slingshot_list_m = [sun_mdm, mercury_mdm, venus_mdm, earth_mdm, mars_mdm, ship_m]
death_star_list = [sun_d, mercury_d, venus_d, earth_d, mars_d]
death_star_list_m = [sun_dm, mercury_dm, venus_dm, earth_dm, mars_dm]

# system creation
system1 = System(inner_planet_list)
system1_m = System(inner_planet_list_m)
system2 = System(outer_planet_list)
system2_m = System(outer_planet_list_m)
system3 = System(slingshot_list)
system3_m = System(slingshot_list_m)
system4 = System(death_star_list)
system4_m = System(death_star_list_m)

pressed1 = False
pressed2 = False
pressed3 = False
pressed4 = False
pressed5 = False
pressedp = False
pressedu = False
pressed_space = False

stop = False
menu = True # turn off and on menu functions
op1 = False # turn off and on options
op2 = False
op3 = False
op4 = False
paused = False

sling_one = True
sling_two = True
sling_instruction = True
slingshot_end = False

death_instruction = True
p1 = True
p2 = True
p3 = True
p4 = True
p5 = True

x1 = 0
y1 = 0
time = 0
time2 = 0


def key_down(key): # checks if a key is pressed
    global KEY1, KEY2, KEY3, KEY4, pressed1, pressed2, pressed3, pressed4, pressedp, KEYP, pressedu, KEYU
    global KEY_SPACE, pressed_space, KEY5, pressed5

    if key == KEY1:
        pressed1 = True
    if key == KEY2:
        pressed2 = True
    if key == KEY3:
        pressed3 = True
    if key == KEY4:
        pressed4 = True
    if key == KEY5:
        pressed5 = True
    if key == KEYP:
        pressedp = True
    if key == KEYU:
        pressedu = True
    if key == KEY_SPACE:
        pressed_space = True


def key_up(key): # checks if a key is released
    global KEY1, KEY2, KEY3, KEY4, pressed1, pressed2, pressed3, pressed4, pressedp, KEYP, pressedu, KEYU
    global KEY_SPACE, pressed_space, KEY5, pressed5

    if key == KEY1:
        pressed1 = False
    if key == KEY2:
        pressed2 = False
    if key == KEY3:
        pressed3 = False
    if key == KEY4:
        pressed4 = False
    if key == KEY5:
        pressed5 = False
    if key == KEYP:
        pressedp = False
    if key == KEYU:
        pressedu = False
    if key == KEY_SPACE:
        pressed_space = False


def m_move(x, y): # finds the mouse's coordinates
    global mx, my
    mx = x
    my = y


def pause(): # press p to pause sim and u to unpause
    global pressedp, paused, pressedu

    if pressedp:
        paused = True

    if pressedu:
        paused = False


def main_menu(): # runs each component on the main menu
    draw_menu()
    menu_inner_planets()
    menu_outer_planets()
    menu_slingshot()
    menu_death_star()


def draw_menu(): # draws the menu text
    enable_stroke()
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 1)
    set_font_size(60)
    set_font_bold()
    set_font_italic()
    draw_text("Gravity Simulator", 163, 150)
    set_font_normal()
    set_font_size(15)
    draw_text("[1]", 212, 220)
    draw_text("[2]", 748, 220)
    draw_text("[3]", 212, 610)
    draw_text("[4]", 748, 610)
    set_font_normal()
    set_font_size(20)
    draw_text("Inner Planets", 150, 260)
    draw_text("Outer Planets", 680, 260)
    draw_text("Gravitational Slingshot", 100, 650)
    draw_text("Death Star", 690, 650)
    draw_text("Type a number to get started!", 310, 950)


def menu_inner_planets(): # draws the inner planets menu
    global CENTER_MIP_X, CENTER_MIP_Y, PIXELS_PER_METER_INNER_M, TIME_SCALE_INNER_M, stop
    disable_stroke()
    system1_m.draw(CENTER_MIP_X, CENTER_MIP_Y, PIXELS_PER_METER_INNER_M, stop)
    system1_m.update(TIMESTEP * TIME_SCALE_INNER_M, stop)


def menu_outer_planets(): #draws the outer planet menu
    global CENTER_MOP_X, CENTER_MOP_Y, PIXELS_PER_METER_OUTER_M, TIME_SCALE_OUTER_M, stop
    disable_stroke()
    system2_m.draw(CENTER_MOP_X, CENTER_MOP_Y, PIXELS_PER_METER_OUTER_M, stop)
    system2_m.update(TIMESTEP * TIME_SCALE_OUTER_M, stop)


def menu_slingshot(): # draws the slingshot menu
    global CENTER_MD_X, CENTER_MD_Y, PIXELS_PER_METER_SLING_M, TIME_SCALE_SLING_M, stop
    disable_stroke()
    system3_m.draw(CENTER_MD_X, CENTER_MD_Y, PIXELS_PER_METER_SLING_M, stop)
    system3_m.update(TIMESTEP * TIME_SCALE_SLING_M, stop)


def menu_death_star(): #draws the death star menu
    global CENTER_D_X, CENTER_D_Y, PIXELS_PER_METER_DEATH_M, TIME_SCALE_DEATH_STAR_M, stop
    disable_stroke()
    system4_m.draw(CENTER_D_X, CENTER_D_Y, PIXELS_PER_METER_DEATH_M, stop)
    system4_m.update(TIMESTEP * TIME_SCALE_DEATH_STAR_M, stop)

    # draw the death star
    set_fill_color(.3, .3, .3)
    draw_circle(900, 900, 20)
    set_fill_color(.1, .1, .1)
    draw_circle(895, 891, 8)
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_stroke_width(2)
    draw_line(880, 902, 920, 902)


def inner_planets(): # runs inner planet simulation
    global PIXELS_PER_METER_INNER, TIME_SCALE_INNER, stop
    set_clear_color(0, 0, 0)
    clear()
    system1.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER_INNER, stop)
    system1.update(TIMESTEP * TIME_SCALE_INNER, stop)


def outer_planets(): # runs outer planet simulation
    global PIXELS_PER_METER_OUTER, TIME_SCALE_OUTER, stop
    set_clear_color(0, 0, 0)
    clear()
    system2.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER_OUTER, stop)
    system2.update(TIMESTEP * TIME_SCALE_OUTER, stop)


# runs slingshot simulation - goal: have the fastest possible speed when the ship hits the edge
def slingshot():
    global PIXELS_PER_METER_SLING, TIME_SCALE_SLING, stop, paused, system3, slingshot_end, sling_instruction

    if sling_instruction:
        slingshot_instructions()

    else:

        pause()

        if not paused and not slingshot_end:

            set_clear_color(0, 0, 0)
            clear()
            enable_stroke()

            if ship != 0:        # once the ship has been made start checking if it leaves the area
                check_slingshot()
                disable_stroke() # also hide the instructions text

            set_stroke_color(1, 1, 1)
            set_font_size(15)
            draw_text("Press p to pause", 0, 30)
            draw_text("Pressed u to unpause", 0, 50)
            draw_text("While paused, click to place the ship", 0, 100)

            disable_stroke()
            system3.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER_SLING, stop)
            system3.update(TIMESTEP * TIME_SCALE_SLING, stop)

            if ship != 0:
                check_slingshot()

        if paused and not slingshot_end:

            slingshot_add_ship()
            slingshot_draw()
            slingshot_calculate()

        if slingshot_end:
            sling_score()


def slingshot_instructions(): #display instructions before the game
    global sling_instruction

    set_clear_color(0, 0, 0)
    clear()
    enable_stroke()
    set_font_size(30)
    set_stroke_color(1, 1, 1)
    draw_text("A gravitational slingshot is a technique used to", 100, 150)
    draw_text("alter the path and speed of a spacecraft.", 130, 200)
    draw_text("The technique uses the gravity of an astronomical", 80, 300)
    draw_text("object in order to perform the maneuver.", 150, 350)
    draw_text("Your goal is to set a starting point and path for a ship", 50, 550)
    draw_text("so that it has the maximum possible velocity", 120, 600)
    draw_text("as it leaves the solar system.", 240, 650)
    draw_text("Press space to continue", 280, 850)

    if pressed_space:
        sling_instruction = False


def slingshot_add_ship(): #if mouse gets pressed add ship to system once
    global sling_one, system3, x1, y1, stop, ship

    if is_mouse_pressed():
        if sling_one:
            x1 = mx
            y1 = my
            ship = Body(1, (x1 - 500) / PIXELS_PER_METER_SLING,
                        (y1 - 500) / PIXELS_PER_METER_SLING, 0, 0, 5, .3, .3, .3)
            slingshot_list.append(ship)
            system3 = System(slingshot_list)
            sling_one = False


def slingshot_draw(): # draws the new ship and information
    global sling_one, time, system3, stop

    if not sling_one:
        set_clear_color(0, 0, 0)
        clear()
        enable_stroke()
        set_stroke_color(1, 1, 1)
        set_stroke_width(2)
        draw_line(x1, y1, mx, my)

        set_stroke_color(1, 1, 1)
        set_font_size(17)
        draw_text("ship placed", x1 + 30, y1 - 15)
        set_font_size(25)
        draw_text("please select a direction", 320, 100)
        disable_stroke()
        system3.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER_SLING, stop)
        time = time + 1


def slingshot_calculate(): # calculate the x and y velocity of the ship according to SLING_SPEED
    global paused, time, x1, x2

    if is_mouse_pressed() and time > 20:
        x = mx - x1
        y = my - y1
        z = sqrt((x ** 2 + y ** 2) / SLING_SPEED ** 2)

        ship.vx = x / z
        ship.vy = y / z

        paused = False


def check_slingshot(): #checks if the ship has left the system
    global ship, slingshot_end

    if ship.x > (WINDOW_WIDTH - 500) / PIXELS_PER_METER_SLING:
        slingshot_end = True

    if ship.x < (500 - WINDOW_WIDTH) / PIXELS_PER_METER_SLING:
        slingshot_end = True

    if ship.y > (WINDOW_HEIGHT - 500) / PIXELS_PER_METER_SLING:
        slingshot_end = True

    if ship.y < (500 - WINDOW_HEIGHT) / PIXELS_PER_METER_SLING:
        slingshot_end = True


def sling_score(): # score screen for slingshot game
    global ship
    x = ship.vx
    y = ship.vy

    score = sqrt(x**2 + y**2)

    set_clear_color(0, 0, 0)
    clear()
    enable_stroke()
    set_font_size(30)
    set_stroke_color(1, 1, 1)
    draw_text("Starting speed: " + str(SLING_SPEED) + "m/s", 280, 300)
    draw_text("When your ship left the system,", 250, 400)
    draw_text("your ship was moving at:", 310, 450)
    draw_text(str(score) + " m/s", 300, 550)

def death_star(): # death star game
    global death_instruction

    if death_instruction:
        death_star_instruction()

    else:
        set_clear_color(0, 0, 0)
        clear()
        enable_stroke()
        set_font_size(15)
        set_stroke_color(1, 1, 1)
        draw_text("Press 1 to remove Mercury", 0, 20)
        draw_text("Press 2 to remove Venus", 0, 40)
        draw_text("Press 3 to remove Earth", 0, 60)
        draw_text("Press 4 to remove Mars", 0, 80)
        draw_text("Press 5 to remove the Sun", 0, 100)

        destroy_planet()

        disable_stroke()
        system4.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER_DEATH, stop)
        system4.update(TIMESTEP * TIME_SCALE_DEATH_STAR, stop)

        death_draw()

def death_star_instruction(): # instruction for death star
    global pressed_space, death_instruction

    set_clear_color(0, 0, 0)
    clear()
    enable_stroke()
    set_font_size(30)
    set_stroke_color(1, 1, 1)
    draw_text("You have control the death star superlaser and can", 50, 300)
    draw_text("destroy any body within the solar system.", 120, 380)

    draw_text("Remove bodies to study how gravity is affected.", 80, 580)

    draw_text("Press space to continue", 280, 900)

    if pressed_space:
        death_instruction = False


def death_draw(): # draw the death star

    set_fill_color(.3, .3, .3)
    draw_circle(900, 900, 50)
    set_fill_color(.1, .1, .1)
    draw_circle(885, 880, 19)
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_stroke_width(2)
    draw_line(850, 902, 950, 902)

def destroy_planet(): # destroy a planet with the death star
    global pressed1, pressed2, pressed3, pressed4, pressed5, p1, p2, p3, p4, p5
    global system4, death_star_list, mercury_d, venus_d, earth_d, mars_d, sun_d, time2

    if pressed1 and p1:
        p1 = False

        while time2 < 80:
            enable_stroke()
            set_stroke_width(4)
            set_stroke_color(.196, .804, .196)
            draw_line(885, 880, mercury_d.x * PIXELS_PER_METER_DEATH, mercury_d.y * PIXELS_PER_METER_DEATH)
            time2 = time2 + 1

        death_star_list.remove(mercury_d)
        system4 = System(death_star_list)
        time2 = 0


    if pressed2 and p2:
        p2 = False

        while time2 < 80:
            enable_stroke()
            set_stroke_width(4)
            set_stroke_color(.196, .804, .196)
            draw_line(885, 880, venus_d.x * PIXELS_PER_METER_DEATH, venus_d.y * PIXELS_PER_METER_DEATH)
            time2 = time2 + 1

        death_star_list.remove(venus_d)
        system4 = System(death_star_list)
        time2 = 0

    if pressed3 and p3:
        p3 = False

        while time2 < 80:
            enable_stroke()
            set_stroke_width(4)
            set_stroke_color(.196, .804, .196)
            draw_line(885, 880, earth_d.x * PIXELS_PER_METER_DEATH, earth_d.y * PIXELS_PER_METER_DEATH)
            time2 = time2 + 1

        death_star_list.remove(earth_d)
        system4 = System(death_star_list)
        time2 = 0

    if pressed4 and p4:
        p4 = False

        while time2 < 80:
            enable_stroke()
            set_stroke_width(4)
            set_stroke_color(.196, .804, .196)
            draw_line(885, 880, mars_d.x * PIXELS_PER_METER_DEATH, mars_d.y * PIXELS_PER_METER_DEATH)
            time2 = time2 + 1

        death_star_list.remove(mars_d)
        system4 = System(death_star_list)
        time2 = 0

    if pressed5 and p5:
        p5 = False

        while time2 < 80:
            enable_stroke()
            set_stroke_width(4)
            set_stroke_color(.196, .804, .196)
            draw_line(885, 880, sun_d.x * PIXELS_PER_METER_DEATH, sun_d.y * PIXELS_PER_METER_DEATH)
            time2 = time2 + 1

        death_star_list.remove(sun_d)
        system4 = System(death_star_list)
        time2 = 0


def option_selection(): #changes op values when a button is pressed
    global pressed1, pressed2, pressed3, pressed4, op1, op2, op3, op4, stop, menu

    if not op1 and not op2 and not op3 and not op4:

        if pressed1:
            op1 = True
            menu = False

        if pressed2:
            op2 = True
            menu = False

        if pressed3:
            op3 = True
            menu = False

        if pressed4:
            op4 = True
            menu = False


def main():
    global menu, op1, op2, op3, op4

    option_selection()

    if menu:
        main_menu()

    if op1:
        inner_planets()

    if op2:
        outer_planets()

    if op3:
        slingshot()

    if op4:
        death_star()

start_graphics(main, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, key_release=key_up, key_press=key_down, mouse_move=m_move)