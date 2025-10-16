import random
# print('Random number from 1 to 1000:')
# print(random.randint(1,1000))

import random
def findwinner():
    name=input('\nEnter Your Name:\t')
    luckyNumber=random.randint(1,10)
    print('Welcome Mr./Ms',name)
    if (luckyNumber==1):
        print('CONGRATS,You have won an Iphone 17 Pro Max 😀🎉✨')
    elif(luckyNumber==4):
        print('CONGRATS, You have won a PS5 😀🎉✨')
    elif(luckyNumber==8):
        print('CONGRATS,You have won Proton X50 😀🎉✨')
    else:
        print('UHOHHHH, Better luck next time .·°՞(˃ ᗝ ˂)՞°·.')
print()
 