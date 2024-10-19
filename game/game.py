import pgzrun
import random
import itertools

WIDTH=600
HEIGHT=400

blockpositions=[(550,50),(550,350),(50,350),(50,50)]

blocks=itertools.cycle(blockpositions)

block=Actor('block')
block.pos=(50,50)

ship=Actor('ship')
ship.pos=(300,200)

def draw():
    screen.clear()
    ship.draw()
    block.draw()


def moveblock():
    animate(block,'bounce_end',duration=1,pos=next(blocks))

def shiptarget():
    x=random.randint(100,500)
    y=random.randint(100,300)
    ship.target=x,y
    targetangle=ship.angle_to(ship.target)
    targetangle += 360*((ship.angle-targetangle+180)//360)
    animate(ship,angle=targetangle,duration=0.9,on_finished=moveship)

def moveship():
    animate(ship,tween='accel_decel',pos=ship.target,duration=ship.distance_to(ship.target)/200,on_finished=shiptarget)

moveblock()
clock.schedule_interval(moveblock,2)
shiptarget()
pgzrun.go()