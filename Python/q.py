Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("-8-6-4-2")
-8-6-4-2
>>> x=0
>>> n=0
>>> for i in range(1,n+1,1):
	x=x+i
	print(x)

	
>>> x=0
>>> n=5
>>> for i in range(1,n+1,1):
	x=x+i
	print(x)

	
1
3
6
10
15
>>> for i in range(1,11):
	for j in range(1,11):
		print("x")

		
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
>>> lastNumber=10
>>> for row in range(1,lastNumber,2):
	print("x")

	
x
x
x
x
x
>>> num=10
>>> c=0
>>> for x in range(1,num,2):
	for y in range(1,x+1):
		c=c+1
		print(c)

		
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
>>> pastry=["Pie","cake","tart"]
>>> fruit=["Apple","Lemon","pumpkin"]
>>> for i in pastry:
	for j in fruit:
		print(i,j)

		
Pie Apple
Pie Lemon
Pie pumpkin
cake Apple
cake Lemon
cake pumpkin
tart Apple
tart Lemon
tart pumpkin
>>> def sumlist(listSalaries):
	sum=0
	i=0
	while(i<len(listSalaries)):
		sum=sum+listSalaries[i]
		i=i+1
		return sum
	