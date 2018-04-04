import random

def master_mind ():
    # initalize game
    hidden_number = random.randint(1000,9999)
    won = False
    print ( " ┌───────────────────────────────────┐")
    print ( " │ Guess a number from 1000 to 9999! │")
    print (f" ├───────────────────────────────────┘")

    # Begin game with 10 rounds
    for x in range (0,10):
        guess = input (f" ├ Guess! ─── Round {x + 1}/10\n │ ")
        part_match = 0
        full_match = 0
        hidden_array = []
        guess_array  = []

        # validate user input
        try:
            int (guess)
        except ValueError:
            print (f" ├ Guess was invalid.")
            
        # Append number and guess to an array to access easier
        for i in range (len(str(hidden_number))):
            hidden_array.append (str(hidden_number)[i])
            guess_array.append (str(guess)[i])

        # comparing items in arrays to find matches
        for i in range (len(hidden_array)):
            for n in range (len(hidden_array)):
                if (str(hidden_number)[i] == str(guess)[i]):
                    full_match = full_match + 1
                    break
                elif (str(hidden_number)[i] == str(guess)[n]):
                    part_match = part_match + 1
                    break

        print (f" ├ Matched {full_match} fully and {part_match} partially.")
        # check if all digits match
        if (full_match == 4):
            won = True
            break
        # reset win condition as round restarts
        else:
            full_match = 0
    
    # Win loss messages
    if (won):
        print (" │ ╔══════════╗")
        print (" └─╢ You win. ║")
        print ("   ╚══════════╝")
    else:
        print (f" │ ┌──────────────────────────────────────┐")
        print (f" └─┤ You have lost... The number was {hidden_number} │")
        print (f"   └──────────────────────────────────────┘")


# run program
master_mind()