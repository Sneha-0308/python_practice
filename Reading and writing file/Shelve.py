import shelve
shelfFile = shelve.open('mydata.txt')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
