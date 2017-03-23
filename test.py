import math

'''list = [10,20,30,True]
list.append(20)
print(list)'''


'''list = [10,20,30,True]
list.remove(20)
print(list)'''


'''a=9
b=6
c=a+b
print(a,'+',b,'=',c)
print(a,'+',b,'=',(a+b))
print('%d + %d = %d' %(a,b,c))
print('{} + {} = {}'.format(a,b,c))'''


'''a = int(input())
b = int(input())
print(a + b)'''


'''print('Enter First Number: ')
a = eval(input())
print('Enter Second Number:')
b = eval(input())
print('Ans is: ')
print(a + b)'''


'''print('Enter First Number: ',end='')
a = eval(input())
print('Enter Second Number:')
b = eval(input())
print('Ans is: ')
print(a + b)'''


'''print('Enter First Number: ',end='')
a = eval(input())
print('Enter Second Number: ',end='')
b = eval(input())
print('Ans is: ',end='')
print(a + b)'''


'''print('Enter First Number: ',end='a = ')
a = eval(input())
print('Enter Second Number: ',end='b = ')
b = eval(input())
print('Ans is: ',end='c = ')
print(a + b)'''


'''a = int(input('Enter First Number: '))
b = eval(input('Enter First Number: '))
c = eval(input())
print(a,'+',b,'=',c)'''


'''a = int(input('Enter First Number: '))
b = eval(input('Enter First Number: '))
c = input()
d = eval(c)
print('{}={}'.format(c, d))'''


'''a = int(input('Enter First Number: '))
b = eval(input('Enter First Number: '))
c = input() #a+b
d, e, f = c.split(' ')
c = eval(c)
print('{} {} {} = {}'.format(a, e, b, c))'''



'''mark = eval(input('Enter Your Mark: '))
if mark<0 or mark>100:
    print('Envalid Mark')

elif mark < 60:
    print('Fail')

else:
    print('Pass')'''


'''fac = 1
for i in range(5):
    fac = (i+1) * fac
print('5! = '+str(fac))'''


'''number = eval(input('Enter the number: '))
fac = 1
for i in range(number):
    fac = (i+1) * fac
print(number, '! = '+str(fac), sep='')'''


'''number = eval(input('Enter the number: '))
fac = 1
for i in range(number):
    fac = (i+1) * fac
print(str(number)+ '! = '+str(fac))'''


'''def factorial_generator():
    number = eval(input('Enter the intiger number: '))
    fac = 1
    for i in range(number):
        fac = (i+1) * fac
    print(str(number)+ '! = '+str(fac))
factorial_generator()'''




'''number = int(input('Enter the number: '))

def factorial_generator(num):
    fac = 1
    for i in range(num):
        fac = (i+1) * fac
    return fac

print (str(number)+'!=',factorial_generator(number))'''



'''def factorial_generator(num):
    fac = 1
    for i in range(num):
        fac = (i+1) * fac
    return fac

number = int(input('Enter the number: '))
print (str(number)+'!=',factorial_generator(number))'''



'''def sum(num1, num2):
    print (num1 + num2)
sum(7,8)'''




'''for line in range(1,5):
    for star in range (line):
        print('*',end='')
    print()'''



'''lines = eval(input('Enter how many lines you want to Print: '))
for line in range(lines):
    for star in range (line):
        print('*',end='')
    print()'''



'''def sum(num1, num2):
    return num1 + num2
    a = sum(7,8)
print(a)'''



'''for i in range(1,6):
    for star in range (i):
        print('*',end='')
    print()'''


'''for i in range (1,6):
    for star in range (6-i):
        print('*',end='')
    print()'''



'''for i in range (5):
    for j in range (5-i):
        print('*',end='')
    print()
    for k in range (i+1):
        print(' ',end='')'''



'''for i in range (1,6):
    for j in range (i):
        print(i,end='')
    print()'''



'''for i in range (5):
    for j in range (4-i):
        print(' ',end='')
    for k in range (i+1):
        print('*',end='')
    print()'''


#While Loop
'''a=1
while a<=10:
    print(a)
    a=a+1'''


'''a=2
while a<=10:
    print(a)
    a=a+2'''


'''a=1
while a<=10:
    print(a)
    a=a+2'''



'''a=1
while a<=20:
    print(a)
    a=a+1
    if a==7:
        a=a+6'''



'''a=1
while a<=20:
    if a>7 and a<13:
        a=a+1
        continue
    print(a)
    a=a+1'''

'''a=10
while a<=50:
    print(a)
    if a==30:
        break
    a=a+1'''



