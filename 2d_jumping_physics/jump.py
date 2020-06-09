#IMPROVEMENTS
# 1 - prevent player from being able to jump when below a platform
# 2 - horizontal collision - Done 
# 3 - Put player on platform if just about to make it

import pgzrun
from pgzero.builtins import Actor, animate, keyboard, Rect # make linter stop complaining

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

  # Create collision check for player position on the x axis
  x_collision = False
  if keyboard.left:
    newx -= HORIZONTAL_SPEED
    if player.x < 0: x_collision = True
  if keyboard.right:
    newx += HORIZONTAL_SPEED
    if player.x > 780: x_collision = True
  new_player_position_x = Rect((newx, player.y),(player.w, player.h))

  newy = player.y
  player.y_velocity += GRAVITY
  newy += player.y_velocity
  new_player_position_y = Rect((player.x, newy),(player.w, player.h))

  y_collision = False
  on_platform = False
  for platform in platforms:
    y_collision = new_player_position_y.colliderect(platform) or y_collision
    x_collision = new_player_position_x.colliderect(platform) or x_collision
    # check if player is above/on the platform
    if not on_platform:
      on_platform = y_collision and player.y < platform.y

  # stop falling if colliding
  if y_collision:
    player.y_velocity = 0
  else:
    player.y = newy

  # press space to jump if on the platform
  if keyboard.space and on_platform:
    player.y_velocity = player.jump_velocity

  # press left or right and the player will move unless colliding horizontally
  if keyboard.left and not x_collision:
    player.x = newx
  elif keyboard.right and not x_collision:
    player.x = newx

def draw():
  screen.clear()

  for platform in platforms:
    screen.draw.filled_rect(platform,MAROON)
  
  player.draw()

pgzrun.go()