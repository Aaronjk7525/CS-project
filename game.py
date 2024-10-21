from turtle import Screen
import pgzrun 
from platformer import *
import time

TILE_SIZE=18
ROWS= 18
COLS =18

WIDTH = TILE_SIZE*ROWS
HEIGHT = TILE_SIZE*COLS
TITLE="new game" 

platforms=build("tile3.csv",TILE_SIZE)
points=build("tile4.csv",TILE_SIZE)
obstacles=build("tile5.csv",TILE_SIZE)




player= Actor("p_right")
player.bottomleft = (0,HEIGHT-TILE_SIZE)
player.velocity_x = 3
player.velocity_y = 0
player.jumping = False
player.alive = True
gravity = 1
jump_velocity = -10
over = False
WIN = 0

def draw():
    screen.clear() # type: ignore
    screen.fill("skyblue") # type: ignore
    for platform in platforms:
        platform.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for point in points:
        point.draw()
    
    if player.alive:
        player.draw()
    #display
    if over==True and WIN!=0:
        screen.draw.text("!!!GAME OVER!!!",center=(WIDTH/2,HEIGHT/2)) # type: ignore
        screen.draw.text("!!!U have lost!!!",center=(WIDTH/3,HEIGHT/3)) # type: ignore
    if over==True and WIN==-1:
        screen.draw.text("!!!GAME OVER!!!",center=(WIDTH/2,HEIGHT/2)) # type: ignore
    

def update():
    global over,WIN,platforms,points
    if keyboard.LEFT and player.midleft[0] > 0: # type: ignore
        player.x-=player.velocity_x
        player.image ="p_left"
        #if player collided with plateform
        if player.collidelist(platforms)!=-1:
            object=platforms[player.collidelist(platforms)]
            player.x = object.x + (object.width/2 + player.width/2 )

    elif keyboard.RIGHT and player.midright[0] < WIDTH: # type: ignore
        player.x+=player.velocity_x
        player.image ="p_right"
        #if player collided with plateform
        if player.collidelist(platforms)!=-1:
            object=platforms[player.collidelist(platforms)]
            player.x = object.x - (object.width/2 + player.width/2 )


    #handles gravity
    player.y += player.velocity_y
    player.velocity_y += gravity
    #if player collided with platform
    if player.collidelist(platforms)!=-1:
        #get object tht player collided with
        object=platforms[player.collidelist(platforms)]
        if player.velocity_y>=0:
             player.y = object.y - (object.height/2 + player.height/2 )
             player.jumping = False 
        else:
             player.y = object.y + (object.height/2 + player.height/2 )
        player.velocity_y = 0


    # getting points
    for point in points:
        if player.colliderect(point)>0:
            points.remove(point)
    if len(points)==0:
        WIN-=1
    
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            over=True
            WIN+=1
        

 
def on_key_down(key):
    if key == keys.UP and not player.jumping: # type: ignore
        player.velocity_y = jump_velocity
        player.jumping = True
 
pgzrun.go()
