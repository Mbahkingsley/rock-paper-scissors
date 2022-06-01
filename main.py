import random

while True:
    
    choices=["R","P","S"]

    # computer's move
    cpu = random.choice(choices)

    player = None

    while player not in choices:

    # get player's move
        player = input("enter R, P or S for rock, paper or scissors respectively:\n").upper()

    # converting lowercase letter to uppercase letter
 
    
    if player == cpu:
        print("player ({}): CPU ({}) its a tie try again...".format(player,cpu))

    elif player == "R ":
        #print("player picks R")
        if cpu == "S":
            print("player ({}): CPU ({})".format(player,cpu))
            print("player wins")
    
        else:
            print("player ({}): CPU ({})".format(player,cpu))
            print("computer wins")

    elif player == "P":
        #print("player picks P")
        if cpu == "R":
            print("player ({}): CPU ({})".format(player,cpu))
            print("player wins")
    
        else:
            print("player ({}): CPU ({})".format(player,cpu))
            print("computer wins")

    elif player == "S":
        #print("player picks S")
        if cpu == "R":
            print("player ({}): CPU ({})".format(player,cpu))
            print("computer wins")

        else:
            print("player ({}): CPU ({})".format(player,cpu))
            print("player wins")

    elif cpu == "R":
        #print("computer picks R")
        if player == "S":
            print("player ({}): CPU ({})".format(player,cpu))
            print("computer wins")
    
        else:
            print("player ({}): CPU ({})".format(player,cpu))
            print("player wins")

    elif cpu ==  "P":
        #print("computer picks P")
        if player == "R":
            print("player ({}): CPU ({})".format(player,cpu))
            print("computer wins")
    
        else:
            print("player ({}): CPU ({})".format(player,cpu))
            print("player wins")

    elif cpu == "S":
        
        if player == "R":
            print("player ({}): CPU ({})".format(player,cpu))
            print("player wins")

        else:
            print("player ({}): CPU ({})".format(player,cpu))
            print("computer wins")
   
    if player != cpu:
        break

