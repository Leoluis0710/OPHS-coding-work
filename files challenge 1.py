print('/noopening the file')
file = open('numbers.txt','w')
numb=input('write a number >>>')
file.write(numb)
file.close()
