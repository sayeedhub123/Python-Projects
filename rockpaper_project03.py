
import random

element_list = ["ROCK", "PAPER" ,  "SCISSOR"]


user_choice = input("\n\n\nEnter your choice (ROCK / PAPER / SCISSOR): ").upper()
computer_choice = random.choice(element_list)

print(f"\n\nUser move: {user_choice} \nComputer move: {computer_choice}\n\n")



if user_choice == computer_choice:
    print("Both has same move! Match tie....")


elif user_choice == "ROCK":
    if computer_choice == "PAPER":
        print("PAPER covered the ROCK : Computer WIN!!\U0001F4BB \U0001F389")
    else:
        print("ROCK smashed the SCISSOR : User WIN!!\U0001F9D4 \U0001F389 ")
elif user_choice == "PAPER":
    if computer_choice == "ROCK":
        print("PAPER covered the ROCK : User WIN!!\U0001F9D4 \U0001F389")
    else:
        print("SCISSOR cut the PAPER : Computer WIN!!\U0001F4BB \U0001F389")

elif user_choice == "SCISSOR":
    if computer_choice == "PAPER":
        print("SCISSOR cut the PAPER : User WIN!!\U0001F9D4 \U0001F389")
    else:
        print("ROCK smashed the SCISSOR : Computer WIN!!\U0001F4BB \U0001F389")
else:
    print("User move is not correct")


print("\n\n")


