#!/usr/bin/python3
 
# in use for husband to randomly be placed in different rooms each turn
import random
 
 
 
def showInstructions():
 
  #print a main menu and the commands
 
  print('''
Hidden Truths: The Escape
Backstory:
You are Sarah, trapped in a marriage that hides dark secrets. Your husband, Mark, once seemed perfect, 
but you've uncovered a disturbing diary entry revealing his sinister plans against you. Now, you must gather evidence 
hidden around the house to prove his true nature and escape before he catches you.
Mark is growing suspicious, and his movements around the house are unpredictable. Every room holds a clue, 
but time is running out. Can you collect the evidence and escape, or will you become another victim of his twisted scheme

========

Commands:

  go [direction]  - Move between rooms
  get [item]      - Pick up items

Navigate: Use go [direction] to move between rooms.
Collect Evidence: Use get [item] to pick up items that can be used as evidence.
Escape Encounters: Avoid or escape from your husband if you encounter him.
Unlock Rooms: Find keys to access locked areas.
Win: Gather all the evidence and escape to the garden to win.
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
 
 
 
 

# the monster/husband can randomly appear in any room of the home
def moveHusband():
 
    global husbandRoom
 
    possible_rooms = list(rooms.keys())
 
    #possible_rooms.remove(currentRoom)
 
    husbandRoom = random.choice(possible_rooms)

    print(f"Husband moved to: {husbandRoom}")
 

class Wife():
  #wife has 3 chances to be able to escape her husband if caught before completing the game
  def __init__(self):
    self.escape = 2

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
 
#add functionality to evidence,  diary entires, text messages, etc
 
evidence = []
 
 
 
#A dictionary linking a room to other rooms
 
rooms = {
 
 
 
 
            'Hall' : {
 
                  'south' : 'Kitchen',
 
                  'east'  : 'Dining Room',
 
                  'west'  : 'Bedroom'
 
                },
 
            'Kitchen' : {
 
                  'north' : 'Hall',
 
                  'item'  : 'key',

                  'itemdesc': "A slightly worn key that fits the bedroom door. It'\s the only way to access the room where Mark has hidden some of his darkest secrets."
 
                },
 
            'Dining Room' : {
 
                  'west' : 'Hall',
 
                  'south': 'Garden',
 
                  'item' : 'photo',
                
                  'itemdesc' : 'A faded photograph showing Mark with a woman you don’t recognize. The smiles are unsettling, and the date on the back is recent.'
               },
 
            'Garden' : {
 
                  'north' : 'Dining Room',
               },
 
            'Bedroom' : {
 
                'east': 'Hall',
 
                'north': 'Closet',
 
                'item': 'diary',

                'itemdesc': "An old leather-bound diary with entries that reveal a different side of Mark - a side he/'s kept hidden. The last few pages are particularl chilling.",
 
                'requires': 'key'
 
                },
 
            'Closet':   {
 
                'south': 'Bedroom',
 
                'item' : 'cell phone',

                'itemdesc': "An unmarked cell phone with a series of incriminating text messages and voicemails. The battery is low, but it could be the key to your escape."
 
                }  
 
        }
 
 
 
 
#start the player in the Hall
currentRoom = 'Hall'
#start husband in random room
husbandRoom = random.choice(list(rooms.keys()))
player = Wife()
 
 
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
      if 'itemdesc' in rooms[currentRoom]:
        print(f"Description: {rooms[currentRoom]['itemdesc']}")
      print(move[1] + ' has been placed in your evidence bag!')


 
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
 
