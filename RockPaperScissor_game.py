import random
options = ("rock","paper","scissor")

playing = True 

while playing:

    player = None
    computer = random.choice(options) 

    while player not in options: 
        player = input("Enter a choice (rock,paper,scissor):")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("YOU WIN !")
    elif player == "paper" and computer == "rock":
        print("YOU WIN !")
    elif player == "scissor" and computer == "paper":
        print("YOU WIN !")
    else:
        print("YOU LOSE!")
    
    if not input("PLAY AGAIN ? (y/n):").lower() == "y":
   
        playing = False
print("Thanks for playing !")
