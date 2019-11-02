#while loop is executed only when a condition is met
import random #random number module. import should be at top of file


val = 1
while val < 10:
    print(val)
    val += 1 #increment val

#guessing game

#guess my number is called a prompt in this case...tells user what to do
#all keyboard input is string

#correct_answer = 7
correct_answer = random.randint(1, 10)
guess = int(input("guess my number (1 - 10) "))

while guess != correct_answer:
    guess = int(input("wrong. try again "))

print("You are correct!!")

#how do you break a loop?
names = ["jack", "jill", "mary", "kate"]

idx = 0
while idx < len(names):
    if "mary" == names [idx]:
        print("Found mary!!")
        break
    idx += 1

#how do we loop forever. if you enter anything other than "n" it will keep asking you for prompts
while True:
    answer = input("continue(y/n)" )
    if answer == "n":
        break