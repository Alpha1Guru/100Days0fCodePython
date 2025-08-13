print("Hello Welcome to treasure Island")
#The First Trial
print("""You come to a crossroad in the Valley Of Decisions.
      1. On the left is the path of Ice Cream of Frivolities.
      2. On the right is the path of Rotten Toads of Importance. """)
while True:
    choice = input("Which do you chose 1 or 2? ")
    if choice not in ("1", "2"):
        print("\nNot a path choose 1 or 2")
    else:
        break
if choice == "1":
    print("You have taken the easy path\nYou consumed a lot of ice cream but was never satisfied\nGAME OVER!!")
    exit()

#The Second Trial
print("You have taken a hard part. You journey will not be easy!.")
print("As you walk through the path of the Rotten Toads of Importance\n"
"Your energy is draining. Your brain screams'Give Up!' and your body is crys 'Rest!'\n"
"\t1. You quit\n" 
"\t2. You move on\n")

while True:
    choice = input("Which do you chose 1 or 2? ")
    if choice not in ("1", "2"):
        print("\nNot a path choose 1 or 2")
    else:
        break
if choice == "1":
    print("You have taken the easy path\nTo give up is not an option!\nGAME OVER!!")
    exit()

#The Third Trial
print("You have taken a hard part. You journey will not be easy!.")
print("As you walk through the path of the Rotten Toads of Importance\n"
"You encounter 4 gates and a glowing bowl filled with three disgusting toads!:\n"
"\t1. The Gate of the Ugliest Toad. (You most eat the ugliest and biggest toad to open the gate)\n" 
"\t2. The Gate of the Second Ugliest Toad (You most eat the second ugliest and biggest toad to open the gate)\n" 
"\t3. The Gate of the Third Ugliest Toad (You most eat the third ugliest and biggest toad to open the gate)\n" 
"\t4. The Gate of Sweet Foods\n (You don't need to eat anything)")
while True:
    choice = input("Which do you choose 1, 2, 3 or 4? ")
    if choice not in ("1", "2", "3", "4"):
        print("\nNot a path choose 1 or 2")
    else:
        break

reward = round(100000 * 0.8 *0.8)
if choice == "1":
    print("Congatualations on reaching the treasure you got {} worth of gold!".format(reward))
elif choice == "2":
    reward = round(reward*0.8*0.5)
    print("Congratualtions on reaching the treasure you got {} worth of gold!".format(reward))
elif choice == "3":
    reward = round(reward * ((0.8*0.5)*2))
    print("Congratualtions on reaching the treasure you got {} worth of gold!".format(reward))
else:
    print("Wow you came all this way just to fail?\nYou Lost\tGAME 0VER!!")


