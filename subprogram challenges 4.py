def menu():
     print('1 creative')
     print('2 Survival')
     print('3 Hardcore')
     print('4 Adventure')
     print('5 exit')
     option = int(input('what game mode do you want to play'))
menu()
option = int(input('what game mode do you want to play'))
if option == 1:
    print('creative selected')
elif option == 2:
    print('survival selected')
elif option == 3:
    print('hardcore selected')
elif option == 4:
    print('adventure selected')
elif option == 5:
    print('exiting...')
else :
    print('invalid')
    menu()
    
