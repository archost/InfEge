def CC(p,k,m):
	m=str(m)
	a=['A','B','C','D','E','F']
	c=[] 
	ten=0 
	power=len(m)
	for i in range(len(m)):
		temp=m[i]
		if temp in a:
			temp=10+(a.index(temp))
		c.append(temp)
	for i in range(power):
		ten+=int(c[i])*(p**(power-i-1))
	if k==10:
		return ten
	else:
		newNum = ''
		while ten > 0:
			if ten%k>9:
				newNum = a[(ten % k)%10] + newNum
			else:
				newNum = str(ten % k) + newNum
			ten //= k
		return newNum

def gcd(p,q):
	if q==0:
		return p
	return gcd(q,p%q)

def lcm(p,q):
	return p*q/gcd(p,q)

def Factor(n):
	a = []
	d = 2
	while d * d <= n:
		if n % d == 0:
			a.append(d)
			n //= d
		else:
			d += 1
	if n > 1:
		a.append(n)
	return a

def Div_Count(n):
	s=Factor(n) 
	p=[]
	i=0
	while i < len(s):
		p.append(s.count(s[i]))
		i+=s.count(s[i])
	print(p)
	k=1
	for i in range(len(p)):
		k*=(p[i]+1)
	return k

def Dividers(n):
	a = []
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			a.append(i)
	half=len(a) 
	for j in range(1,len(a)+1):
		if (n // a[half - j]) not in a:
			a.append(n // a[half - j])
	return a
def Task_23(start,end,multi=[9999],plus=[0],minus=[0],inc=[-1],ex=[-1]):
	if minus[0]!=0:
		start, end = end, start
		plus = minus
	a = [0]*(end+1)
	a[start] = 1
	for i in range(start+1,end+1):
		for j in range(len(multi)):
			if i % multi[j] == 0:
				a[i] += a[i // multi[j]]
		if plus[0]!=0:
			for j in range(len(plus)):
				a[i] += a[i - plus[j]]
		for j in range(len(ex)):
			if i==ex[j]:
				a[i]=0
		for j in range(len(inc)):
			if i==inc[j]:
				for k in range(start,inc[j]):
					a[k]=0
	return a[end]

def Palindrome(n):
	n=str(n)
	for i in range(len(n)):
		if n[i]!=n[len(n)-i-1]:
			return False
	return True

def Prime(n):
	if n<2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

if __name__ == '__main__':
	print("Библиотека InfEge")
__version__ = '0.1'
