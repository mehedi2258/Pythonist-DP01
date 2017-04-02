'''For printing
1
2 3
4 5 1
2 3 4 5
1 2 3 4 5 '''
'''
number = 1
a= int(input('Enter line number: '))
for i in range(1,a+1):
    for j in range(i):
        print(number,end=" ")
        number = number + 1
        if number==6:
            number=1
    print()
'''


'''
number = int(input('Enter number: '))
a= int(input('Enter line number: '))
for i in range(1,a+1):
    for j in range(i):
        print(number,end=" ")
        number = number + 1
        if number==6:
            number=1
    print()
'''

'''
number = int(input('Enter number: '))
first_num= number
end_num = int(input('Enter last number: '))
a= int(input('Enter line number: '))
for i in range(1,a+1):
    for j in range(i):
        print(number,end=" ")
        if number==end_num:
            number=first_num
        else:
            number= number+1
    print()
'''



#Function, Function, Function
'''
syntex
dif function_name():
    --------
    --------
    --------'''


'''
def function_name():
    print("Mehedi")
    print("Hasan")

function_name()'''

'''
d = 5
def function_name(num):
    print("Mehedi")
    print("Hasan")
    print(num)

function_name('Mehedi')
function_name(923)
function_name(True)
function_name(14.5)'''


'''
def add(num1, num2):
    print(num1+num2)
add(23,32)'''


'''
def add(num1, num2):
    print(num1+num2)
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
add(a,b)'''

'''
def sum(a,b):
    return (a+b)
x = sum(10,20)
print(x)'''

'''
def add(num1, num2):
    return(num1+num2)
def mul(num3, num4):
    return(num3-num4)
def sub(num5, num6):
    return(num5*num6)
def div(num7, num8):
    return(num7/num8)
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))

x= add(a,b)
y = mul(a,b)
z = sub(a,b)
zz = div(a,b)
    print(a,'+',b,'=',x)
    print(a,'-',b,'=',y)
    print(a,'*',b,'=',z)
    print(a,'/',b,'=',zz)
'''


'''
def add(num1, num2):
    return(num1+num2)
def mul(num3, num4):
    return(num3-num4)
def sub(num5, num6):
    return(num5*num6)
def div(num7, num8):
    return(num7/num8)
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
print()
print('Enter 1 for Addition, Enter 2 for Multiplication, Enter 3 for Substitution, Enter 4 for division')
print()
r = int(input('Choose what do you want to do: '))

x= add(a,b)
y = mul(a,b)
z = sub(a,b)
zz = div(a,b)
if r==1:
    print(a,'+',b,'=',x)
elif r==2:
    print(a,'-',b,'=',y)
elif r==3:
    print(a,'*',b,'=',z)
elif  r==4:
    print(a,'/',b,'=',zz)
'''


'''
def sum(a,b):
   return a*b

a = sum(12,12)
print(a)
print(sum(a,12))'''



a =0
try:
    a = int(input('Enter a number: '))
except ValueError:
    print('invalid')
except Exception:
    print('Somethimg going wrong')
print(a)
