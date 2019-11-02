import random

correct_answer = "e"
guess = input("write your name or enter e to exit ")

message_list = ["Keep trying ", "Yay ", "Try again! ", "You can do it ", "One more try "]

while guess != correct_answer:
    idx_message = random.randint(0, len(message_list) - 1)
    guess = input(message_list[idx_message])