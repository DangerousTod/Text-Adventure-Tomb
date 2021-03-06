import textwrap
import time
import random
import math
import csv

ZONEMAP = []
ZONENAME= ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
EXIT = 'exit'
ITEM = 'item'

      # 80 Columns   ########################################################L#####################

solved_places = {'ROOM_ONE':False, 'ROOM_TWO':False, 'ROOM_THREE':False, 'ROOM_FOUR':False }
zonemap = {
  'ROOM_ONE': {
	ZONENAME: 'start',
	DESCRIPTION: 
'Welcome to ROOM_ONE\n\n',
	EXAMINATION: '\n\nOptions:\n1.) EXAMINE?\n2.) ESCAPE?\n3.) TRAP?\n', 
	SOLVED: False,
	NORTH: '',
	SOUTH: 'ROOM_FOUR',
	EAST: 'ROOM_TWO',
	WEST: '',
	ITEM: 'objects separated by commas, like this, or this\n'
  },
  'ROOM_TWO': {
	ZONENAME: 'start',
	DESCRIPTION: 
'Welcome to ROOM_TWO\n\n',
	EXAMINATION: '\n\nOptions:\n1.) COMBAT ONE?\n2.) COMBAT TWO?\n3.) TRAP?\n',
	SOLVED: False,
	NORTH: '',
	SOUTH: 'ROOM_THREE',
	EAST: '',
	WEST: 'ROOM_ONE',
	ITEM: 'objects separated by commas, like this, or this\n'
  },
  'ROOM_THREE': {
	ZONENAME: 'start',
	DESCRIPTION: 
'Welcome to ROOM_THREE\n\n',
	EXAMINATION: '\n\nOptions:\n1.) COMBAT ONE?\n2.) COMBAT TWO?\n3.) TRAP?\n',
	SOLVED: False,
	NORTH: 'ROOM_TWO',
	SOUTH: '',
	EAST: 'ROOM_FOUR',
	WEST: '',
	ITEM: 'objects separated by commas, like this, or this\n'
  },
  'ROOM_FOUR': {
	ZONENAME: 'start',
	DESCRIPTION: 
'Welcome to ROOM_FOUR\n\n',
	EXAMINATION: '\n\nOptions:\n1.) RUN APPLICATION?\n2.) COMBAT TWO?\n3.) TRAP?\n',
	SOLVED: False,
	NORTH: 'ROOM_ONE',
	SOUTH: '',
	EAST: '',
	WEST: 'ROOM_THREE',
	ITEM: 'objects separated by commas, like this, or this\n'
  },
  'Exit': {
       ZONENAME: 'start',
       DESCRIPTION:
'SURVIVAL MESSAGE.\n\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0+0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-+0\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
'00000000000000000000000000000000000000000000000000000000000000000000000000000000\n'+
'0|0000000000000000000000000000000000000000000000000000000000000000000000000000|0\n'+
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
}

