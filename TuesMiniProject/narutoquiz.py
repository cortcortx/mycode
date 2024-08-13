#!/usr/bin/env python3
""" Naruto quiz """

points = 0
questions = 0
invalidresponse = "Invalid! Please only type "

print("\n\nQuiz: How well do you know Naruto?\n\n")

while questions < 3:

    if questions == 0:
        print("Q1:\n[T/F] Kakashi has another mask under his original one.")
        print(" [T] True\n [F] False\n")

        answer = input("> ").upper()
        if answer == 'T':
            print("Correct! I knew you had it in you!\n")
            points += 1
        elif answer == 'F':
            print("Wrong! Kakashi does not get caught lacking. He layers masks to avoid revealing his whole face.\n")
        else:
            print(invalidresponse + "T or F\n")
            continue

    elif questions == 1:
        print("Q2:\nWhat was the nickname of the Fourth Hokage?")
        print(" [A] Konoha's Orange Flash \n [B] Konoha's Yellow Flash \n [C] The Teleporting Hokage \n [D] The Lightning Hokage\n")
        answer = input("> ").upper()
        if answer == 'B':
            print("Correct! You're a Naruto genius!\n")
            points += 1
        elif answer == "A" or answer == "C" or answer == "D":
            print("Wrong! The Fourth Hokage was known across the world as Konoha's Yellow Flash.\n")
        else:
            print(invalidresponse + "A, B, C or D\n")
            continue

    elif questions == 2:
        print("Q3:\nWhat's the real name of the Nine-Tailed Beast?")
        print(" [A] Gyuki \n [B] Shikaku \n [C] Kurama \n [D] Uzumaki\n")
        answer = input("> ").upper()
        if answer == 'C':
            print("Correct! You sure know your tailed beasts!\n")
            points += 1
        elif answer == "A" or answer == "B" or answer == "D":
            print("Wrong! The Nine Tails within Naruto is named Kurama.\n")
        else:
            print(invalidresponse + "A, B, C or D\n")
            continue

    questions += 1

print("Total points awarded: " + str(points))

if points == 3:
    print("You should be so proud of yourself NERD! :)")
elif points == 2 or points == 1:
    print("Meh. You need to go back through all 1,000+ episodes.")
else:
    print("I can tell you've never watched a single episode.")
