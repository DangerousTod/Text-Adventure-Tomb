
class vampire:
  def __init__(self):

    self.name = 'Vampire'
    self.attack = 5
    self.health = 100
    self.location = 'Tropy_Room'
    self.dead = False
import sys
import os

class zombie:
  def __init__(self):

    self.name = 'zombie'
    self.attack = 5
    self.health = 50
    self.location = 'Kitchen'
    self.dead = False

# global my_player
# my_player = player()

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

