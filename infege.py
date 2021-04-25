def gcd(p,q):
	if q==0:
		return p
	return gcd(q,p%q)

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

def DCount(s):
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

if __name__ == '__main__':
	print("Библиотека InfEge")
__version__ = '0.1'