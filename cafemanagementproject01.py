#Menu of the restaurent
menu = {
    'PIZZA': 590,
    'PASTA': 290,
    'BURGER': 320,
    'COFFEE': 120,
    'MEAT BOX': 299,

}


#greetings
print("\n{{{{{WELCOME TO OUR RESTAURANT SIDDU}}}}}")
print("\nHere is our menu. Please check it out!")
print("Pizza: 590BDT \nPasta: 290BDT\nBurger: 320BDT \nCoffee: 120BDT \nMeat Box: 299BDT") 


total_payment = 0

first_order = input("Enter what you need: ").upper()

if first_order in menu:
    total_payment += menu[first_order]
    print(f"Your item {first_order} has been added")
    
else: 
    print("Your entered item is not available yet")


#asking for another order
wish_order = input("Do you need anything else sir? (Yes/No)")

if wish_order == "Yes" .lower():
    second_order = input("Enter your another item: ") .upper()
    if second_order in menu:
        total_payment += menu[second_order] 
        print(f"Your second item {second_order} has been added")
       
    else:   
        print("Your entered item is not available yet")


if first_order and second_order not in menu:
    print("Sorry sir, we can not serve you")

else:

    print(f'Sir, for those items you have to pay {total_payment}')


    print("THANK YOU SIR, Have a great day!!!")