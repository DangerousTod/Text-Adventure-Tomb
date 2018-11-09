import sys
import os
import random
# from tomb_main_master import prompt

class Tarotcard(object):
  def __init__(self, name, firstkey, secondkey, danger, fear):
    self.name = name
    self.firstkey = firstkey
    self.secondkey = secondkey
    self.danger = danger
    self.fear = fear

  def __repr__(self):
    return '\nYour card is the {} \nwho guides you with {} and protects you \nfrom {} but beware of this danger: {} \nand rightly fear {}\n'.format(self.name, self.firstkey, self.secondkey, self.danger, self.fear)

my_card1 = Tarotcard('The Fool','capability','empowerment','your own ego','shortcuts')
my_card2 = Tarotcard('The Magician','intuition','initiation','Being aloof','to standoff')
my_card3 = Tarotcard('The High priestess','fertility','nurturing','Overindulging','addiction')
my_card4 = Tarotcard('The Empress','authority','structure','Micromanaging','overt force and order')
my_card5 = Tarotcard('The Emperor','guidance','belief','experience as a misguide','Restricting access to the gods')
my_card6 = Tarotcard('The Hierophant','love','choice','Debilitating passion','Ill-informed decisions')
my_card7 = Tarotcard('The Lovers','advancement','success','Resting on laurels','impulsive behavior')
my_card8 = Tarotcard('The Chariot','discipline','vitality','Indulgence','the sick bed')
my_card9 = Tarotcard('Strength','solitude','withdrawal','angst','hiding power')
my_card10 = Tarotcard('The Hermit','luck','revolution','gambling','fighting Nature')
my_card11 = Tarotcard('The Wheel','balance','objectivity','criticism','favoritism')
my_card12 = Tarotcard('Justice','enlightenment','reversals','yielding','laying blame')
my_card13 = Tarotcard('The Hanged Man','ending','departure','fatalism','rumination')
my_card14 = Tarotcard('Death','blending','harmony','zealotry','treachery')
my_card15 = Tarotcard('Temperance','shadow','delusion','materialism','manifest posession')
my_card16 = Tarotcard('The Devil','demolition','destruction','anachronsim','Malicious destruction')
my_card17 = Tarotcard('The Tower','hope','truth','Denial','locum lacuna')
my_card18 = Tarotcard('The Star','mystery','uncertainty','fantasy','melancholy')
my_card19 = Tarotcard('The Moon','joy','energy','delusion','boastfulness')
my_card20 = Tarotcard('The Sun','revival','invitation','inversion','disinclimant self')
my_card21 = Tarotcard('Judgement','wholeness','fullness','malice','malaise')
my_card22 = Tarotcard('The World','desire','invention','Indolence','cowardice')




#####################################itterator#for#dictionary##################################


def future_card(for_future):

  fort2 = random.randint(0,19)
  card = for_future.pop(int(fort2))
  print("\nNow I am looking at your future, prepare yourself....")
  data = eval(card)
  print data
  raw_input("\nWhen you are ready press enter\n")
  print("The fortune teller faints from her efforts.\n")
  return

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


