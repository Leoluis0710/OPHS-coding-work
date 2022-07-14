def menu():
     print('1 for Domination')
     print('2 for team deathmatch')
     print('3 for headquaters')
menu()
option = int(input('what game mode do you want to play'))
if option == 1:
    print('domination')
elif option == 2:
    print('team deathmatch')
elif option == 3:
    print('headquaters')
else:
    print()
