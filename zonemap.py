import textwrap
import time
import random
import math
import csv
##############################################################################
#  SWORD + FORTUNE + GOLD = YOU WIN PLAY THE NEXT MODULE SOON!               #
##############################################################################
#
ZONEMAP = []
ZONENAME= ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
EXIT = 'north'
DEATH = 'death'
ESCAPE = 'escape'
NO_MOVE = 'no_move'
ITEM = 'item'


solved_places = {'Great_Hall':False, 'Long_Hall':False, 'Trophy_Room':False, 'Trophy_Room_Vampire':False, 'Kitchen':False, 'You_Killed_The_Vampire':False, 'You_Killed_The_Zombie':False }

zonemap = {
  'Great_Hall': {
	ZONENAME: 'start',
      # 80 Columns   ########################################################L#####################
	DESCRIPTION: 
'A flurry of bats suddenly flaps through the doorway, their screeching barely \n' +
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
'can fix it.\n\n',
	EXAMINATION: '\n\nOptions:\n1.) Examine Bookshelf?\n2.) Check Behind The Curtain?\n3.) Open The Glass Door Of The Clock?\n',
        #EXAMINATION_ONE: Examine Bookshelf, bookshelf You might fall to the floor
        #EXAMINATION_TWO: Check Behind The Curtain, curtain Here is the sword
        #EXAMINATION_THREE: Open The Glass Door Of The Clock, fix-clock You can pull on the chains getting greasy
	SOLVED: False,
	NORTH: '',
	SOUTH: '',
	EAST: 'Trophy_Room',
	WEST: '',
	ITEM: 'Bookshelf, Old Paintings, Clock, Curtain\n'
  },
  'Long_Hall': {
	ZONENAME: 'start',
      # 80 Columns   ########################################################L#####################
	DESCRIPTION: 
'You enter a long hall and your steps echo. Looking about, you\'re uncertain \n' + 
'why, but then a wall vanishes and reveals an enormous chamber. The wall was \n' +
'an illusion and whoever cast it must be nearby!\n\n'+
'To the North is a Door\n'+
'To the East is a Door\n\n'+
'You spin around looking in every direction quickly. It seems you are in the \n' +
'entrance room to this mansion where the curtains and clock were, the room full\n' +
'of cobwebs and books. The wall where the paintings hung is right in front of \n' +
'you, you are simply on the other side of it!\n\n' +
'A woman appears. There is a door to the north, back to the entrance or maybe \n' +
'you could flee back to the east, through the kitchen.\n',
	EXAMINATION: '\n\nOptions:\n1.) Hear Your Fortune?\n2.) Escape This Haunted Mansion?\n3.) Run From The Fortune Teller?\n',
      #  EXAMINATION_FOUR: Do You Have The Sword, sword She will offer a fortune telling
      #  EXAMINATION_FIVE: Go North To Escape, north You can escape
      #  EXAMINATION_SIX: Run East To The Kitchen, east She sends a Zombie after you
	SOLVED: False,
	NORTH: 'Great_Hall',
	SOUTH: '',
	EAST: 'Kitchen',#First: Zombie Fight
	WEST: '',
        ESCAPE: 'Exit',#Oh yes, you can run
	ITEM: 'Fortune Teller, Small Table, Coat Rack\n'
  },
  'Trophy_Room': {
	ZONENAME: 'start',
      # 80 Columns   ########################################################L#####################
	DESCRIPTION: 
'Neither light nor darkvision can penetrate the gloom in this chamber. An \n' + 
'unnatural shade fills it, and the room\'s farthest reaches are barely \n' +
'visible. Near the room\'s center, you can just barely perceive a lump about \n' +
'the size of a human lying on the floor.\n\n'+
'To the South is a Door\n'+
'To the West is a Door\n\n' +
'You creep slowly into the gloom. The carpet crunches under your feet. Even a \n'+
'flashlight with full batteries cannot help you make out the fingers of you own\n'+
'hand before your face. You bump into a statue and hear the quiet tinkling of \n'+
'bells, but from where?\n\n',
	EXAMINATION: '\n\nOptions:\n1.) Examine The Statue?\n2.) Investigate The Mysterious Lump?\n3.) Try to find the source of the tinkling bells?\n',
     #   EXAMINATION_SEVEN: Examine The Statue, statue Has a cloak around shoulders
     #   EXAMINATION_EIGHT: Investigate The Mysterious Lump, lump Vampire flees to coffin-is daytime
     #   EXAMINATION_NINE: Try to find the source of the tinkling bells, bells 
	SOLVED: False,
	NORTH: '',
	SOUTH: 'Kitchen',
	EAST: '',
	WEST: 'Great_Hall',#Pretty smart start for an adventurer
	ITEM: 'Carpet, Statue, Animal Head Trophies, Coffin\n'
  },
  'Trophy_Room_Vampire': {
	ZONENAME: 'start',
      # 80 Columns   ########################################################L#####################
	DESCRIPTION: 
'Neither light nor darkvision can penetrate the gloom in this chamber. An \n' + 
'unnatural shade fills it, and the room\'s farthest reaches are barely \n' +
'visible.\n\n'+
'To the South is a Door\n'+
'To the West is a Door\n\n' +
'You creep slowly into the gloom. The carpet crunches softly. \n' +
'You hear terrifying laughter, but from from where?\n\n',
	EXAMINATION: '\n',
     #   EXAMINATION_SEVEN: Examine The Statue, statue Has a cloak around shoulders
     #   EXAMINATION_EIGHT: Investigate The Mysterious Lump, lump Vampire flees to coffin-is daytime
     #   EXAMINATION_NINE: Try to find the source of the tinkling bells, bells 
	SOLVED: False,
	NORTH: '',
	SOUTH: 'Kitchen',
	EAST: '',
	WEST: 'Great_Hall',#Pretty smart start for an adventurer
	ITEM: 'Carpet, Statue, Animal Head Trophies, Coffin\n'
  },
  'Kitchen': {
	ZONENAME: 'start',
      # 80 Columns   ########################################################L#####################
	DESCRIPTION: 
'A crack in the ceiling above the middle of the north wall allows a trickle \n' +
'of water to flow down to the floor. The water pools near the base of the \n' +
'wall, and a rivulet runs along the wall an out into the hall. The water \n' +
'smells fresh. Through grimy windows you see a clue as to why such terrible \n' +
'things have happened here: behind this terrible house is a tiny graveyard \n' +
'buried in moss and weeds.\n\n' +
'To the North is a Door\n' +
'To the West is a Door\n\n' +
'A greybearded man emerges from the gardener\'s shed. He lets the door slam \n' +
'shut with a loud metal bang! Just then you notice a beautiful wooden box on \n' +
'top of an old table. Beside the box is a huge tarantula spider!\n\n',
	EXAMINATION: '\n\nOptions:\n1.) Hide From The Gardener?\n2.) Open Wooden Box?\n3.) Squish The Spider?\n',
     #   EXAMINATION_TEN: Hide From The Gardener, gardener Better hide, he will remember
     #   EXAMINATION_ELEVEN: Open Wooden Box, box Treasure! Spanish gold! We are rich!
     #   EXAMINATION_TWELVE: Squish The Spider, spider Gardener enters, fun is over
	SOLVED: False,
	NORTH: 'Trophy_Room_Vampire',#Did you forget about the Vampire???
	SOUTH: '',
	EAST: '',
	WEST: 'Long_Hall',
  #      ESCAPE: 'Exit',
	ITEM: 'Table, Spider\n'
  },
  'Death': {
        ZONENAME: 'start',
        DESCRIPTION:
'What a lovely youth, still so young and strong. Such a pity...Death shakes \n' +
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
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
        EXAMINATION: '\n\n\n\nYou go on ahead, we will wait right here...\n',
	NORTH: '',
	SOUTH: '',
	EAST: '',
	WEST: ''
  },
  'Exit': {
       ZONENAME: 'start',
       DESCRIPTION:
'You bolt from the door of the mansion. Jump on your bike and start pumping \n' +
'the pedals. You feel incredible. Somehow terrified and thrilled at the same \n' +
'time. You have a prickly feeling you will be back.\n\n'+
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
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n',
        EXAMINATION: '\n\n\n\nYou go on ahead, we will wait right here...\n',
	NORTH: '',
	SOUTH: '',
	EAST: '',
	WEST: ''
  },
#  'You_Killed_The_Vampire': {
#	ZONENAME: 'start',
      # 80 Columns   ########################################################L######################
#	DESCRIPTION: 
#'Neither light nor darkvision can penetrate the gloom in this chamber. An \n' + 
#'unnatural shade fills it, and the room\'s farthest reaches are barely \n' +
#'visible.\n\n'+
#'To the South is a Door\n'+
#'To the West is a Door\n\n' +
#'You creep slowly into the gloom. You hear quiet laughter, but from where?\n\n',
#	EXAMINATION: 'Try to find the source of the laughter?\n',

     #   EXAMINATION_THIRTEEN: ,vampire fight 
#	SOLVED: False,
#	NORTH: '',
#	SOUTH: 'Kitchen',
#	EAST: '',
#	WEST: 'Great_Hall',#Pretty smart start for an adventurer
#	ITEM: 'Carpet, Statue, Animal Head Trophies, Coffin\n'
#  },
# 'You_Killed_The_Zombie': {
#	ZONENAME: 'start',
      # 80 Columns   ########################################################L#####################
#	DESCRIPTION: 
#'"A true warrior!" The woman is stunned. "Please sit at my table and let me \n' +
#'tell you your fortune. We are few, and we need warriors like you! Our land is \n' +
#'far away, a journey through both time and space, but we would reward you! Now \n' +
#'sit and let me tell you of the things that await you!"\n\n'+
#'To the North is a Door\n'+
#'To the East is a Door\n\n',
#	EXAMINATION: 'Accept Her Offer?\nGo North To Escape?\n',
   #     EXAMINATION_FOUR: Do You Have The Sword, gratitude She will offer a fortune telling
   #     EXAMINATION_FIVE: Go North To Escape, north You can escape
#	SOLVED: False,
#	NORTH: 'Exit',#victory message also
#	SOUTH: '',
#	EAST: 'Kitchen',
#	WEST: '',
#	ITEM: 'Table, Spider\n',
#  },
}

