import random
#slightly diff from yours. you don't keep re-stating that you need to have the guess pop up
correct_answer = "e"
guess = input("write your name or enter e to exit ")

message_list = ["Keep trying ", "Yay ", "Try again! ", "You can do it ", "One more try "]

while guess != correct_answer:
    idx_message = random.randint(0, len(message_list) - 1)
    print(message_list[idx_message])
    guess = input("write your name or enter e to exit ")