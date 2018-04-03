import random

def master_mind ():
    hidden_number = random.randint(1000,9999)
    won = False
    print ( " ┌───────────────────────────────────┐")
    print ( " │ Guess a number from 1000 to 9999! │")
    print (f" ├───────────────────────────────────┘")
    for x in range (0,10):
        guess = input (f" ├ Guess! --- Round {x + 1}/10\n │ ")
        part_match = 0
        full_match = 0
        hidden_array = []
        guess_array  = []

        for i in range (len(str(hidden_number))):
            hidden_array.append (str(hidden_number)[i])
            guess_array.append (str(guess)[i])

        for i in range (len(hidden_array)):
            for n in range (len(hidden_array)):
                if (str(hidden_number)[i] == str(guess)[i]):
                    full_match = full_match + 1
                    break
                elif (str(hidden_number)[i] == str(guess)[n]):
                    part_match = part_match + 1

        print (f" ├ Matched {full_match} fully and {part_match} partially.")
        if (full_match == 4):
            won = True
            break
        else:
            full_match = 0
            
    if (won):
        print (" └ You win.")
    else:
        print (" └ You have lost...")

master_mind()