#IMPROVEMENTS
# 1 - Player can jump even if below a platform?
# 2 - horizontal collision - Done 
# 3 - Put player on platform if just about to make it

import pgzrun
#define screen size
WIDTH = 800
HEIGHT = 800
# Define Colors
MAROON = 128,0,0
#vertical accelerations
GRAVITY = 0.2

HORIZONTAL_SPEED = 2

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
  # Collision Check
  newx = player.x

  x_collision = False
  if keyboard.left:
    newx -= HORIZONTAL_SPEED
    if player.x < 0: x_collision = True
  if keyboard.right:
    newx += HORIZONTAL_SPEED
  new_player_position_x = Rect((newx, player.y),(player.w, player.h))

  newy = player.y
  player.y_velocity += GRAVITY
  newy += player.y_velocity
  new_player_position_y = Rect((player.x, newy),(player.w, player.h))

  y_collision = False
  for platform in platforms:
    y_collision = new_player_position_y.colliderect(platform) or y_collision
    x_collision = new_player_position_x.colliderect(platform) or x_collision

  if y_collision:
    player.y_velocity = 0
  else:
    player.y = newy

  # jump if colliding on y axis
  if keyboard.space and y_collision: 
    player.y_velocity = player.jump_velocity

  # Move if the player will not collide horizontally
  if keyboard.left and not x_collision and player.x > 0:
    player.x = newx
  elif keyboard.right and not x_collision and player.x < 780:
    player.x = newx

def draw():
  screen.clear()

  for platform in platforms:
    screen.draw.filled_rect(platform,MAROON)
  
  player.draw()

pgzrun.go()