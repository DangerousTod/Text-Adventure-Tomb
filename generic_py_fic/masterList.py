import os
import sys

class carpet:
  def __init(self):
    self.name = 'carpet'
    self.description ='Thick brown and red carpet very old and very dusty.\n',
    self.location = 'Trophy Room'

class statue:
   def __init(self):
    self.name = 'statue'
    self.description ='A carved wooden statue wearing a cloak\n',
    self.location = 'Trophy Room'

class animal_head_Trophies:
   def __init(self):
    self.name = 'animal head trophies'
    self.description = 'Several severed heads of big game and carnivores mounted on the walls.\n',
    self.location = 'Trophy Room'

class coffin:
  def __init(self):
    self.name = 'coffin'
    self.description = 'Standing in the corner of this room is a coffin made of carved stone.\n',
    self.location = 'Trophy Room'

class cloak:
   def __init(self):
    self.name = 'cloak'
    self.description ='A thick cloak that protects the shoulders, back and head.\n',
    self.location = 'Trophy Room'

class bookshelf:
  def __init(self):
    self.name = 'bookshelf'
    self.description ='Hundreds of old books stand on the dusty shelves. Books in every color shape, binding, size and on dozens and dozens of peculiar subjects.\n' ,
    self.location = 'Great Hall'


class old_paintings:
  def __init__(self):
    self.name = 'old paintins'
    self.description = 'Someone was fond of painting with dogs beside a fire. Many have a young man or boy, only half the size of the armored man who stands mighty beside the fire with a rod in his hand a stern look on his face. Many however feature a plump woman with a powdered face or exploding curls on her head. Again beside her are often dogs and a small sized man.\n',
    self.location = 'Great Hall'

class clock:
  def __init__(self):
    self.name = 'clock'
    self.description = ''
    self.location = 'Great Hall'

class curtain:
  def __init__(self):
    self.name = 'curtain'
    self.description = ''
    self.location = 'Great Hall'

class attack:
  def __init__(self, attack):
    self.attack = attack

class sword(attack):
  def __init__(self):
    attack.__init__(self, attack)
    self.name = 'sword'
    self.description = ''
    self.location = 'Great Hall'
    self.attack = 50
  
class rake: 
  def __init__(self):
    self.name = 'rake'
    self.description = ''
    self.location = 'Kitchen'

class shovel: 
  def __init__(self):
    attack.__init__(self, attack)
    self.name = 'shovel'
    self.description = ''
    self.location = 'Kitchen'
    self.attack = 20

class pots_and_pans: 
  def __init__(self):
    self.name = 'pots and pans'
    self.description = ''
    self.location = 'Kitchen'

class table: 
  def __init__(self):
    self.name = 'table'
    self.description = ''
    self.location = 'Kitchen'

class box:
  def __init__(self):
    self.name = 'box'
    self.description = ''
    self.location = 'Kitchen'

class spider:
  def __init__(self):
    self.name = 'spider'
    self.description = ''
    self.location = 'Kitchen'

class fortune_teller: 
  def __init__(self):
    self.name = 'fortune teller'
    self.description = ''
    self.location = 'Long Hall'

class small_table:
  def __init__(self):
    self.name = 'small table'
    self.description = ''
    self.location = 'Long Hall'

class coat_rack:
  def __init__(self):
    self.name = 'coat rack'
    self.description = ''
    self.location = 'Long Hall'

class umbrella:
  def __init__(self):
    self.name = 'umbrella'
    self.description = ''
    self.location = 'Long Hall'
