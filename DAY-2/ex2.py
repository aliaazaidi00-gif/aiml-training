#OPERATORS IN PYTHON
# ourNum=1
# print('Printing Numbers from 1 to 100')
# while(ourNum<=100):
#     print(ourNum,end=" ")
#     ourNum+=1                 #kalau takda ni dia never ending

#break example
# Num=1
# print('Printing Numbers from 1 to 100 before we get the number divisible by 11')
# while(Num<=100):
#     if(Num%11==0):
#         break                    #all numbers listed except thoe that starts to be divisible by the number stated 
#     print(Num,end=" ")
#     Num+=1   

#CONTINUE EXAMPLE
# Num=1
# print('Printing Numbers from 1 to 100 those are not divisable by 11')
# while(Num<=100):
#     if(Num%11==0):
#         continue
#     print(Num,end=" ")
#     Num+=1   

# num=1
# while(num<=100):
#     if(num%11==0):
#         num+=1
#         continue
#     print(num,end="\t")
#     num+=1

#num+=1
# print("odd numbers from 1 to 100")                  #tak divisable dia tak listed 
# num=1
# while(num<=100):
    
#     if(num%5==0):
#         num+=1
#         continue
#     print(num,end="\t")
    
#     num+=1

# for i in range(1,100):                       #while loop-condition arrives unexpectedly, ex:indefinite
#     if (i%5==0):                             #full loop-we know further circumstances, ex:table of sifir
#         continue
# print(i,end="\t")

# correctPwd='alia@123'

# while True:
#     pwd=input('enter password to start the game:\t')
#     if(correctPwd==pwd):
#         print('Permission Granted!!!')
#         print ('***Game Started!!!***')
#         break
#     else:
#         print('wrong password,try again sis')

#COUNTER
# correctPwd='alia@123'
# counter=0
# while True:
#     pwd=input('enter password to start the game:\t')
#     if(correctPwd==pwd):
#         print('Permission Granted!!!')
#         print ('***Game Started!!!***')
#         break
#     else:
#         print('wrong password,try again sis')
#         counter+=1
#         if(counter>=3):
#             print('blocked for further attempt')
#             break 
