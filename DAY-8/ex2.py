from ourpack import calc

fnum=float(input("Enter first number  :\t"))
snum=float(input("Enter second number :\t"))
while True:
    try:
        op=input("Enter operation (+,-,*,/)   :\t")
        if (op=='+'):
            print(f"Result: ",calc.add(fnum,snum))
        elif (op=='-'):
            print(f"Result: ",calc.sub(fnum,snum))
        elif (op=='*'):
            print(f"Result: ",calc.mul(fnum,snum))
        elif (op=='/'):
            print(f"Result: ",calc.div(fnum,snum))
        else:
            raise ValueError
    
    except ZeroDivisionError as ze:
        print('Division by 0 not allowed',ze)
    except ValueError as ve:
        print('Error in values',ve)
    except Exception as ex:
        print('Some other error',ex)
    choice=input("Do you want to continue (y/n): ")
    if (choice!='y'):
        print('Good Bye')
        break 

#-------------------------------------------------------------------------------------------------------

