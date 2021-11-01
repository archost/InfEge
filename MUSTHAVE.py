######### CC ##########
def CC(p,k,m):
	m=str(m)
	a=['A','B','C','D','E','F']
	ten=int(m,p)
	N=''
	if k==10:
		return ten
	else:
		while ten:
			if ten%k>9:N+=a[(ten%k)%10]
			else:N+=str(ten%k)
			ten//=k
		return N[::-1]

######### 2 ЗАДАНИЕ ##########
def F(x,y,z,w):
	return (x and y and w and z)
for i in range(16):
	temp=i
	mask=[]
	for j in range(4):
		mask.append(temp%2)
		temp//=2
	f=F(mask[3],mask[2],mask[1],mask[0])
	#if f:
	for j in reversed(range(4)):
		print(mask[j],end='')
	print('',int(f))

######### 8 ЗАДАНИЕ ##########
from itertools import product
k=0
for i in product('ПРИКАЗ',repeat=4):
	s = ''.join(i)
	if all(s.count(x)<=1 for x in 'ПРИКАЗ') and (not('А' in s and 'И' in s)):
		k+=1
print(k)

######### 15 ЗАДАНИЕ ##########
#ОТРЕЗКИ, МНОЖЕСТВА. P = [10,25], Q = [27,81]
def F(x,a):
	return (x in a) <= ((x not in Q) and (x in P))
P = set([i/10 for i in range(100,250+1)])
Q = set([i/10 for i in range(270,810+1)])

a = set()
#a = set([i/10 for i in range(10000)]) для максимума
for x in [i/10 for i in range(10000)]:
	if not F(x,a):
		a.add(x)
		#a.remove(x) для максимума
print(sorted(a))

#ДЕЛ, ПОРАЗРЯДКА.
def F(x,a):
	return (x & a != 0) <= (x%a == 0)
for a in range(1,1000): #range(1000,1,-1) для максимума
	ok = True
	for x in range(1,10000):
		if not F(x,a):
			ok=False
			break
	if ok:
		print(a)
		break

#НЕРАВЕНСТВА
def F(a,x,y):
	(x**2 - 3*x + 2 > 0) or (y > x**2 + a) 
from itertools import product
for a in range(100): #range(100,1,-1) для максимума
	ok = True
	for x,y in product(range(1,1000), repeat=2):
		if not F(a,x,y):
			ok = False
			break
	if ok:
		print(a)
		break

######### 18 ЗАДАНИЕ ##########
#ПОСЛЕДОВАТЕЛЬНОСТЬ ВЕЩЕСТВЕННЫХ ЧИСЕЛ
f = open('18.txt')
x = f.readlines()
for i in range(len(x)):
	x[i]=x[i].replace(',','.')
	x[i]=x[i].replace('\n','')

prev=float(x[0])
#предыдущий элемент
summ=prev
#сразу суем его в сумму
maxs=0
for i in range(1,len(x)):
	s=float(x[i])
	#считываем 1 элемент
	if s > prev:
		#если текущий больше предыдущего, это удовлетворяет условиям
		#добавляем в сумму
		summ+=s
	else:
		#если условие не выполняется, последовательность прервалась
		#поэтому обновляем максимальную сумму, И!!..
		maxs=max(maxs,summ)
		summ=s #вот сюда 
#..и текущий элемент сохраняем в предыдущий, а его значение в текущую сумму!
	prev=s
maxs=max(maxs,summ)
print(int(maxs))

######### ТЕОРИЯ ИГР (19-21) ##########
#ОДНА КУЧА
from functools import lru_cache
def moves(h):
	return h+1, h+2, h*3
@lru_cache(None)
def f(h):
	if h>54:
		return 'END'
	elif any(f(x)=='END' for x in moves(h)):
		return 'П1'
	elif all(f(x)=='П1' for x in moves(h)):
		return 'В1'
	elif any(f(x)=='В1' for x in moves(h)):
		return 'П2'
	elif all(f(x)=='П1' or f(x)=='П2' for x in moves(h)):
		return 'В2'
for i in range(1,100):
	print(i,f(i))

#ДВЕ КУЧИ
from functools import lru_cache
def moves(h):
	a,b=h
	return (a+1,b),(a,b+1),(a*2,b),(a,b*2)
@lru_cache(None)
def f(h):
	if sum(h)>=74:
		return 'END'
	elif any(f(x)=='END' for x in moves(h)):
		return 'П1'
	elif all(f(x)=='П1' for x in moves(h)):
		return 'В1'
	elif any(f(x)=='В1' for x in moves(h)):
		return 'П2'
	elif all(f(x)=='П1' or f(x)=='П2' for x in moves(h)):
		return 'В2'
for i in range(1,100):
	h=12,i
	print(i,f(h))

######### 23 ЗАДАНИЕ ##########
a = [0]*(end+1)
a[start] = 1
for i in range(start+1, end+1):
	a[i]+=a[i - plus]
	if i%multi==0:
		a[i]+=a[i//multi]
	if i==ex:
		a[i]==0
	if i==inc:
		for j in range(start, inc):
			a[j]=0
print(a[end])

######### 24 ЗАДАНИЕ ##########
#ПЕРЕБОР N-ОК С ПЕРЕСЕЧЕНИЯМИ.
k=0
s=input()
for i in range(len(s)-n+1):
	if s[i:i+n]=='COCKC...':
		k+=1
print(k)

#КОЛИЧЕСТВО КОМБИНАЦИЙ БЕЗ ПЕРЕСЕЧЕНИЙ. (Определите максимальное количество подряд идущих комбинаций «KOT»)
f = open('2546.txt')
s = f.readline()+'*'
f.close()
s = s.replace('KOT','Z')

k=0
m=0
for i in range(len(s)):
	if s[i]=='Z':
		k+=1
	else:
		m=max(k,m)
		k=0
print(m)

#ASCII - просто сравнивай символы.
#Вернуть код ASCII: ord('A')
#Это цифра? if s[i] in '0123456789' или if '0' <= s[i] <= '9'

#МНОЖЕСТВА. (Сколько раз встречаются комбинации «BOSS» при этом до и после этого слова нет символа «J»? комбинации «JBOSS», «BOSSJ» и «JBOSSJ» не учитываются)
print(s.count('BOSS')-s.count('JBOSS')-s.count('BOSSJ')+s.count('JBOSSJ'))

######### 25 ЗАДАНИЕ ##########
def Prime(x):
	if x<=2:
		return True
	if x%2==0:
		return False
	for i in range(3,int(x**0.5)+1,2):
		if x%i==0:
			return False
	return True

def Dividers(n):
	a = []  
	for i in range(1, int(n ** 0.5) + 1):  
		if n % i == 0:
			a.append(i)
	half=len(a) 
	for i in range(1,half+1): 
		if (n // a[half - i]) not in a: 
			a.append(n // a[half - i])
	return a

n=12
sieve = [0]*(n+1)
for i in range(2,n+1):
	if sieve[i]: continue 
	for j in range(i*2,n+1,i): 
		sieve[j]=1
for x in range(n+1):
	if not sieve[x]:
		print(x)

######### 26 ЗАДАНИЕ #########
m = float('inf') #для минимума

#СТАНДАРТНОЕ
f = open('2617.txt')
s, n = map(int, f.readline().split())

a = [int(f.readline()) for i in range(n)]
a.sort()

#заполнение
b = []
for x in a:
	if sum(b)+x <= s:
		b+=[x]

#заполнение до конца
k=-1
while sum(b) < s:
	for x in a:
		if x <= b[k] + (s-sum(b)):
			m = x
	b[k] = m
	k-=1

print(b)
print(len(b),max(b))

#ПЕРЕБОР ВСЕХ ПАР В СПИСКЕ a
a = [1,2,3,4,5]
for i in range(len(a)-1):
	for j in range(i+1, len(a)):
		print(a[i], a[j])

#БИНАРНЫЙ ПОИСК
def bin_search(l,el):
	st, end = 0, len(l)-1
	while st<end:
		k = (st+end)//2
		if l[k]>=el:
			end = k
		else:
			st = k + 1
	return l[st]==el

#С ПОМОЩЬЮ БИБЛИОТЕКИ bisect (быстрее)
from bisect import bisect_left
def Contains(l, el):
	index = bisect_left(l, el)
	if index < len(l):
		return l[index] == el
	return False

#А ЕЩЕ БЫСТРЕЕ И ПРОЩЕ ИСПОЛЬЗОВАТЬ МНОЖЕСТВА (set) НУ ИЛИ СЛОВАРИ (dict). РАБОТАЕТ ЗА O(1)
c = 'наличие чего в отсортированном списке a нужно определить'
d = [x:('любое значение') for x in a]
if c in d:
	pass

s = set(x for x in a)

if c in s:
	pass

################# 27 ЗАДАНИЕ #################
# М Ч С
f = open('f/2681b.txt')
n=int(f.readline())
def get():
	return list(map(int, f.readline().split()))
s = get()
for _ in range(n-1):
	pair = get()
	combi = [a+b for a in s for b in pair]
	s1 = [0]*10
	for x in combi:
		s1[x%10] = max(s1[x%10], x)
	s = [x for x in s1 if x!=0]
print(s)

