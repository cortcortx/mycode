#!/usr/bin/python3

#in use for husband to randomly be placed in different rooms each turn
import random

def showInstructions():
    #print a main menu and the commands

    print('''
    RPG Mystery Game

    =================

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

        #print an item if there if one

        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])
        
        print('----------------------------')





        #the husband can randomly appear in any room of the home
        def moveHusband():
            global husbandRoom
            
            possible_rooms = list(rooms.keys())

            possible_rooms.remove(currentRoom)

            husbandRoom = random.choice(possible_rooms)


        
        #evidence holds all items collected from each room
        evidence = []


        #a dictionary linking a room to other rooms
        rooms = {


                    'Hall' : {

                        'south' : 'Kitchen',
                        'east'  : 'Dining Room',
                        'west'  : 'Bedroom'

                    },

                    'Kitchen' : {

                        'north' : 'Hall',
                        'item'  : 'husband',

                    },

                    'Dining Room' : {

                        'west'  : 'Hall',
                        'south' : 'Garden',
                        'item'  : 'photo'  

                    },

                    'Garden' : {

                        'north' : 'Dining Room',
                        'item'  : 'key'

                    },

                    'Bedroom' : {

                        'east'     : 'Hall',
                        'north'    : 'Closet',
                        'item'     : 'diary',
                        'requires' : 'key'

                    },

                    
                    'Closet' : {

                        'south' : 'Bedroom',
                        'item'  : 'cell phone'

                    }
        }

    #start the user in the Hall
    currentRoom = 'Hall'
    #start husband in random room
    husbandRoom = random.choice(list(rooms.keys()))






    showInstructions()


    #loop forever
    while True:
        showStatus()
        moveHusband()


        #get the user's next 'move'

        #.split() breaks it up into a list array

        #eg typing 'go east' would give the list:

        #['go', 'east']

        move = ''

        while move == '':

            move = input('> ')



            #split allows an item to have a space on them

            #get golden key is returned ["get", "golden key"]

            move = move.lower().split(" ", 1)



            #if they type 'go' first

            if move[0] == 'go' :

                if move[1] in rooms[currentRoom]:
                    nextRoom = rooms[currentRoom][move[1]]

                    #checks if user has found and placed key in evidence[] prior to accessing Bedroom,
                    #if key has not been found yet, Bedroom cannot be accessed

                    if 'requires' in rooms.get(nextRoom, {}) and rooms[nextRoom]['requires'] not in evidence:
                        print(f"The bedroom is locked! I wonder if there is a key somewhere to unlock it..")

                    else:
                        currentRoom = nextRoom

                else:
                    print('You can\'t go that way!')

            
            #if they type 'get' first

            if move[0] == 'get' :

                #if the room contains an item, and the item is he one they want to get
                if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:

                    #add the item to evidence
                    evidence += [move[1]]

                    #display a helpful message
                    print([move[1] + ' has been placed into your evidence bag'])

                    #delete the item from the room
                    del rooms[currentRoom]['item']

                #otherwise
                else:
                    #tell tehm they can't get it
                    print('Can\'t get ' + move[1] + '!')


            #Define how a player can win

            if currentRoom == 'Garden' and 'key' in evidence and 'photo' in evidence and 'cell phone' in evidence and 'diary' in evidence:
                print('You have escaped the house with all of the evidence you will need to provide to the authorities...\n' +
                'YOUR DIVORCE IS GRANTED and YOUR [EX]-HUSBAND IS NOW IN JAIL.\nJustice has been served.')

                break #ends game


            #if a player enters a room with husband

            if currentRoom == husbandRoom :
                print('Your husband has got you... GAME OVER!')

                break#ends game


