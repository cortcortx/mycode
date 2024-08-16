#!/usr/bin/python3
 
# in use for husband to randomly be placed in different rooms each turn
import random
 
 
 
 
 
 
def showInstructions():
 
  #print a main menu and the commands
 
  print('''
 
RPG Mystery Game
 
========
 
Commands:
 
  go [direction]
 
  get [item]
 
''')
 
 
 
 
 
 
 
 
def showStatus():
 
  #print the player's current status
 
  print('---------------------------')
 
  print('You are in the ' + currentRoom)
 
  #print the current evidence
 
  print('Evidence : ' + str(evidence))
 
  #print an item if there is one
 
  if "item" in rooms[currentRoom]:
 
    print('You see a ' + rooms[currentRoom]['item'])
 
  print("---------------------------")
 
 
 
 
# TODO Add addtl methods, i.e interrogate, block,
# the monster/husband can randomly appear in any room of the home
def moveHusband():
 
    global husbandRoom
 
    possible_rooms = list(rooms.keys())
 
    #possible_rooms.remove(currentRoom)
 
    husbandRoom = random.choice(possible_rooms)
 

class Wife():
  #wife has 2 chances to be able to escape her husband if caught before completing the game
  def __init__(self):
    self.escape = 3

  def escapeHusband(self):
      # If a player enters a room with husband 
      if currentRoom == husbandRoom :
          if self.escape > 0:
            self.escape -= 1
            print(f"Ack! Your husband appears! You manage to escape but barely! You only have {self.escape} escapes left.")
            return True
          else:
            print('You have been caught by your husband... GAME OVER!')
            return False
      return True  
 

#an evidence bag, which is initially empty
 
evidence = []
 
 
 
# a dictionary linking a room to other rooms
 
rooms = {
 
 
 
 
            'Hall' : {
 
                  'south' : 'Kitchen',
 
                  'east'  : 'Dining Room',
 
                  'west'  : 'Bedroom'
 
                },
 
            'Kitchen' : {
 
                  'north' : 'Hall',
 
                  'item'  : 'key',
 
                },
 
            'Dining Room' : {
 
                  'west' : 'Hall',
 
                  'south': 'Garden',
 
                  'item' : 'photo',
                
                  'itemdesc' : 'A photo of William and his former housemaid, Annalise was taken on the night of October 21, 2010 on their very first night out together '
               },
 
            'Garden' : {
 
                  'north' : 'Dining Room',
 
                  'item'  : 'key'
 
               },
 
            'Bedroom' : {
 
                'east': 'Hall',
 
                'north': 'Closet',
 
                'item': 'diary',
 
                'requires': 'key'
 
                },
 
            'Closet':   {
 
                'south': 'Bedroom',
 
                'item' : 'cell phone'
 
                }  
 
        }
 
 
 
 
#start the player in the Hall
currentRoom = 'Hall'
#start husband in random room
husbandRoom = random.choice(list(rooms.keys()))
 
 
 
 
showInstructions()
 

 
 
 
#loop forever
 
while True:
  showStatus()
  moveHusband()


  if not player.escapeHusband():
    break
 
  #get the player's next 'move'
 
  #.split() breaks it up into an list array
 
  #eg typing 'go east' would give the list:
 
  #['go','east']
 
  move = ''
 
  while move == '':
 
    move = input('>')
 
 
 
 
  # split allows an items to have a space on them
 
  # get golden key is returned ["get", "golden key"]          
 
  move = move.lower().split(" ", 1)
 
 
 
 
  #if they type 'go' first
 
  if move[0] == 'go':
 
    if move[1] in rooms[currentRoom]:
      nextRoom = rooms[currentRoom][move[1]]
 
      #check if user has found key prior, if key is not found,
      #bedroom cannot be accessed prior
      if 'requires' in rooms.get(nextRoom, {}) and rooms[nextRoom]['requires'] not in evidence:
        print(f"The bedroom is locked! I wonder if there is a key somewhere to unlock it..")
      else:
      #set the current room to the new room
        currentRoom = nextRoom
 
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
 
 
 
 
  #if they type 'get' first
 
  if move[0] == 'get' :
 
    #if the room contains an item, and the item is the one they want to get
 
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
 
      #add the item to their evidence
 
      evidence += [move[1]]
 
      #display a helpful message
 
      print(move[1] + ' got!')
 
      #delete the item from the room
 
      del rooms[currentRoom]['item']
 
    #otherwise, if the item isn't there to get
 
    else:
 
      #tell them they can't get it
 
      print('Can\'t get ' + move[1] + '!')
 
  
 
      
 
  ## Define how a player can win
 
  if currentRoom == 'Garden' and 'key' in evidence and 'photo' in evidence and 'cell phone' in evidence and 'diary' in evidence:
 
    print('You escaped the house with all the evidence you need to provide to the authorities... YOUR HUSBAND IS IN JAIL, DIVORCE GRANTED!')
 
    break
 