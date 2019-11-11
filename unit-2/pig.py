import random

val = random.randint(1, 6)

#need two player variables to store the scores
#each roll of a die is a score and it is used to update the total

player1_total = 0
player2_total = 0

#You need a way to tell whose turn it is
#h or r
#1 means you lose your turn and your score goes back to 0

score = val
bad_score = 1

#if you have a 1 or a h the turn passes over
#if turn is one then we increment player 1's total and if the turn is 2 then we increment player 2's total
print(score)

#this allows a person to roll and tally their score. it will stop their turn if they reach a score of 20 or if they roll a 1.
while val != bad_score:
    player1_total += val
    #print(player1_total)
    score = input("Roll or Hold (R to Roll and H to Hold) ")
    val = random.randint(1, 6)
    if val == bad_score:
        print("Game over")
        print(f"Roll was 1")
    elif score == "R":
        print(player1_total + val)
        print(f"Roll is {val}")
        if (player1_total + val) >= 20:
            print("YOU WIN!!!")
            break
    elif score == "H":
        print(player1_total)
        
        
    



    
   


