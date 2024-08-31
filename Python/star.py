Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> for i in range(1,x+1):
	for j in range(1,i+1):
		print("*",end=" ")
	print()

	
* 
* * 
* * * 
* * * * 
* * * * * 
>>> x=5
>>> for i in range(1,x-1):
	for j in range(1,i-1):
		print("*",end=" ")
	print()

	


* 
>>> x=1
>>> for i in range(5,x-5):
	for j in range(5,i-5):
		print("*",end=" ")
	print()

	
>>> x=5
>>> for i in range(5,0,-1):
	for j in range(0,i):
		print("*",end=" ")
	print()
	