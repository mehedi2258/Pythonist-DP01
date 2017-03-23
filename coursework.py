#Cgpa Count

'''
mark = int (input('Enter your mark: '))

if mark >= 80 and mark <=100:
    print('A +')

elif mark >=75 and mark <=79:
    print('A')

elif mark >=70 and mark <=74:
    print('A-')

elif mark >=65 and mark <=69:
    print('B+')

elif mark >=60 and mark <=64:
    print('B')

elif mark >=55 and mark <=59:
    print('B-')

elif mark >=50 and mark <=54:
    print('C+')

elif mark >=45 and mark <=49:
    print('C')

elif mark >=40 and mark <=44:
    print('D')

elif mark >=00 and mark <=39:
    print('You are Fail')

else:
    print('\nEnter number between 0 and 100')
'''


#Number Count

a = input('a =  ')
b = input('b =  ')
c = input('c =  ')

if a==b and a==c:
    print('a=b=c')
elif b>a and a>c:
    print('b>a>c')
elif a>c and c>b:
    print('a>c>b')
elif b>c and c>a:
    print('b>c>a')
elif a>b and b>c:
    print('a>b>c')
elif c>a and c>b:
    print('c>a>b')
else:
    print('c>b>a')
