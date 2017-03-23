'''
a = "python class 4."
b = "pycharm & pythonist BP01."
print(a[-2])
print(b[10:25]+a[6:15])
print(b[10:]+a[6:])
print(b[10:],a[7:])
'''


'''a = 4
b = 'pycharm & pythonist BP01 team'
c = 62.2
print(b[0:7],str(c))
print(b[10:24],'Class',str(a), b[25:])

print(b[:7],c)
print(b[10:24],'Class',a, b[25:])

print (len(b))
'''

'''
b = 'pycharm & pythonist BP01 team'
print (b.find('pycharm'))
print (b.find('BP01'))
'''


#List

'''
a = list ()
b = []
c = [1,2,3,4]
print (type(a))
print (type(b))
print (type(c))

true = 'This is true'
d = [1,2,3,4,['a','b','c','d'], True, true]
print (d[4])
print (d[-1])
print (d[-2])
print (d[4][-1])
print (d[4][3])


list = [12, 'python', 16.2, 4, True]
print (type(list))
print (list)
print (list[0])
print (list[0:2])
list.append(6)
print (list)
'''

'''
a = []
b = list()
true = 'This is true'
c= [1,2,3,4,['a','b','c','d'], True, true]
c[1]= 'Mehedi'
print(c)
print (c[1])
print (c[2])

c= [1,2,3,4,['a','b','c','d'], True, true]
c[1]= ['Mehedi',12,13]
print(c)
print (c[1][2])
print (c[3]+c[1][1])

c= [1,2,3,4,['a','b','c','d'], True, true]
c[1]= ['Mehedi','12',13]
print (c[3],c[1][1])
print(str(c[3])+c[1][1])
print(str(c[3])+" "+c[1][1])
'''


#Append & Extend
'''
b = list()
print(b)
b.append(12)
print(b)
b.append([12,13,14,'name'])
print(b)

b = list()
print (b)
b.append(12)
print(b)
b.extend([12,13,14,'name'])
print(b)
'''


'''
a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
a.extend(c)
print(a)

a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
a = c[:]
print(a)

a = []
true = 'This is true'
a.extend([1,2,3,4,['a','b','c','d'],True,true])
print(a)
'''

'''
a = []
x =12
y = 'python 3'
a.extend([x,y])
print(a)

a= []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
x= 12
y=13
a.extend([c,x,y])
print(a)
'''


#Count


'''
a= []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
print (c.count(2))
print (c.count(4))
print (c.count('a'))
print (c[4].count('a'))
'''

'''
a = []
b = input()
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
#print (c.count(b))
print (c[4].count('a'))
'''

'''
a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
a = c.copy()
print(a)
'''

a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
c.clear()
print(c)


a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
c.remove(2)
print(c)


a = []
true = 'This is true'
c = ['a','z','A','Bqsd']
c.reverse()
print(c)



a = []
true = 'This is true'
c = ['a','z','A','Bqsd']
n = c.index('Bqsd')
print(n)



a = []
true = 'This is true'
c = ['a','z','A','Bqsd']
n = c.index('z')
c[n]='mehedi'
c.insert(n+1, 12)
print(c)
