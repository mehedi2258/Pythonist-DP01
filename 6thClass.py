#if-else

'''
a = 10
b = 20
if a > b:
    print('a is getter than b')
else:
    print('a is less than b')
'''

'''
a = int(input('a = '))
b = int(input('a = '))
if a > b:
    print('a is getter than b')
else:
    print('a is less than b')
'''

'''
a = eval(input('a = '))
b = eval(input('b = '))
c = eval(input('c = '))

if a>b:
    if a>c:
        print('a is gretter than b,c')
    else:
        print('c is gretter than a,b')
elif b>a:
    if b>c:
        print(print('b is gretter than a,c'))
    else:
        print('c is gretter than a,b')
else:
    if c>a:
        print(print('c is gretter than a,b'))
    else:
        print('a is gretter than b,c')



if a==b and a==c:
    print('a = b =c')
elif a>=b and a>=c:
    print('a is gretter than b,c')
elif b>=a and b>=c:
    print('b is gretter than a,c')
elif c>=a and c>=b:
    print('c is gretter than a,b')



if b>a and a>c:
    print('b>a>c')
elif a>c and c>b:
    print('a>c>b')
#elif c>a and c>b:
 #   print('c is gretter than a,b')
else:
    print('a=b=c')
'''



#Loop - For loop,  While loop

'''
for i in range(10):
    print(i)
'''
'''
i = 0
while i<=10:
    print(i)
    i = i+1
'''

'''
l = range(10)
print(l)
print(type(l))'''

'''
for i in [2,4,5,100]:
    print(i)'''

'''
for i in range(20,10,-1):
    print(i)

for i in range(20,10,-2):
    print(i)

for i in ['a','b','c','d']:
    print(i)

for i in ['a','b','c','d']:
    print(ord(i))

print(bin(15))

a = 0b1111
print(a)

b = 0xa
print(b)

print(oct(10))

print(hex(15))
'''


#for i in range(100):
 #   print(ord(str(i)))

'''
username = input('Username: ')
password = input('Password: ')
if len(password) >=6:
    print('Password is Strong')
else:
    print('Your password is not secured')



name = 'mehedi'
password = '123mehedi123'
name = input('Username: ')
password = input('Password: ')
if name == 'mehedi' and password == '123mehedi123':
    print('Log in')
else:
    print('Username or password incorrect')
'''

'''
name = ['mehedi','nayon','jibon']
print('mehedi' in name)
'''

username = ['mehedi','jibon','nayon']
password = ['123mehedi123','jibon123','123nayon']
n = input('Username: ')
p = input('Password: ')
if n in username and p in password:
    print('Log in')
else:
    print('Username or password incorrect')

i = username.index(n)
password[i]==p
