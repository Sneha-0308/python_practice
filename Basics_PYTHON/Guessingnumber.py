import random
secretnum = random.randint(1,20)
print(secretnum)
print('Im guessing the number between 1 to 20')
for i in range(1, 7):
    num = int(input('Enter your guess:'))
    if(num < secretnum):
        print('your guess is to low')
    elif(num > secretnum):
        print('Your guess is to high')
    else:
        break

if num == secretnum:
    print('your guess is correct ')
else:
    print('guess is wrong')