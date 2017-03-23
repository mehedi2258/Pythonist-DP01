#List

'''
list =[16,22]
list.append(16)
print(list)
list.insert(1,22)
print(list)
list.extend([12,2])
print(list)
'''

'''
l_even = [2,4,6,8]
l_odd = [1,3,5,7]
new_list =(l_even+l_odd)
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)
l_even.append(10)
print(l_even)
l_odd.append(9)
print(l_odd)
l_odd.extend([11,13])
print(l_odd)
'''

'''
new_l = [1,2,3,4,['A','B','C'],10]
print(new_l[4][1])  #For print B

print(new_l[1])  #For print 2

print(new_l.index(2))  #For print index number of 2

print(new_l[4].index('A'))  # For print index number of A

print(new_l.clear())
'''



#Set

'''set = set()
set = {}
set = {1,2,3,4}'''

'''
s = set()
s = {}
s = {1,2,3,4}

s.add(5) #Add value 5
print(s)

s.remove(3)
print(s) #Remove  value 3

s.clear() #Clean the set
print(s)
'''

even = {2,4,6,8,10}
odd = {1,3,5,7,9,11}
prime = {2,3,5,7,11}
fibonacci = {1,1,2,3,5,8}

a = odd.union (even)
print(a)

b = odd.intersection(even)
print(b)


'''
s = set()
print(s)

ss ={1, 9, 8}
# initial set and assign value
s = {1, 2, 3, 4}
print(s)
s.add(5)  # add five if it is not in set s
print(s)
s.remove(2)  # for removing item to set
print(s)
s.update(ss)  # add ss set to set s
print(s)
print(s.pop())  # remove and return an element from set
s.clear()  # for cleaning all set
print(s)

even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7}
fib = {1, 1, 2, 3, 5, 8}

even_union_odd = even.union(odd)
print('Even U Odd =', even_union_odd)

even_int_odd = even.intersection(odd)
print('Even n Odd =', even_int_odd)

prime_intersection_fib = prime.intersection(fib)
print('Prime intersection fib =', prime_intersection_fib)

fib_union_prime = fib.union(prime)
print('Fib Union Prime =', fib_union_prime)

unuse_number = even_union_odd.difference(fib_union_prime)
print('Unused number for prime and fib =', unuse_number)
'''



#Dictionary

'''
d = {}  # this is a dist not set
d = dict()
d['name'] = 'Noyon'
d['Name'] = 'Python'
d[1] = 'Number one'
print(d)
print(type(d))
d = dict(name = 'Noyon',
         phone = '01740399036',
         email = 'noyonmassive@gamil.com',
         location = 'DIU')
print(d)
d = {'name' : 'Noyon',
'phone' : '01740399036',
'email' : 'noyonmassive@gamil.com',
'location' : 'DIU'}
d[19] = 'Python calss no 5'
print(d)
print(d['name'])
print(d[19])
print(d.keys())
print(d.values())
#d.clear()
print(d.get('email')) # d['email']
print(d['email'])
print(d.items())
d1 = {'New Dict': 'New Value', 'New Email': 'New Email Value'}
d.update(d1)
print(d)
d['new Dict'] = {'n' : 'Name',
                 'E' : 'Email',
                 "phone" : '029394',
                 'list' : [1, 2, 44, 44, 5],
                 'set' : {1, 2, 3, 3 ,3, 3},
                 'tuple' : (1, 2, 2, 4, 2, 3)}
print(d)
print(d['new Dict']['E'], d['new Dict']['phone'])
print(d['new Dict']['list'][3])
print(d['new Dict']['tuple'].index(2))

for key, value in d.items():
print(key, ' = ', value)
'''



#Tuple

#  first method to create a tuple
t = ()
print(t)
#  Second method to create a tuple
t = tuple()
print(t)

#  Third method to create a tuple
t = 1,
print(t)

#  Fourth method to create a tuple
t = 1, 2, 3, 4, 5
print(t)

#  Fifth method to create a tuple
t = (1, 3, 2, 4, 3, 3, 3, 4, 4, 4, 5, 3)
print(t)

#  count() finction ]
n = t.count(3)  # count how many times 3 is used in this tuple and return count number
print('Number of 3 in use of t tuple is', n, 'times.')
ind = t.index(5)  # return the index number of 5
print('The index number of 5 is', ind)
