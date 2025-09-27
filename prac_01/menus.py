MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter your name: ")
print(MENU)
menu_choice = input("Please enter your menu choice: ")
while menu_choice != "Q":
    if menu_choice == "H":
        print("hello",name)
        print(MENU)
        menu_choice = input("Please enter your menu choice: ")
    elif menu_choice == "G":
        print("goodbye",name)
        print(MENU)
        menu_choice = input("Please enter your menu choice: ")
    else:
        print("Invalid")
        print(MENU)
        menu_choice = input("Please enter your menu choice: ")