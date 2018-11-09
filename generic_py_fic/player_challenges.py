import sys
import os

global my_player
#my_player = player()

def get_quest_item():

  file = open('inventory.txt','r')
  my_contents = file.read()
        
  if '<quest item>' in my_contents:
    file.close()
    print("You already have one of these.\n")
    return
#    prompt()
  else:
    file.close()
    file = open('inventory.txt','a')
    file.write('<quest item>\n')
    file.close
    skill_attack_increase()

def examine_interior_quest_object():
  print("You pull aside the curtain to reveal a <quest item>.\n")
  cmd = raw_input("Type: 'get <quest item>' to pick it up! ")
  if cmd in ['get <quest item>']:
    get_quest_item()
  elif cmd in ['go back']:
    return
#    prompt()
  else:
    cmd2 = raw_input("Try again, Exactly: 'get <quest item>' to pick it up! ")
    if cmd2 in ['get <quest item>']:
      get_quest_item()
    elif cmd2 in ['go back']:
      return
#      prompt()
    else:
      print("You will get it next time")
      return
#      prompt()

