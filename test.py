c = 'tu'
print ord(c[0])
print chr(97)
print ord(c[0]) - ord(chr(97))

t = [3,3,4]
t[0] = ord(c[0]) - ord(chr(97))
t[1] = 'hao'
t[2] = 23
print t

print t[-1]
print t[1:]

t[1:2] = [2,1]
print t

t.extend([9,0])
print t
del t[2]
print t

print t.pop(1)
print t

print len(t)

t.append('hao')
t.sort()
print t

t.reverse()
print t

pow2 = []
for x in range(10):
	pow2.append(2 ** x)
	print x
print pow2

print len(pow2)
print sum(pow2)
print min(pow2)
print pow2
pow2[2:4] = [5,4,1]

print pow2
print sorted(pow2)
print pow2

print 2 ** 10

count = 0
for x in 'hello world':
	if x == 'l': 
		count+=1
print count

my_set = set([1,2,3,2])
print len(my_set)
print my_set.pop()



while len(my_set) != 0: 
	my_set.pop()
	
print len(my_set)

my_set.clear()
print len(my_set)

'tap hop'
A = {1, 2, 3, 4, 5, 10, 3}
B = {4, 5, 6, 7, 8}

print A
print len(A)
print A - B
print A ^ B
print A & B

add = ['a', 'b', 'c']
add.append('d')
print(add)


str = 'haohao xin chao'
print str.split(' ')[0]
print str


test1 = [1,2,3,45]
for x in range(len(test1)):
	print test1[x]

for x in test1:
	print x
	
	
arr2 = [['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave',80,80,80,90,95]]

print arr2[1]

for i in range(len(arr2)):
	for j in range(len(arr2[0])):
		print arr2[i][j]
		

		
my_dict = {}

my_dict['age'] = 27

print(my_dict)

# add item
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)


streetno = {}
streetno["1"] = "Sachine Tendulkar" 
streetno["11"] = "121232" 

print streetno


squares = {1: 1, 3: 7, 5: 25, 7: 49, 9: 81}
squares[9] = 1000
for i in squares:
    print(squares[i])




def digitalSumSort(a):
    c = sorted(a,cmp=numeric_compare)
    return c

def numeric_compare(x, y):
    r = xx(x) - xx(y)
    rr = len(str(x)) - len(str(y))
    if r!=0:
        return r
    elif rr!=0:
        return rr
    else:
        return x-y

def xx(st):
    return sum(int(x) for x in str(st))
















