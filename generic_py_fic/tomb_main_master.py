#######################################################################################################
#         developed by Jonathan Engwall, October of 2018 in Tijuana, MX                               #
#               PYTHON CMD CRUD MUD: THE TOMB INTERACTIVE FICTION                                     #
#         	ENGWALLJONATHANTHEREAL@GMAIL.COM **2018**                                             #
#######################################################################################################

import textwrap
import sys
import os
import random
import math
import csv
import functools

from time import sleep
from zonemap import *
from masterList import *
from memo import *

screen_width = 80
combat_state = 0
combat_round = 0

@memoize
def blockPrint():
  sys.stdout = open(os.devnull, 'w')
  return

@memoize
def enablePrint():
  sys.stdout = sys.__stdout__
  return

class player:
  def __init__(self):
    self.name = ''
    self.attack = 6
    self.health = 110
    self.location = 'ROOM_ONE'
    self.card = ''
    self.game_over = False

global my_player
my_player = player()

from enemy import *

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

def skill_attack_increase():
  my_player.attack += 50
  prompt()

def print_location():
  playerlocation = my_player.location.lower()
  print('\n' + my_player.location.upper() + '')
  print('' + zonemap[my_player.location][DESCRIPTION] + ' ')
  print('' + zonemap[my_player.location][ITEM] + ' ')
  prompt()

def movement_handler(destination):

  if destination.strip():
    os.system('clear')
    print('\n\n' + 'You enter the ' + destination + '.')
    my_player.location = destination
    print_location() 
  else:
    print('\nSorry...You cannot go that direction.\n')
    my_player.location = my_player.location
    prompt()

def game_over(destination):
  if destination.strip():
    os.system('clear')
    print('\n\n' + 'You enter the ' + destination + '.')
    my_player.location = destination
    print('\n' + my_player.location.upper() + '')
    print('' + zonemap[my_player.location][DESCRIPTION] + ' ')
    print('' + zonemap[my_player.location][EXAMINATION] + ' ')
    my_player.game_over == True
    sys.exit()

def player_look():
  os.system('clear')
  playerlocation = my_player.location.lower()
  if zonemap[my_player.location][SOLVED]:
    print('\n' + my_player.location.upper() + '')
  else:
    print('\n' + my_player.location.upper() + '')
    print('' + zonemap[my_player.location][DESCRIPTION] + '   ')
    print('' + zonemap[my_player.location][ITEM] + ' ')
    prompt()

def ai_intercept(combat_round, my_player, ai, whereabouts, playerlocation):
  whereabouts = ai.location.lower()
  playerlocation = my_player.location.lower()
  whereabouts = playerlocation
  combat_state = 1
  hand_to_hand_combat(combat_round, my_player, ai, whereabouts, playerlocation)

def player_move(myQuarter):
  print('North - South - East - West')
  ask = "Choose a direction: "
  destination = raw_input(ask)
  destinations = ['north', 'south', 'east', 'west']
  if destination in ['north']:
    destination = zonemap[my_player.location][NORTH]
    movement_handler(destination)
  elif destination in ['south']:
    destination = zonemap[my_player.location][SOUTH]
    movement_handler(destination)
  elif destination in ['east']:
    destination = zonemap[my_player.location][EAST]
    movement_handler(destination)
  elif destination in ['west']:
    destination = zonemap[my_player.location][WEST]
    movement_handler(destination)
  elif destination in ['escape']:
    destination = zonemap[my_player.location][EXIT]
    game_over(destination)
  else:
    print("Where is that?\nYou stay where you are.\n")

def ai_fight(my_player, ai, whereabouts, playerlocation):
  combat_round = 0
  combat_state = 1
  combat_round = combat_round
  while combat_state == 1:
    if whereabouts != playerlocation:
      time.sleep(0.02)
      ai_intercept(combat_round, my_player, ai, whereabouts, playerlocation)
    else:
      combat_state = 1
      print("" + str(ai.name.upper()) + " has found you!\n")
      print("The mad beast looks at you for a moment...\n")
      print( "" + str(ai.name.upper()) + " attacks!!!\n")
      hand_to_hand_combat(combat_round, my_player, ai, whereabouts, playerlocation)
    
def hand_to_hand_combat(combat_round, my_player, ai, whereabouts, playerlocation):
  combat_state = 1
  combat_round += 1
  while combat_state == 1:
    if my_player.health > 0:
      if ai.health > 0:
        
        player_dam_math = ((int(my_player.attack)) * (random.randint(5, 10))) - ((int(ai.attack)) * (random.randint(1, 4)))
        ai_dam_math = ((int(ai.attack)) * (random.randint(5, 10))) - ((int(my_player.attack)) * (random.randint(1, 4)))   
                               
        my_player.health -= abs(ai_dam_math)
        print "Points of damage taken: %i" % (ai_dam_math)
        ai.health -= abs(player_dam_math)
        if ai.health <= 0:
          combat_state = 0
          ai_death(ai, whereabouts)
        elif my_player.health <= 0:

          print('What a lovely youth, still so young and strong. Such a pity...Death shakes \n' +
'his head, lifts his scythe and cuts you down...Such a pity...\n\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0+0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-+0\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|00000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'0+-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0+0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'\n\n\n\nYou go on ahead, we will wait right here...\n')
          sys.exit()
        else:
          print "Points of damge you deal: %i" % (player_dam_math)
          print "Your health: %i" % (my_player.health)
          print "" + ai.name + " health: %i" % (ai.health)
          print "Combat round: " ,combat_round
          quarter = raw_input("Do you want to fight or run: \n" )
          if quarter.lower() == ('fight'):
            raw_input("Press Enter to Continue")
            hand_to_hand_combat(combat_round, my_player, ai, whereabouts, playerlocation)
           
          elif quarter.lower() == ('run'):
            player_move(quarter.lower())
                   
          else:
            print("Unknown command")
            print("The battle continues.\n")  
            hand_to_hand_combat(combat_round, my_player, ai, whereabouts, playerlocation)
    
      else:
        combat_state = 0
        ai_death(ai, whereabouts)
    else:  

      print('\nWhat a lovely youth, still so young and strong. Such a pity...Death shakes \n' +
'his head, lifts his scythe and cuts you down...Such a pity...\n\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0+0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-+0\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|00000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'0+-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0+0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'\n\n\n\nYou go on ahead, we will wait right here...\n')
      sys.exit()
  return

def ai_death(ai, whereabouts):
  print("Victory!\nThe " + ai.name +" has been defeated.")
  file = open('inventory.txt','a')
  reward = ['treasure_one','treasure_two','treasure_n']
  t_int = random.randint(0,5)
  loot = reward.pop(int(t_int))
  file.write('' + loot + '\n')
  file.close
  print "You gained a " + loot + " for your effort.\n"
  print "Your health: %i" % (my_player.health)
  ai.dead = True
  ai.location = ''
  whereabouts = ''
  combat_state = 0
  combat_round = 0
  ai = ''
  prompt()


def challenges(myAction):
  playerlocation = my_player.location
  print('' + zonemap[my_player.location][EXAMINATION] + ' ')
  commandX = raw_input("Choose your path\n1, 2, 3, or go back: ")
  commandXs = [ "1","2","3", "go back" ]
  if commandX not in commandXs:
    print("Unknown, use 1, 2, or 3")
    prompt()
  elif commandX.lower() in ["go back"]:
    prompt()
  else:
    player_commands(commandX.lower()) 


from player_challenges import *
from fortune_application import *
from player_challenges_continued import *

#######################################################################################################
#         reproduce for each room                                                                     #
#              if playerlocation in ['']:                                                             #
#         and for each challenges (specific to the number challenges)                                 #
#                if myCommandX == ('number'):                                                         #
#                  name_of_challenge()                                                                #
#######################################################################################################
#                                                                                                     #

def player_commands(myCommandX):
  playerlocation = str(my_player.location.lower())
  if playerlocation in ['room_one']:
    
    if myCommandX == ('1'):
      examine_interior_quest_object()
    elif myCommandX == ('2'):
      prep_quest_escape(playerlocation)
    elif myCommandX == ('3'):
      prep_quest_trap(playerlocation)

  if playerlocation in ['room_two']:
    if myCommandX == ('1'):
      quest_combat_one()
    elif myCommandX == ('2'):
      quest_combat_two()
    elif myCommandX == ('3'):
      prep_quest_trap(playerlocation)

  if playerlocation in ['room_three']:
    if myCommandX == ('1'):
      quest_combat_one()
    elif myCommandX == ('2'):
      quest_combat_two()
    elif myCommandX == ('3'):
      prep_quest_escape(playerlocation)

  if playerlocation in ['room_four']:
    if myCommandX == ('1'):
      run_application()
    elif myCommandX == ('2'):
      quest_combat_two()
    elif myCommandX == ('3'):
      prep_quest_trap(playerlocation)
#                                                                                                     #
#######################################################################################################
#         reproduce for each room                                                                     #
#              if playerlocation in ['']:                                                             #
#         and for each challenges (specific to the number challenges)                                 #
#                if myCommandX == ('number'):                                                         #
#                  name_of_challenge()                                                                #
#######################################################################################################

def show():
  playerlocation = my_player.location.lower()
  print("Showing...\n\nThe things you can get: ")
  with open('' + str(playerlocation) + '.txt','r+') as show_items:
    lines = show_items.read()
    print(lines)
    prompt()

def player_status(myAction):
  print "Name: %s" % (my_player.name)
  print "Health: %i\n" % (my_player.health)
  print("You are wearing:")
  file = open('wearing.txt','r+')
  garments = file.read()
  print(garments)
  file.close()

  print("And in your hands you have:")
  file = open('holding.txt','r+')
  worts = file.read()
  print(worts)
  file.close()
  prompt()

def player_clear(myAction):
  os.system('clear')
  prompt()

def player_move(myAction):
  print('North - South - East - West')
  ask = "Choose a direction: "
  destination = raw_input(ask)
  destinations = ['north', 'south', 'east', 'west']
  if destination in ['north']:
    destination = zonemap[my_player.location][NORTH]
    movement_handler(destination)
  elif destination in ['south']:
    destination = zonemap[my_player.location][SOUTH]
    movement_handler(destination)
  elif destination in ['east']:
    destination = zonemap[my_player.location][EAST]
    movement_handler(destination)
  elif destination in ['west']:
    destination = zonemap[my_player.location][WEST]
    movement_handler(destination)

def prompt():
  print('' + my_player.location.upper() + '\n')
  print('challenges - show more - move - look - options - status - quit')
  global playerlocation
  playerlocation = my_player.location
  global action
  action = raw_input("Command: ")
  actions = ['quit','look','move','options','status','challenges','show more']
  if action.lower() not in actions:
    print('Command unrecognized.\n')
    prompt()
  elif action.lower() == ("quit"):
    sys.exit()
  elif action.lower() in ['move']:
    player_move(action.lower())
    return
  elif action.lower() in ['look']:
    player_look()
  elif action.lower() in ['options']:
    player_options(action.lower())
    return
  elif action.lower() in ['status']:
    player_status(action.lower())
    return
  elif action.lower() in ['challenges']:
    challenges(action.lower())
  elif action.lower() in ['show more']:
    show()

def append_wear(clothing_c):
  file = open('wearing.txt','r+')
  isWearing = file.read()
  
  if clothing_c in isWearing:
    print("You already are wearing your " + clothing_c + "") 
    file.close()
    prompt()
    
  else:
    file = open('wearing.txt','a+')
    file.write('' + str(clothing_c) + '\n')
    file.close()
    print("You wear your " + clothing_c + '')
    prompt()


def append_WorT(weapon_or_tool_c):
  file = open('holding.txt','r+')
  isHolding = file.readlines()
  
  length = len(isHolding)
  if weapon_or_tool_c in isHolding:
    print("" + weapon_or_tool_c + " is already in your hands.")
    file.close()
    return
  elif length > 2:
    print("You only have two hands.")
    prompt()
    
  else:
    file = open('holding.txt','a+')
    file.write('' + str(weapon_or_tool_c) + '\n')
    file.close()
    print("Your " + weapon_or_tool_c + " is in your hands.")

    prompt()

def take_item(want):
  playerlocation = my_player.location.lower()
  file = open('' + str(playerlocation) + '.txt','r+')
  contents = file.read()
  
  if want in contents:
    file.close()
    file = open('' + str(playerlocation) + '.txt','r+')
    lines = file.readlines()

    next_file = open('' + str(playerlocation) + '.txt','w+')

    for line in lines:
      if line != ('' + str(want) + '\n'):
        next_file.write(line)
        continue
      continue
    file.close()
    next_file.close()   
    append_inventory(want)
  else:
    file.close()
    prompt()  
  
def append_inventory(want):
  file = open('inventory.txt','a+')
  file.write('' + str(want) + '\n')
  file.close()
  prompt()

def update_room_contents(drop_item):
  playerlocation = my_player.location.lower()
  file = open('' + str(playerlocation) + '.txt','a+')
  file.write( '' + str(drop_item) + '\n')
  file.close
  prompt()

def drop_wearing(drop_item):
  file = open('wearing.txt','r+')
  contents = file.read()
  
  if drop_item in contents:
    file.close()
    file = open('wearing.txt','r+')
    w_lines = file.readlines()
    
    next_file = open('wearing.txt','w+')

    for w_line in w_lines:
      if w_line != ('' + str(drop_item) + '\n'):
        next_file.write(w_line)
        continue         
      continue
    
    file.close()
    next_file.close()
    update_room_contents(drop_item)
  else:
    file.close()
    update_room_contents(drop_item)
    
def drop_holding(drop_item): 
  file = open('holding.txt','r+')
  contents = file.read()
  
  if drop_item in contents:
    file.close()
    file = open('holding.txt','r+')
    h_lines = file.readlines()
    
    next_file = open('holding.txt','w+')

    for h_line in h_lines:
      if h_line != ('' + str(drop_item) + '\n'):
        next_file.write(h_line)
        continue
      continue
    
    file.close()
    next_file.close()
    update_room_contents(drop_item)
  else:
    file.close()
    drop_wearing(drop_item)

def inventory_commands(myDecisionX):
  playerlocation = my_player.location.lower()
  print('\nget - wear - hold - drop - go back')
  global inventX
  inventX = raw_input("Inventory Command: ")
  if inventX.lower() not in ['get', 'wear', 'hold', 'drop', 'go back']:
    print("Unknown command. ")
    prompt()
  elif inventX.lower() == ('go back'):
    os.system('clear')
    prompt()
  elif inventX.lower() == 'get':
    file = open('' + str(playerlocation) + '.txt', 'r+')
    contents = file.read()
    print(contents)
      
    global want
    want = raw_input("What do you want to get: " )
    if want.lower() == ('go back'):
      file.close() 
      os.system('clear')
      prompt()
    elif want.lower() in contents:
      file.close()
      file = open('inventory.txt','r+')
      my_contents = file.read()
        
      if want.lower() in my_contents:
        file.close()
        print("You already have one of these.\n")
        prompt()
      else:
        print "You take the " +str(want) + " from the " +str(playerlocation)
        file.close()
        take_item(want)
    else:
        print("This " + str (want) + " you want so bad might not exist\n")
        file.close()
        prompt()

  elif inventX.lower() == 'wear':
    print('\n')
    file = open('inventory.txt','r+')
    contents = file.read()
    print(contents)

    global clothing_c
    clothing_c = raw_input("Choose item: ")
    if clothing_c.lower() == ('go back'):
      file.close()
      os.system('clear')
      prompt()
    else:
      file.close()
      file = open('clothing.txt','r+')
      isGarment = file.read()

      if clothing_c in isGarment:
        file.close()
        append_wear(clothing_c)
          
      else:
        print("That is not something you can wear.")
        file.close()
        prompt()
          
  elif inventX.lower() == 'hold':
    print('\n')
    file = open('inventory.txt','r+')
    contents = file.read()
    print(contents)
      
    global tool_or_weapon_c
    tool_or_weapon_c = raw_input("Choose item: ")
    if tool_or_weapon_c.lower() == ('go back'):
      file.close()
      os.system('clear')
      prompt()
        
    else:
      file.close()
      file = open('weaponOrTool.txt','r+')
      isWorT = file.read()
        
      if tool_or_weapon_c in isWorT:
        file.close()
        append_WorT(tool_or_weapon_c)
          
      else:
        file.close()
        print("That is not a hand held implement.")
        prompt()

  elif inventX.lower() =='drop':
    print('\n')
    file = open('inventory.txt','r+')
    contents = file.read()
    print(contents)
      
    global drop_item
    drop_item = raw_input("Choose item: ")

    if drop_item.lower() == ('go back'):
      file.close()
      os.system('clear')
      prompt()
        
    elif drop_item in contents:
      file.close()
      file = open('inventory.txt','r+')
      d_lines = file.readlines()
      
      next_file = open('inventory.txt','w+')

      for d_line in d_lines:
        if d_line != ('' + str(drop_item) + '\n'):
          next_file.write(d_line)
          continue
        continue
      file.close()
      next_file.close()
      
      print("You drop your " + str(drop_item) + " in the " + str(playerlocation) + "")
      drop_holding(drop_item)
    else:
      file.close()
      print("What is that?")
      prompt()

def player_options(myAction):
  os.system('clear')
  print('inventory - inventory commands - go back')
  opt = "Choose an option: "
  global decisionX
  decisionX = raw_input(opt)

  if decisionX.lower() not in ['inventory', 'inventory commands','go back']:
    print("Unknown command. ")
    prompt()
  elif decisionX.lower() == ('go back'):
    os.system('clear')
    prompt()
  elif decisionX.lower() == ('inventory'):
    print("You have the following in your inventory...\n")

    file = open('inventory.txt','r+')
    contents = file.read()
    print(contents)
    file.close()
    prompt()

  else: 
    decisionX.lower() == ('inventory commands')
    inventory_commands(decisionX)
  return

def title_screen():
  os.system('clear')
  print('\n')
  print('WELCOME TO: ')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('000000           NEW GAME        00000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000\n')
  title_screen_selections()


def title_screen_selections():
  choice = raw_input("Command: ")
  while choice.lower() in ['new game','quit']:
    if choice.lower() == ("quit"):
      sys.exit()
    elif choice.lower() == ("new game"):
      setup_game()
      return
    while choice.lower() not in ['new game', 'quit']:
      print("Please enter a valid command: New Game or Quit")
      choice = raw_input("Command: ")
      if choice.lower() == ("quit"):
        sys.exit()
      elif choice.lower() == ("new game"):
        setup_game()
        return

#######################################################################################################
#                                                                                                     #
#                                                 set up and main                                     #
#######################################################################################################


def inventory_stripe():
  file = open('inventory.txt','r+')
  file.close()

def holding_stripe():
  file = open('holding.txt','r+')
  file.close()

def clothing_stripe():
  file = open('clothing.txt','r+')
  file.close()

def wearing_stripe():
  file = open('wearing.txt','r+')
  file.close()

def weaponOrTool_stripe():
  file = open('weaponOrTool.txt','r+')
  file.close()

def treasure_stripe():
  file = open('treasure.txt','r+')
  file.close()


def main_game_loop():
  while my_player.game_over is False:
    prompt()

def setup_game():

  question = "\nHello, I hope you are ready for a scare. What's your name?\n"
  for character in question:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  player_name = raw_input("Your Name: ")

  my_player.name = player_name

  welcome = "Okay, " + player_name + " let's begin. You need to know a few things.\n"
  for character in welcome:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

  help = "### Verbs are available and certain language processing. The basic CMDS \n" 
  help1 = "### are: look, get, drop, hold, show more, challenges, and move. You \n"
  help2 = "### have a certain amount of Health, check this with: status, and you \n"
  help3 = "### can only explore The Tomb for a certain amount of time. Use: clock \n"
  help4 = "### to make sure you do not get trapped [ GAME NAME ]!\n"
  for character in help:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  for character in help1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  for character in help2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  for character in help3:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  for character in help4:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)

  goodluck = "\n\n\nOkay, " + player_name + " you will be you and the clock starts ticking now!!!\n"
  for character in goodluck:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.08) # was time.sleep(0.08)
  os.system('clear')

  inventory_stripe()
  holding_stripe()
  weaponOrTool_stripe()
  clothing_stripe()
  wearing_stripe()
  treasure_stripe()


#######################################################################################################
#                                                                                                     #
#                                                desc first room                                      #
#######################################################################################################

  print('\n\nROOM ONE\nWelcome to ROOM ONE.\n\n')

  main_game_loop()

title_screen()


