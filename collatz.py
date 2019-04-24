def collazt(number):
    if number == 1:
        print('collazt function complete')
    elif number % 2 == 0:
        print(number // 2)
        return collazt(number // 2)
    else:
        print(3*number+1)
        return collazt(3*number+1)
            

#print('Enter number :')
#number = int(input())
#collazt(number)

try:
    collazt(int(input('Enter number : ')))
except ValueError:
    print('Non-Integer entered, program will exit')