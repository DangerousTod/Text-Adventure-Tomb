
import textwrap
import sys
import os
import random
import math
import csv
import functools

from time import sleep
from zonemap import *
from tarotzone import *
from masterList import *
from memo import *

screen_width = 80

combat_state = 0
combat_round = 0

#ai = 0

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
#    self.status_scares = []
    self.location = 'Great_Hall'
    self.card = ''
    self.game_over = False


class vampire:
  def __init__(self):

    self.name = 'Vampire'
    self.attack = 5
    self.health = 100
    self.location = 'Tropy_Room'
    self.dead = False
    self.loot = ['sunscreen', 'wand']

class zombie:
  def __init__(self):

    self.name = 'zombie'
    self.attack = 5
    self.health = 50
    self.location = 'Kitchen'
    self.dead = False
    self.loot = ['rags','old belt','copper key']

global my_player
my_player = player()

global ai
ai = vampire()
ai = zombie()


#class ai:
#  def __init__(self):
#    self.name = ''
#    self.attack = attack
#    self.health = 20
#    self.location = ''
#    self.dead = False
#    self.loot = []
#global ai
#ai = ai()

#class bats(ai):
#  def __init__(self):
#    ai.__init__(self)
#    self.name = 'bats'
#    self.attack = 10
#    self.health = 20
#    self.dead = False
#    self.location = 'Trophy_Room'




#aiList = [ bats, vampire, zombie ]

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

def title_screen():
  os.system('clear')
  print('\n')
  print('WELCOME TO: ')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('000            0  0000  0       0          00         0  00000  0        0000000')
  print('000 0000  0000 0  0000  0 00000 0 000  000 00 0000000 0   000   0 000000  000000')
  print('000 0000  0000 0  0000  0 0000000 000  000 00 0000000 0 0 000 0 0 000000  000000')
  print('00000000  000000  0000  0    00000000  000000 0000000 0 00 0 00 0       00000000')
  print('00000000  000000        0 00000000000  000000 0000000 0 00 0 00 0 000000  000000')
  print('00000000  000000  0000  0 00000 00000  000000 0000000 0 00   00 0 000000  000000')
  print('00000000  000000  0000  0       00000  000000         0 000 000 0        0000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000')
  print('000000           NEW GAME        HELP      or     RESUME                  000000')
  print('00000000000000000000000000000000000000000000000000000000000000000000000000000000\n')
  title_screen_selections()



# '''
# ##  ##  ##   ##
# ###########  ##
# ## ##### ##   #
# ### ### ###  ##
# ###########
# '''

ZONENAME= ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
EXIT = 'escape'
DEATH = 'death'
ESCAPE = 'escape'

solved_places = {'Top Left Corner Room':False, 'Lower Left Room':False, 'Top Right Room':False, 'Lower Right Room':False, } # '':False, '':False, '':False, '':False,
#                 '':False, '':False, '':False, '':False, '':False, '':False, '':False, '':False,
#                 '':False, '':False, '':False, '':False, '':False, '':False, '':False, '':False,
#                 '':False, '':False, '':False, '':False, '':False, '':False, '':False, '':False,
#                 '':False, '':False, '':False, '':False, '':False, '':False, '':False, '':False,
#                 '':False, '':False, '':False, '':False, '':False, '':False, '':False, '':False,
#                }

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

 ################################################################################
#                                                                                #
#                          OUR VILLAINS                                          #
# ai = bats(Bats, 10, 20, 'Great_Hall', False, ['gold coin'])                    #
# ai = vampire(Vampire, 15, 75, 'Trophy_Room', False, ['sunscreen', 'wand'])     #
# ai = zombie(Zombie, 5, 30, 'Kitchen', False, ['old boots','copper key'])       #
#                                                                                #
 ################################################################################

def ai_intercept(combat_round, my_player, ai, whereabouts, playerlocation):
  whereabouts = ai.location.lower()
  playerlocation = my_player.location.lower()
#  if whereabouts != playerlocation:
#    sleep(0.10)
  whereabouts = playerlocation
#    print(ai.speak())
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



def ai_fight(my_player, ai, whereabouts, playerlocation):
  combat_round = 0
  combat_state = 1
  combat_round = combat_round
  while combat_state == 1:
    if whereabouts != playerlocation:
      time.sleep(0.02)
#      ai.location = my_player.location
#      ai_fight(my_player, ai, whereabouts, playerlocation)
#      time.sleep(0.06)
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


#    while combat_round % 3 != 0:                       
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
'0|0            0  0000  0       0          00         0  00000  0        00000|0\n'+
'000 0000  0000 0  0000  0 00000 0 000  000 00 0000000 0   000   0 000000  000000\n'+
'0|0 0000  0000 0  0000  0 0000000 000  000 00 0000000 0 0 000 0 0 000000  0000|0\n'+
'00000000  000000  0000  0    00000000  000000 0000000 0 00 0 00 0       00000000\n'+
'0|000000  000000        0 00000000000  000000 0000000 0 00 0 00 0 000000  0000|0\n'+
'00000000  000000  0000  0 00000 00000  000000 0000000 0 00   00 0 000000  000000\n'+
'0|000000  000000  0000  0       00000  000000         0 000 000 0        00000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'0+-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0+0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'\n\n\n\nYou go on ahead, we will wait right here...\n')
          sys.exit()
        else:
 #         return combat_round
          print "Points of damge you deal: %i" % (player_dam_math)
   #       combat_round += 1
          print "Your health: %i" % (my_player.health)
          print "" + ai.name + " health: %i" % (ai.health)
          print "Combat round: " ,combat_round
          quarter = raw_input("Do you want to fight or run: \n" )
          if quarter.lower() == ('fight'):
   #         combat_round += 1
            raw_input("Press Enter to Continue")
  #        return combat_round
            hand_to_hand_combat(combat_round, my_player, ai, whereabouts, playerlocation)
           
          elif quarter.lower() == ('run'):
            player_move(quarter.lower())
                   
          else:
            print("Unknown command")
            print("The battle continues.\n")  
            hand_to_hand_combat(combat_round, my_player, ai, whereabouts, playerlocation)
    
      else:
        combat_state -= 1
        ai_death(ai, whereabouts)
    else:  
     
      print('What a lovely youth, still so young and strong. Such a pity...Death shakes \n' +
'his head, lifts his scythe and cuts you down...Such a pity...\n\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0+0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-+0\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0            0  0000  0       0          00         0  00000  0        00000|0\n'+
'000 0000  0000 0  0000  0 00000 0 000  000 00 0000000 0   000   0 000000  000000\n'+
'0|0 0000  0000 0  0000  0 0000000 000  000 00 0000000 0 0 000 0 0 000000  0000|0\n'+
'00000000  000000  0000  0    00000000  000000 0000000 0 00 0 00 0       00000000\n'+
'0|000000  000000        0 00000000000  000000 0000000 0 00 0 00 0 000000  0000|0\n'+
'00000000  000000  0000  0 00000 00000  000000 0000000 0 00   00 0 000000  000000\n'+
'0|000000  000000  0000  0       00000  000000         0 000 000 0        00000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'0+-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0+0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'\n\n\n\nYou go on ahead, we will wait right here...\n')
      sys.exit()

  return

#def ai_death(combat_round, my_player, ai, whereabouts, playerlocation):
def ai_death(ai, whereabouts):
  print("Victory!")

  print "Your health: %i" % (my_player.health)
  file = open('inventory.txt','w+')
  file.write("" + str(ai.loot) + "\n")
#    file.remove(""+ str(ai.name()) + "")
  file.close()
  print("The " + ai.name +" has been defeated.")

  ai.dead = True
  ai.location = ''
  whereabouts = ''
  combat_state = 0
  combat_round = 0
  ai = ''
  prompt()


##############################################################################################
##############################################################################################


def examine_bookshelf():
  pass

def get_sword():

  file = open('inventory.txt','r')
  my_contents = file.read()
        
  if 'bronze sword' in my_contents:
    file.close()
    print("You already have one of these.\n")
    prompt()
  else:
    file.close()
    my_player.attack += 50
    file = open('inventory.txt','a')
    file.write('bronze sword\n') ##############################################
    file.close
    return #player.attack

def examine_curtain():
  print("You pull aside the curtain to reveal a bronze short sword.\n")
  cmd = raw_input("Type: 'get sword' to pick it up! ")
  if cmd in ['get sword']:
    get_sword()
  elif cmd in ['go back']:
    prompt()
  else:
    cmd2 = raw_input("Try again, Exactly: 'get sword' to pick it up! ")
    if cmd2 in ['get sword']:
      get_sword()
    elif cmd2 in ['go back']:
      prompt()
    else:
      print("You will get it next time")
      prompt()
###############################################################################################




###############################################################################################

class Tarotcard(object):
  def __init__(self, name, firstkey, secondkey, danger, fear):
    self.name = name
    self.firstkey = firstkey
    self.secondkey = secondkey
    self.danger = danger
    self.fear = fear

  def __repr__(self):
    return '\nYour card is the {} \nwho guides you with {} and protects you \nfrom {} but beware of this danger: {} \nand rightly fear {}\n'.format(self.name, self.firstkey, self.secondkey, self.danger, self.fear)

my_card1 = Tarotcard('the_fool','capability','empowerment','your own ego','shortcuts')
my_card2 = Tarotcard('the magician','intuition','initiation','Being aloof','to standoff')
my_card3 = Tarotcard('the high priestess','fertility','nurturing','Overindulging','addiction')
my_card4 = Tarotcard('the empress','authority','structure','Micromanaging','overt force and order')
my_card5 = Tarotcard('the emperor','guidance','belief','experience as a misguide','Restricting access to the gods')
my_card6 = Tarotcard('the hierophant','love','choice','Debilitating passion','Ill-informed decisions')
my_card7 = Tarotcard('the lovers','advancement','success','Resting on laurels','impulsive behavior')
my_card8 = Tarotcard('the chariot','discipline','vitality','Indulgence','the sick bed')
my_card9 = Tarotcard('strength','solitude','withdrawal','angst','hiding power')
my_card10 = Tarotcard('the hermit','luck','revolution','gambling','fighting Nature')
my_card11 = Tarotcard('the wheel','balance','objectivity','criticism','favoritism')
my_card12 = Tarotcard('justice','enlightenment','reversals','yielding','laying blame')
my_card13 = Tarotcard('the hanged man','ending','departure','fatalism','rumination')
my_card14 = Tarotcard('death','blending','harmony','zealotry','treachery')
my_card15 = Tarotcard('temperance','shadow','delusion','materialism','manifest posession')
my_card16 = Tarotcard('the devil','demolition','destruction','anachronsim','Malicious destruction')
my_card17 = Tarotcard('the tower','hope','truth','Denial','locum lacuna')
my_card18 = Tarotcard('the star','mystery','uncertainty','fantasy','melancholy')
my_card19 = Tarotcard('the moon','joy','energy','delusion','boastfulness')
my_card20 = Tarotcard('the sun','revival','invitation','inversion','disinclimant self')
my_card21 = Tarotcard('judgement','wholeness','fullness','malice','malaise')
my_card22 = Tarotcard('the world','desire','invention','Indolence','cowardice')




###############################################################################################


def future_card(for_future):

  fort2 = random.randint(0,19)
  card = for_future.pop(int(fort2))
  print("\nNow I am looking at your future, prepare yourself....")
  data = eval(card)
  print data
  raw_input("\nWhen you are ready press enter\n")
  print("The fortune teller faints from her efforts.\n")
  prompt()

def present_card(for_present):

  fort1 = random.randint(0,20)
  card = for_present.pop(int(fort1))
  print("\nNow I see your present, today even this moment....")
  data = eval(card)
  print data

  for_future = for_present
  raw_input("\nWhen you are ready press enter\n")
  future_card(for_future)

def past_card():
  for_past = ['my_card1','my_card2','my_card3','my_card4','my_card5','my_card6','my_card7','my_card8','my_card9','my_card10','my_card11','my_card12','my_card13','my_card14','my_card15','my_card16','my_card17','my_card18','my_card19','my_card20','my_card21','my_card22']

  fort = random.randint(0,21)
  card = for_past.pop(int(fort))
  print("\nI will look into your past....")
  data = eval(card)
  print data

  for_present = for_past
  raw_input("\nWhen you are ready press enter\n")
  present_card(for_present)


###############################################################################################

def hear_fortune():
  print("'Place your hand on the deck...\n'")
  print("She seems dizzy, 'I see now and I see then...I see what will be...'\n")
  raw_input("\n<<When you are ready hear your fortune press enter>>\n\n")
  past_card()
#  past_card_handler()
#  print(my_card15)

def escape():
  destination = zonemap[my_player.location][EXIT]
  game_over(destination)


def run_from_fortuneteller():

  print("The fortune teller screams: 'No one runs from me!\n")

  my_player = player()
  ai = zombie()
  whereabouts = ai.location.lower()
  playerlocation = my_player.location.lower()
  ai_fight(my_player, ai, whereabouts, playerlocation)

#  ai = zombie(Zombie, 5, 30, 'Kitchen', False, ['old boots','copper key'])
#  hand_to_hand(whereabouts, playerlocation, player, ai)

def fix_clock():
  pass


def fortune_and_sword():
  pass


def get_cloak():

  file = open('inventory.txt','r')
  my_contents = file.read()
        
  if 'cloak' in my_contents:
    file.close()
    print("You already have one of these.\n")
    prompt()
  else:
    file.close()
    my_player.attack += 20
    file = open('inventory.txt','a')
    file.write('cloak\n')
    file.close
    prompt()

def examine_statue():
  print("Hanging over the statue's shoulders is a heavy cloak. It looks like \n" +
"great protection and a lot flashier than anything anybody at school will ever \n" +
"have.\n")
  cmd = raw_input("Type: 'get cloak' to pick it up! ")
  if cmd in ['get cloak']:
    get_cloak()
  elif cmd in ['go back']:
    prompt()
  else:
    cmd2 = raw_input("Try again, Exactly: 'get cloak' to pick it up! ")
    if cmd2 in ['get cloak']:
      get_sword()
    elif cmd2 in ['go back']:
      prompt()
    else:
      print("You will get it next time")
      prompt()

def investigate_lump():
 ######################                         #########
  print("You cautiosly approach the lump in the center of the room. It is so like \n" +
"like the shape and size of a person you expect it to wake up, or at least \n" +
"breathe. But it does nothing. It just lies there. \n" +
"Since when was there a REAL haunted house in THIS neighborhood?\n" +
"It is too scary, you have to back away!\n")
  time.sleep(0.05)
  vampire_attack()

def vampire_attack():
  

  print("Someone is behind you!\n")
 # ai = VampireAI
#  ai = vampire()        ####################################### ###########33 ############

  my_player = player()
  ai = vampire()
  whereabouts = ai.location.lower()
  playerlocation = my_player.location.lower()
  ai_fight(my_player, ai, whereabouts, playerlocation)
#  return my_player, ai, whereabouts, playerlocation;


def tinkling_bells():
  pass


def hide_from_the_gardener():
  print("You duck down to avoid the gardener. Who knew there would be anyone here?\n")

def get_coins():
#    player.attack += 50 // maybe magic points in later versions or adventures
  file = open('inventory.txt','a')
  file.write('Thirty gold coins\n')
  file.close
  prompt()
  

def open_wooden_box():
  print("The small wooden box opens slowly on rusty hinges.\nInside are a couple dozen gold coins!")
  cmd = raw_input("Type: 'get coins' you can get rich like this! ")
  if cmd in ['get coins']:
    get_coins()

# 00000000000000000000000000000000000000000000000000000000000000000000000000000000
def squish_spider():
#  playerlocation = my_player.location.lower()
  thrownout = "Just as you lift your foot to squish the tarantula spider a door you did not \n"
  thrownout1 = "at first notice flies open. The gardener stomps in. He shouts: 'I knew I heard \n"
  thrownout2 = "something going on in here! You better not ever come back to this house!' \n"
  thrownout3 = "He deposits you on the curb.\n"

  thrownout4 = "This house is Off-Limits!\nGAME OVER\n"
  thrownout5 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout6 = "0+0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-+0\n"
  thrownout7 = "0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n"
  thrownout8 = "00000000000000000000000000000000000000000000000000000000000000000000000000000000\n"
  thrownout9 = "0|0            0  0000  0       0          00         0  00000  0        00000|0\n"
  thrownout10 = "000 0000  0000 0  0000  0 00000 0 000  000 00 0000000 0   000   0 000000  000000\n"
  thrownout11 = "0|0 0000  0000 0  0000  0 0000000 000  000 00 0000000 0 0 000 0 0 000000  0000|0\n"
  thrownout12 = "00000000  000000  0000  0    00000000  000000 0000000 0 00 0 00 0       00000000\n"
  thrownout13 = "0|000000  000000        0 00000000000  000000 0000000 0 00 0 00 0 000000  0000|0\n"
  thrownout14 = "00000000  000000  0000  0 00000 00000  000000 0000000 0 00   00 0 000000  000000\n"
  thrownout15 = "0|000000  000000  0000  0       00000  000000         0 000 000 0        00000|0\n"
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

#############################################################################
#
#
#    destination = zonemap[my_player.location.upper()][EXIT]
#    game_over(destination)
#
#
#############################################################################

def player_commands(myCommandX):
  playerlocation = str(my_player.location.lower())
#  playerlocations == [ 'great_hall','trophy_room','long_hall','kithchen' ]
  if playerlocation in ['great_hall']:
    
    if myCommandX == ('1'):
      examine_bookshelf()
    elif myCommandX == ('2'):
      examine_curtain()
    elif myCommandX == ('3'):
      fix_clock()

  if playerlocation in ['trophy_room']:
    if myCommandX == ('1'):
      examine_statue()
    elif myCommandX == ('2'):
      investigate_lump()
    elif myCommandX == ('3'):
      tinkling_bells()

  if playerlocation in ['long_hall']:
    if myCommandX == ('1'):
      hear_fortune()
    elif myCommandX == ('2'):
      escape()
    elif myCommandX == ('3'):
      run_from_fortuneteller()

  if playerlocation in ['kitchen']:
    if myCommandX == ('1'):
      hide_from_the_gardener()
    elif myCommandX == ('2'):
      open_wooden_box()
    elif myCommandX == ('3'):
      squish_spider()

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


def show():
  playerlocation = my_player.location.lower()
  print("Showing...\n\nThe things you can get: ")
  with open('' + str(playerlocation) + '.txt','r') as show_items:
    lines = show_items.read()
    print(lines)
    prompt()

def player_status(myAction):
  print "Name: %s" % (my_player.name)
  print "Health: %i\n" % (my_player.health)
  print("You are wearing:")
  file = open('wearing.txt','r')
  garments = file.read()
  print(garments)
  file.close()

  print("\nAnd in your hands you have:")
  file = open('holding.txt','r')
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

def inventory_stripe():
  file = open('inventory.txt','r')
  file.close()

def holding_stripe():
  file = open('holding.txt','r')
  file.close()

def clothing_stripe():
  file = open('clothing.txt','r')
  file.close()

def wearing_stripe():
  file = open('wearing.txt','r')
  file.close()

def weaponOrTool_stripe():
  file = open('weaponOrTool.txt','r')
  file.close()

def treasure_stripe():
  file = open('treasure.txt','r')
  file.close()

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
  file = open('holding.txt','r')
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
  file = open('' + str(playerlocation) + '.txt','r')
  contents = file.read()
  
  if want in contents:
    file.close()
    file = open('' + str(playerlocation) + '.txt','r')
    lines = file.readlines()

    next_file = open('' + str(playerlocation) + '.txt','w')
    for line in lines:
      if line != ('' + str(want) + ''):
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
  file.write('\n' + str(want) + '\n')
  file.close()
  prompt()


def update_room_contents(drop_item):
  playerlocation = my_player.location.lower()
  file = open('' + str(playerlocation) + '.txt','a+')
  file.write( '\n' + str(drop_item) + '\n')
  file.close
  prompt()


def drop_wearing(drop_item):
  file = open('wearing.txt','r')
  contents = file.read()
  
  if drop_item in contents:
    file.close()
    file = open('wearing.txt','r')
    w_lines = file.readlines()
    
    next_file = open('wearing.txt','w')

    for w_line in w_lines:
      if w_line != ('' + str(drop_item) + ''):
        file.write(w_line)
        continue         
      continue
    
    file.close()
    next_file.close()
    update_room_contents(drop_item)
  else:
    file.close()
    update_room_contents(drop_item)
    

def drop_holding(drop_item): 
  file = open('holding.txt','r')
  contents = file.read()
  
  if drop_item in contents:
    file.close()
    file = open('holding.txt','r')
    h_lines = file.readlines()
    
    next_file = open('holding.txt','w')

    for h_line in h_lines:
      if h_line != ('' + str(drop_item) + ''):
        file.write(h_line)
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
    file = open('' + str(playerlocation) + '.txt', 'r')
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
      file = open('inventory.txt','r')
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
    file = open('inventory.txt','r')
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
      file = open('clothing.txt','r')
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
    file = open('inventory.txt','r')
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
      file = open('weaponOrTool.txt','r')
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
      file = open('inventory.txt','r')
      d_lines = file.readlines()
 
      next_file = open('inventory.txt','w')

      for d_line in d_lines:
        if d_line != ('' + str(drop_item) + '\n'):
          file.write(d_line)
          continue
        continue
      next_file.close()
      file.close()
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

    file = open('inventory.txt','r')
    contents = file.read()
    print(contents)
    file.close()
    prompt()

  else: 
    decisionX.lower() == ('inventory commands')
    inventory_commands(decisionX)

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
  help4 = "### to make sure you do not get trapped in The Tomb!\n"
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

  print('\n\nGREAT_HALL\nA flurry of bats suddenly flaps through the doorway, their screeching barely \n' +
'audible as they careen past your heads. They flap past you into the rooms \n' +
'and halls beyond. The room from which they came seems barren at first glance.\n\n' +
'An old clock stands at the north side of the room between two cobweb covered \n' +
'bookshelves. It clicks loudly. Its winding is too slow and the gears rattle \n' +
'with every passing tick.\n\n' +
'To the East is a Door\n\n' +
'High above the bookshelf is a large round window. It is cloudy with dirt and \n' +
'age. Another window just like it is high up on the east wall just below the \n' +
'carved wooden rafters. On the south wall are dozens of oil paintings, normal \n' +
'haunted house painting of ancestors of people who are long since gone away who\n' +
'pose like royalty wearing kilts beside a fire as dogs roll about at foot. Yet \n' +
'behind you there is no window. You turn and look and sure enough a thick black \n' +
'curtain covers nearly the entire wall. It is only pulled back enough for the \n' +
'door to swing inward.\n\n' +
'The clock rattles again. The poor thing almost seems to be in pain. Maybe you \n' +
'can fix it.\n\n')

  main_game_loop()

title_screen()
