#!/usr/bin/env python3
""" Naruto quiz:
    For each of the 5 questions, you are prompted to enter T or F for the True/False questions
    And A, B, C or D for the multiple choice questions.
    At the end, your total points for every correct answer is calculated."""

def narutoQuiz():
    points = 0
    questions = 0
    invalidresponse = "Invalid! Please only type "
    
    print(""" 
 _   _                  _                    
| \ | | __ _ _ __ _   _| |_ ___              
|  \| |/ _` | '__| | | | __/ _ \             
| |\  | (_| | |  | |_| | || (_) |            
|_| \_|\__,_|_|   \__,_|\__\___/  

""")
    print("Quiz: How well do you know Naruto?\n\n")
    
    while questions < 5:
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
                print("Wrong! The Nine-Tails Beast sealed within Naruto is called Kurama.\n")
            else:
                print(invalidresponse + "A, B, C or D\n")
                continue
    
        elif questions == 3:
            print("Q4:\nWhat technique does Naruto learn that finally allows him to pass his ninja graduation exams?")
            print(" [A] The Rasengan \n [B] The Multiple Shadow Clone Technique \n [C] The Clone Technique \n [D] Tailed Beast Powers\n")
            answer = input("> ").upper()
            if answer == 'B':
                print("Correct! You've seen episode one I see!\n")
                points += 1
            elif answer == "A" or answer == "C" or answer == "D":
                print("Wrong! After failing the graduation exam due to his inability to perform the Clone Technique, " +
                "Naruto steals a forbidden scroll and learns the Multiple Shadow Clone Technique. Seeing this, Iruka Umino allowed Naruto to pass.\n")
            else:
                print(invalidresponse + "A, B, C or D\n")
                continue
    
        elif questions == 4:
            print("Q5:\nWhat was Kushina's nickname?")
            print(" [A] The Red Hot-Blooded Habanero \n [B] The Red Hot-Headed Habanero \n [C] The Red-Haired Habanero \n" +
             " [D] The Red Hot-Tempered Habanero\n")
            answer = input("> ").upper()
            if answer == 'A':
                print("Correct! You are on fire!\n")
                points += 1
            elif answer == "B" or answer == "C" or answer == "D":
                print("Wrong! When Kushina first came to the village, she was ridiculed by other kids." +
                " After getting her revenge on them, she was given the nickname Red Hot-Blooded Habanero.\n")
            else:
                print(invalidresponse + "A, B, C or D\n")
                continue
    
        questions += 1
    
    print("Total points awarded: " + str(points))
    
    if points == 5:
        print("You should be so proud of yourself NERD! :)")
    elif points == 0:
        print("A disgrace! I can tell you've never watched a single episode.")
    else:
        print("Meh. You need to back through all 1,000+ episodes and try again.")

if __name__ == "__main__":
    narutoQuiz()