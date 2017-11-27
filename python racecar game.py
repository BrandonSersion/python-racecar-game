import random
option = ["LEFT","RIGHT","STRAIGHT"]
place = 6
suffix=[None,"st","nd","rd","th","th","th"]
print("      =\ Speed Racer /=/=/  /=        ")
while place > 1:
    wrong = random.choice(option)
    prompt = input("Do you swerve LEFT, RIGHT, or continue STRAIGHT?  ")
    prompt = prompt.upper()
    if prompt == wrong:
        print("")
        print("\n You crash while in " + str(place) +  suffix[place] + " place! Game Over.")
        break
    elif prompt not in option and prompt != "WIN":
        print("\n You press the wrong button and explode while in " + str(place) + suffix[place] + " place! Game Over.")
        break
    else:
        place -= 1
        print("You pass your next opponent! Place:", place)
    print()
if place == 1:
    print("\n WINNER! You are #1")
else:
    print("             Try again?")
        
        