def Impl(x,y):
	return x <= y
def Plus(x,y):
	return x or y
def Multi(x,y):
	return x and y
def Not(x):
	return not x
def F(a): 
	return Multi(Not(a[2]),a[0])

def Perm(perm, arr, table):
	n=len(arr)
	if n==0: 
		correct=True
		for j in range(m):
			print(perm,table[j],j)
			if not(Correct(perm,table[j])):
				correct=False
				print("break")
				break
		if correct:
			for k in range(len(table[0])-1):
				print(s[perm[k]], end=' ')
			print()
	else:
		for i in range(n):
			arr1=[] 
			perm1 = perm.copy()
			perm1.append(arr[i])
			for j in range(n):
				if j!=i:
					arr1.append(arr[j])
			Perm(perm1, arr1, table)

def Correct(perm, table_d):
	a=[0]*(len(table_d)-1)
	for i in range((len(table_d)-1)):
		a[perm[i]] = table_d[i]
	print("---",a,F(a),table_d,table_d[len(table_d)-1])
	if F(a) == table_d[len(table_d)-1]:
		return True
	return False

arr = []
s = ['x', 'y', 'z', 'w']
m=int(input())
table = [0]*m
for i in range(m):
	table[i] = list(map(int, input().split()))
for i in range(len(table[0])-1):
	arr.append(i)

Perm([], arr, table)
