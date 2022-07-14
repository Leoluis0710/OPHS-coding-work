def menu():
     print('1 for 1-player')
     print('2 for 2-player')
     print('3 online')
     print('4 exit')
menu()
option = int(input('what game mode do you want to play'))
if option == 1:
    print('1-player selected')
elif option == 2:
    print('2-player selected')
elif option == 3:
    print('online selected')
elif option == 4:
    print('exiting...')
else:
    print()
