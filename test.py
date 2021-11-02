#ПЕРЕМЕННЫЕ
'''
большой
комментарий
'''
#int, float, str, bool
test = 5
fnum = 1.2
s = 'string'
s1 = "string"
status = True
age = 17

#ВВОД ВЫВОД, СТРОКИ
print('вечно', age, sep = ' ', end= '\n')
h = 'вечно' + ' ' + str(age)
print(h)

#fisrt, second = map(int, input().split())

#name = input()
name = 'Соня'
print('Меня зовут', name)
print(len(name))
print('с' in name)

s = 'hello world'
print('count', s.count('o'))
print(s.replace('o', '_'), s)
s = s.replace('o', '_')
print(s)
print(s.split())

#num = int(input())
#print(num + 1)


#ОПЕРАЦИИ
a = 5
b = 7
c = 5*7
d = b/a
e = b//a
f = a+b-c
g = b%a
a = -a
a, b = b, a
print(a, b)


#СПИСКИ. СРЕЗЫ

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

numbers.append(9)

print(numbers[0], numbers[-1])

print('min =', min(numbers))

print('max =', max(numbers))

print(len([1,2,3,4,5]))

print(sum(numbers))

del numbers[2]

print(numbers)

#spisok = list(map(int, input().split()))

print(numbers[1:5:2])

rev = numbers[::-1]

copy = numbers[:]

v = [1, 2, [3, 4]]
print(v[2][0])

a = [1,2,2,2,3]
print(a.count(2))

a.reverse()

print(a)

a.sort()
#a.sort(reverse=True)

print(a)

a.remove(1)
print(a)


#УСЛОВИЯ
#not->and->or
if not (a == b) or (c != d) and (f >= g):
	print('1')
elif a%2==0:
	print('2')
else:
	print('3')

#while
i=1
while i<6:
	print(i)
	i+=1

a = [1,2,3,3]
while 3 in a:
	a.remove(3)
	print('iteration')


#МОДУЛИ
import math
print(math.pi)

#Break, Continue
'''
while True:
	a = input()
	if a =='exit':
		break

while True:
	#a = input()
	if a =='exit':
		break
	if a == 'c':
		continue
	print('iteration')
'''
#FOR
print(list(range(5)))

for i in [0,1,2,3,4]:
	print(i)

for i in range(5):
	print(i)

#ОБХОД СПИСКОВ
a = [12,13,46,74,90,112,24]

for i in range(len(a)):
	print(a[i])

for i in a:
	print(i)

#ФУНКЦИИ
def sayhello():
	print('hello')

sayhello()

def square(x):
	print(x**2)

a = 5
square(a)

def square(x):
	return(x**2)

b = square(3)
print(b)

def SaP(x,y):
	return x**2, 2*(x+y)

