'''
#"GUESS GAMME"

print('\n"Gassing a number between 0 to 30. And you have only 5 chances."')
num=17

def f_name():
    if num==x:
        print('You have win.')
    elif x<0 or x>30:
        print('Wrong Input!')
    elif num<x:
        print("Wrong! try to guess lesser number." )
    elif num>x:
        print("Wrong! try to guess greater number.")


for i in range(1,6):
    x = int(input('\nEnter a number: '))
    print(i,':',' ',end='')
    f_name()
    if num==x:
        break
    print('You have',5-i,'time chances left.')
'''



'''
print('Can you guess my number?')
print('If you can, you have 5 chances to win and the range is 0 to 50.')
num = 35
result = True
for i in range(1,6):
    a = int(input('Enter your number: '))
    if a<num:
        print('Your number is lass than my number')
        print('You have',5-i,'chances left')
    elif a>num:
        print('Your number is greater than my number')
        print('You have',5-i,'chances left')
    else:
        print('You Win')
        result = False
        break
if result:
    print('You Failed')
'''


print('Can you guess my number?')
print('If you can, you have 5 chances to win and the range is 0 to 50.')
num = 35
def chances(num):
    print('You have',5-num,'chances left')
result = True

for i in range(1,6):
    user_input = int(input('Enter your number: '))
    if user_input < num:
        print('Your number is lass than my number')
        chances(i)
    elif user_input > num:
        print('Your number is greater than my number')
        chances(i)
    else:
        print('You Win')
        result = False
        break
if result:
    print('You Failed')
