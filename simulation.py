import pygame as pg
import pygame.display as display
import pygame.draw as draw
import pygame.key as key
import pygame.event as event
import time
from ball import Ball
import threading





def update():

    display.flip()
    #print(display.update)



def draw_ball(surface,pos):
    return draw.circle(surface, pg.Color(255,255,255),pos,10)


def make_window():
    display.init()
    dims = (700,400)
    return display.set_mode(dims)


def test():
    if not display.get_init():
        raise Exception("failed to initialize window")

def gravity_fall(ball_obj):
    
    dy = 1
    ball_obj.move_down(dy)
    print(ball_obj.get_pos())
    

def bounce(ball_obj):
    pass



def main():
    
    #test()
    
    
    quit = False
    
    win = make_window()
    color= (31, 43, 66)
    win.fill(color)
    #print(display.get_surface())
    ball_pos = (350,200)
    
    ball_obj = Ball(ball_pos)
    update()

    UPDATE_DELAY = .5
    TIME =0.0
    G = 98

    SECONDS_PER_PIXEL= 1.0/G
    
    ball = draw_ball(win,ball_pos)

    while not quit:
        
        dt = pg.time.Clock().tick(60)/1000.0
        TIME+=dt

        
        #time.sleep(1)
        if TIME>=UPDATE_DELAY:
            win.fill(color)
            gravity_fall(ball_obj)
            update()
            draw_ball(win,ball_obj.get_pos())
            TIME-=SECONDS_PER_PIXEL

            if list(ball_obj.get_pos())[1]+10 >= list(win.get_size())[1]:
                quit = True


        events = event.get()
        for ev in events:

            if ev.type == pg.QUIT:
                quit = True
                UPDATE_SCREEN =False
        
        
        update()
    display.quit()
    

main()

