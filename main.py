import random as r


layer_char = ["🟩", "🟫", "🟫" ,"🟫", "⬛", "⬛"]


player_pos = [0, 0]

player_layer = 0

player = "🟨"

down_hole = "⬜"

up_hole = "🟦"

board_size = 10

hole_positions = [(r.randint(0, board_size-1), r.randint(0, board_size-1)) for i in range(len(layer_char))]


# Get Rid of Two Holes in a row in the same position
def del_double_holes(hole_list):
  global board_size
  if board_size == 1:
    return hole_list
  new_list = hole_list
  repeat = True
  while repeat:
    repeat = False
    for i in range(len(hole_list)):
      if i+1 < len(hole_list):
        if hole_list[i] == hole_list[i+1]:
          new_list[i] = (r.randint(0, board_size-1), r.randint(0, board_size-1))
          repeat = True
  return new_list

hole_positions = del_double_holes(hole_positions)


def print_board():
  if player_layer > len(layer_char)-1:
    print("You fell into the void and died. L Bozo!")
    return False
  for y in range(board_size):
    for x in range(board_size):
      if not player_pos[0] == x or not player_pos[1] == y:
        if not hole_positions[player_layer][0] == x or not hole_positions[player_layer][1] == y:
          if player_layer > 0:
            if hole_positions[player_layer-1][0] == x and hole_positions[player_layer-1][1] == y:
              print(up_hole, end="")
            else:
              print(layer_char[player_layer], end="")
          else:
            print(layer_char[player_layer], end="")
        else:
          print(down_hole, end="")              
      else:
        print(player, end="")
    print("")
  return True

def move_player():
  global player_layer
  move = input("Which way do you want to move?: ").lower()
  if move == "forward" or move == "f" or move == "w":
    if player_pos[1] > 0:
      player_pos[1] -= 1
    else:
      print("You can't move that way!")
      move_player()
  elif move == "backwards" or move == "b" or move == "s":
    if player_pos[1] < board_size-1:
      player_pos[1] += 1
    else:
      print("You can't move that way!")
      move_player()
  elif move == "left" or move == "l" or move == "a":
    if player_pos[0] > 0:
      player_pos[0] -= 1
    else:
      print("You can't move that way!")
      move_player()
  elif move == "right" or move == "r" or move == "d":
    if player_pos[0] < board_size-1:
      player_pos[0] += 1
    else:
      print("You can't move that way!")
      move_player()
  elif move == "down" or move == "e":
    if player_pos[0] == hole_positions[player_layer][0] and player_pos[1] == hole_positions[player_layer][1]:
      player_layer += 1
    else:
      print("You can't move that way!")
      move_player()
  elif move == "up" or move == "q":
    if player_layer >= 0:
      if player_pos[0] == hole_positions[player_layer-1][0] and player_pos[1] == hole_positions[player_layer-1][1]:
        player_layer -= 1
      else:
        print("You can't move that way!")
        move_player()
    else:
      print("You can't move that way!")
      move_player()
  elif move == "stay":
    return
  else:
    print("Invalid Movements. (Forwards, Backwards, Left, Right, Up, Down, Stay)")
  
while True:
  if not print_board():
    break
  move_player()
      