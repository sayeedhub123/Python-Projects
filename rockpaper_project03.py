
import random

element_list = ["ROCK", "PAPER" ,  "SCISSOR"]


def main():
    while True:
        
        user_choice = input("Enter your choice (ROCK / PAPER / SCISSOR): ").upper()
        computer_choice = random.choice(element_list)

        print(f"\nUser move: {user_choice} \nComputer move: {computer_choice}\n")
        
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
            break


print("\n")
    




if __name__ == "__main__":
    main()
