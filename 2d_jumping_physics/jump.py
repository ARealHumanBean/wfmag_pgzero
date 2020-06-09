#IMPROVEMENTS
# 1 - Player can jump even if below a platform?
# 2 - horizontal collision
# 3 -  

import pgzrun
#define screen size
WIDTH = 800
HEIGHT = 800
# Define Colors
MAROON = 128,0,0
#vertical accelerations
GRAVITY = 0.2

platforms = [
  Rect((0,780),(800,20)),
  Rect((200,700),(100,100)),
  Rect((400,650),(100,20)),
  Rect((600,600),(100,20))
]

player = Actor('alien',(50,450), anchor=('left', 'top'))
player.w = 20
player.h = 20

player.y_velocity = 0
player.jump_velocity = -7

def update():
  #horizontal movement
  if keyboard.left and player.x > 0:
    player.x -= 2
  if keyboard.right and player.x < 780:
    player.x += 2
  
  #vertical movement
  newy = player.y
  
  player.y_velocity += GRAVITY
  newy += player.y_velocity

  new_player_position_y = Rect((player.x, newy),(player.w, player.h))

  #collision check
  y_collision = False
  for platform in platforms:
    y_collision = new_player_position_y.colliderect(platform) or y_collision
  
  if y_collision:
    player.y_velocity = 0
  else:
    player.y = newy

  # jump if colliding on y axis
  if keyboard.space and y_collision: 
    player.y_velocity = player.jump_velocity

def draw():
  screen.clear()

  for platform in platforms:
    screen.draw.filled_rect(platform,MAROON)
  
  player.draw()

pgzrun.go()