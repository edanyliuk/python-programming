import random 

#this is princeton's solution

player_one_total = 0
player_two_total = 0

turn = 1

max_score = 20

#while True is just when you don't have any specific condition to test
while True:
    choice = input(f"Player {turn}: Roll or Hold [r/h] ")
    val = random.randint(1, 6)
    if choice == "r":
        print(f"Player {turn} rolls {val}")
        '''if turn == 1:
            print(f"Player 1 total is {player_one_total}")
        if turn == 2:
            print(f"Player 2 total is {player_two_total}")'''
            #need a way to show the running total which was my attempt above.
        if val != 1:
            if turn == 1:
                player_one_total += val
            else:
                player_two_total += val
            

        else:
            print(f"Player {turn} loses turn ")
            if turn == 1:
                player_one_total = 0
                turn = 2
            else:
                player_two_total = 0
                turn = 1
    else:
        print(f"Player {turn} holds ")
        if turn == 1:
            turn = 2
        else:
            turn = 1
    
    #check if someone wins the game

    if player_one_total >= max_score or player_two_total >= max_score:
        break

if player_one_total >= max_score:
    print("Player 1 wins!!!")
else:
    print("Player 2 wins!!!")