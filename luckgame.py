print('''
   ,--------------------------------------------------------------.
  |============================,--""--.============================|
  |==========================,'   ::   `.==========================|
  |=========================/     ::     \=========================|
  |========================:      ::      :========================|
  |=======================:       ::       :=======================|
  |=======================|      .::.      |=======================|
  |=======================:    .:'  `:.    :=======================|
  |========================: .:'      `:. :========================|
  |=========================\            /=========================|
  |==========================`.        ,'==========================|
  |============================`--..--'========================dd==|
   `--------------------------------------------------------------'

''')


print("Guess you luck")
print("See if you are lucky enough to win lottery")
choice1 = input('You\'re at the first gate.Make a choice to move furhter.Type "Room1" or "Room2" . ')

if choice1 == "room1":
    print("Congratulations for next level")
    choice2=input('You\'re welcome to Room1. Now you pick one of the key to move further. Type "Key1" or "Key2". ')

    if choice2 == "key2":
        print("You are near to win.Select one of the letter among three. ")
        choice3 = input("Select one letter among A,S,W . " )

        if choice3 =="a":
            print("Wrong letter")
        elif choice3 == "s":
            print("You were very close to win but lost the game")
        elif choice3 == "w":
            print("Wohooo!!!!!!! YOU WIN MERCEDEES")
        else:
            print("sorry but you had to select one letter.")
    else:
        print("Sorry,you chose wrong key")
else:
    print("Sorry you\'re out of the game")