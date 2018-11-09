import os
import sys
import time
import random

from tomb_main_master import Player
my_player = player()

ZONENAME= ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
EXIT = 'escape'
ESCAPE = 'escape'

################################################################################
##########FOR#INSTANCE#FOLLOWING#DIRECTS#TO#DIFFERENT#PY#FILE###################
def run_application():
  print("'Place your hand on the deck...\n'")
  print("She seems dizzy, 'I see now and I see then...I see what will be...'\n")
  raw_input("\n<<When you are ready hear your fortune press enter>>\n\n")
  past_card()

################################################################################

def quest_escape(playerlocation):

  destination = zonemap[my_player.location][EXIT]
  game_over(destination)

def prep_quest_escape(playerlocation):
  if combat_state == 0:
    quest_escape(playerlocation)
  else:
    print "There is no escaping the [GAME NAME] for the hunted!"
    return

def quest_combat_one():

  print("ai message\n")

  my_player = player()
  ai = monster_one()
  whereabouts = ai.location.lower()
  playerlocation = my_player.location.lower()
  ai_fight(my_player, ai, whereabouts, playerlocation)

def quest_combat_two():
  print("Scare message\n")
  time.sleep(0.05)
  monster_two_attack()

def monster_two_attack():
  print("Someone is behind you!\n")
  my_player = player()
  ai = monster_one()
  whereabouts = ai.location.lower()
  playerlocation = my_player.location.lower()
  ai_fight(my_player, ai, whereabouts, playerlocation)

def quest_trap():

  thrownout = "This is a trap\n"
  thrownout1 = "Trap City\n"
  thrownout2 = "Angry scary trap stuff\n"
  thrownout3 = "Tossed out, maybe dead too!\n"
  thrownout4 = "Monster Movie Rules!\nGAME OVER\n"
  thrownout5 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout6 = "0+0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-+0\n"
  thrownout7 = "0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n"
  thrownout8 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout9 = "0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n"
  thrownout10 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout11 = "0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n"
  thrownout12 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout13 = "0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n"
  thrownout14 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout15 = "0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n"
  thrownout16 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout17 = "0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n"
  thrownout18 = "0+-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0+0\n"
  thrownout19 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout20 = "\n\n\n\nYou go on ahead, we will wait right here...\n"

  for character in thrownout:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  for character in thrownout1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  for character in thrownout2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  for character in thrownout3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  for character in thrownout4:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout5:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout6:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout7:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout8:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout9:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout10:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout11:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout12:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  for character in thrownout13:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  for character in thrownout14:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout15:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout16:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout17:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout18:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout19:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  for character in thrownout20:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
    sys.exit()

def pre_quest_trap(playerlocation):
  if combat_state == 0:
    quest_trap()
  else:
    print "There is no escaping the [GAME NAME] for the hunted!"
    return
