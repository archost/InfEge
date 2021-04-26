def gcd(p,q):
	#Вычисление НОД(наибольший общий делитель) числа по алгоритму Евклида
	#Основан на том, что НОД(a,b)=a, если b=0 и НОД(a,b)=НОД(b, a mod b), если b!=1.
	#Первое очевидно, т.к. 0 делится на любой число, а второе нетрудно доказать.
	if q==0:
		return p
	return gcd(q,p%q)

def lcm(p,q):
	#Вычисление НОК(наименьшее общее кратное) двух чисел
	#Основано на формуле НОК(a,b) = (a*b)/НОД(a,b)
	return p*q/gcd(p,q)

def CC(p,k,m):
	m=str(m)
	#перевод числа m из сс с основанием p в сс с основанием k
	a=['A','B','C','D','E','F']
	c=[] #это для цифр, в том числе для букв А,В,С,.. в десятичном представлении
	ten=0 #здесь будет храниться 10-ичная запись числа
	power=len(m) #нужен для перевода из p в 10 (степень, в которую будет возводиться основание при умножении на цифры числа)

	#это строку вида A24B4D преобразовывает в [10,2,4,11,4,13]
	for i in range(len(m)):
		temp=m[i]
		if temp in a:
			#если этот символ есть в списке а, значит это сс с основанием больше 9
			#a.index(temp) возвращает индекс элемента. Удобно то, что А с индексом 0, В с индексом 1 и т.д., т.к. А=10, а В=11. Можно легко 
			#записать операцию так, как это сделано:
			temp=10+(a.index(temp))
		c.append(temp)

	#перевод собственно из p в 10                                                           3 2 1 0
	#список с содержит "цифры" исходного числа, то есть А=10, В=11 и т.д. Перевод идет так: a b c d (n) = a*n^3 + b*n^2 + c*n + d*n^0 (10)
	#a,b,c,d это и есть значения из списка с.
	for i in range(power):
		ten+=int(c[i])*(p**(power-i-1))

	#если требуется перевести в 10-ичную сс, мы это уже сделали. Возвращаем.
	if k==10:
		return ten

	#Ну а если нет, то сюда. Создается новая пустая строка. Остаток от деления ten (10-ичного числа) на основание новой сс приписывается новой 
	#строке спереди. Почему? Потому что когда мы переводим из 10 в другую сс, мы делим на основание, а потом записываем остатки в обратном
	#порядке. Здесь они сразу вперед записываются, поразрядно. Если ten % k  >  9 (то есть если остаток, который мы собираемся 
	#приписывать, больше 9, то нужно его представлять в виде буквы). Делается это несложно, опять-таки потому что А с индексом 0, В с индексом 1
	#и т.д. Мы берем остаток от деления остатка(который нужно приписать) на 10, таким образом находим индекс нужного элемента в а (0-А,1-В и т.д)
	#ну и в конце ten нацело делится на 10, убирая уже переконвертированный разряд. 
	else:
		newNum = ''
		while ten > 0:
			if ten%k>9:
				newNum = a[(ten % k)%10] + newNum
			else:
				newNum = str(ten % k) + newNum
			ten //= k
		return newNum
	
def Factor(n):
	#Функция, возвращающая список с делителями числа n. 
	#Если число p входит в разложение больше, чем в 1 степени, то оно просто повторяется. Например Factor(4) -> [2,2]
	a = [] #в этот список будут добавляться делители
	d = 2 #первый простой множитель, на который будем делить - 2
	while d * d <= n:
		if n % d == 0: #если делится, добавляем в список как простой множитель
			a.append(d)
			n //= d #а затем делим на него нацело
		else:
			d += 1 #если не делится, прибавляем 1, делим на другое число. 
			#деления на не простое число не произойдет, т.к. когда d дойдет до не простого, например 4, то все 2 из факторизации уже будут удалены
	if n > 1:
		a.append(n) #добавляем оставшееся после деления число, не поделившееся больше ни на что(если конечно оно больше 1)
	return a

def Div_Count(s):
	#Нахождение количества делителей числа n, которое имеет разложение s. На вход подается список делителей как из Factor.
	#То есть испоьзование выглядит так: Div_Count(Factor(n)). Factor(n) вернет раложение, а потом передаст его в Div_Count.
	#Согласно ОТА (основной теореме арифметики), каждое натуральное число n>1 можно единственным образом представить в виде:
	#p1^a1 * p2^a2 * ... * pn^an, где p1,p2,...,pn - простые числа, а a1,a2,...,an - натуральные (показатели)
	#При этом количество N делителей числа n находится по формуле N = (a1+1)*(a2+1)*...*(an+1), то есть к каждому показателю +1 и перемножить все
	p=[] #в список p мы поместим степени каждого множителя, то есть если например Factor(68) = [2,2,17], то мы считаем количество
	#уникальных множителей, то есть 2 двойки и одна 17. В список p должно пойти [2,1] - степени простых множителей в факторизации в порядке возрастания
	i=0 
	while i < len(s):
		#для этого будем добавлять в наш массив количество уникальных простых множителей с помощью s.count(x), которая считает, сколько раз встречается в списке значение x
		#а потом к индексу прибавляем это количество, чтобы не было повторений и мы сразу перешли бы к следующему простому числу
		p.append(s.count(s[i]))
		i+=s.count(s[i])
	print(p)
	#ну а дальше по формуле: к каждому показателю(значению списка p, там же теперь только показатели хранятся) прибавляем 1 и все это дело перемножаем в k
	k=1
	for i in range(len(p)):
		k*=(p[i]+1)
	return k
