

print('hello world!')

print("hello world!")

print(2)

print(2.6)

print("hi")
print("hello")

print("hi",end=' ')
print("hello")

"""python variables

"""

age=20
print(age)

age=20
print("age is ",age)

age=20
print("age= ",age)
print("age= ",age)

a1=120
a2=a1
print(a2)

x=y=z=1
print(x)
print(y)
print(z)

x,y,z=1,2,3
print(x)
print(y)
print(z)

_a=34
print(_a)

"""python datatypes

"""

x=20
y=20.0
z=1+2j

type(x)

type(y)

print(type(x))
print(type(y))
print(type(z))

z=complex(5,6)
print(z)

3#input function
a=input('Enter 1st no: ')
b=input('Enter 2nd no: ')
s=a+b
print(s)
type(a)

#input function
a=int(input('Enter 1st no: '))
b=int(input('Enter 2nd no: '))
s=a+b
print(s)

a=float(input('Enter 1st no: '))
b=float(input('Enter 2nd no: '))
s=a+b
print(s)

a='hello'
print(a+" welcome to python")
print(a,"welcome to python")

print("hello \nworld")

print("hello\n"*5)

#string index

s="python" #index start from 0
s[0]

len(s)#indexig end with len-1

s[-1]#backward indecx start with -1 and ends with -len

s[0:6]#endeig index should be +1of the required index
s[:6]#beg to 5th index
s[1:]#index 1 to end

x='ICT Academy of kerala'
print(x[4:7])
print(x[12:14])
print(x[8:14])
print(x[-6:-3])

s1="mcdonald's"
s1.upper()

s1.lower()

s1.capitalize()

s1.swapcase()

x=True
y=False
print(type(x))
print(type(y))

int(True)

int(False)

bool('')

bool(' ')

bool(6)

bool(-2)

bool(0)

a=10
b=6
a+b

a-b

a*b

a/b

#floor div
a // b #return the qoutient

a%b

#exponential operation
b**2 # bsquare

"""Data Structure"""

#list
list1=['abel','geo','akhil','antony']
type(list1)

l1=[2,"hi",2.0]
type(l1)

l3=list(('apple',10,"Orange",456.2,))
type(l3)

#list indexing
l2=['apple',23,'oramnge','banana',45.5]
l2[0]

len(l2)

l2.append('kiwi')#add element to end of the list

l2

l2.insert(2,'mango')
l2

l2.pop()#dlt last element and return it

l2

l2.pop(3)#dlt from specified index

l2.remove('apple')#dlt specified value

l2

del l2[0]# delete from specified value
l2

l2.clear#dlt all ele from list

l2

l2.clear()

l2

del l2 #dlt specified list

l1.extend(list1)#it add list1 to l1

l1

l1.reverse()

l1

l2=['apple','banana','strawberry']
l2.sort()#sort in asscend

l2

l2.sort(reverse=True)
l2

#list of list
l6=[1,2,3,4,['abel','antony'],True,45.8,[43,7,True]]
l6[3]

l6[4]

l6[4][1]

#Tuples
tuple1=(1,2,3,4)

type(tuple1)

#tuples are immutable (we canntot delete values extend here)

t2=(1,'abel',43.0,True)
type(t2)

t3=tuple((5,6,7,8))
type(t3)

#to edit value in tuple
y=list(t2)
y

y[2]='geo'

t3=tuple(y)
t3

#unpacking a tuple
(a,b,c,d)=t3
print(a)
print(b)
print(c)
print(d)

"""Dictionaries"""

dict1={'john':85,'abel':55,'akhil':30,'antony':10}
type(dict1)

dict2={85:'john',55:'abel',30:'akhil',10:'antony'}
type(dict2)

dict1['john']

dict2[10]

dict1

dict1['john']=22
dict1

marks={'abel':[98,99,97],'Arya':[100,100,100],'geo':[12,1,4]}

marks['geo']

marks['Arya'][2]

marks.get('abel')

marks.keys()

marks.values()

#to add new key in dict
marks.update({'antony':[12,13,18]})
marks

marks['akhil']=[14,12,10]
marks

marks.pop('geo')

marks

marks.popitem() #delete the last key value

marks

del marks['antony']

marks

marks1={'abel':[98,99,97],'Arya':[100,100,100],'geo':[12,1,4]}

marks1.clear()# delete all key values
marks1

del marks1# dele the dict

"""Conditional statements"""

#if condition
price_tv=int(input('Enter the price of TV: '))
if price_tv<=20000:
  print("Pack it")

#if else condition
price_tv=int(input('Enter the price of TV: '))
if price_tv<=20000:
  print("Pack it")
else:
  print("Don't pack it")

#if elif else
#biggest of 3 number
a=float(input('Enter 1st no: '))
b=float(input('Enter 2nd no: '))
c=float(input('Enter 3rd no: '))
if a>b and a>c:
  print(a,' is big')
elif b>a and b>c:
  print(b," is big")
else:
  print(c," is big")

#for loop
for i in range(0,11):
  print(i)

for i in range(0,11,2):#every 2nd val will print
  print(i)

for i in range(10,0,-1):#to print in rev
  print(i)

f=['apple','orange','banana','pineaplle']
for i in f:
  print(i)

s='python'
for i in s:
  print(i.upper())

#while loop
i=0
while(i<10):
  print(i)
  i+=1

#break
i=0
while i<10:
  if i==5:
    break
  print(i)
  i+=1

#continue
i=0
while i<10:
  if i==5:
    i+=1
    continue
  print(i)
  i+=1

