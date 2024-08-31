Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range(1,16):
	for y in range(1,6):
		print(":)")

		
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
>>> 
KeyboardInterrupt
>>> 35%5*55-24
-24
>>>  for x in range(1,16):
	for y in range(1,6):
		print(":)")
		
SyntaxError: unexpected indent
>>> for x in range(1,16):
	for y in range(1,6):
		print(":)")

		
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
:)
>>> def do_thing(x,y):
	if x>y:
		return x
	return y

>>> 4
4
>>> 5
5
>>> 4 5
SyntaxError: invalid syntax
>>> def do_thing(x,y):
	if x>y:
	    return x
	return y

>>> 4,5
(4, 5)
>>> x=0
>>> y=0
>>> count =2
>>> while x>25:
	while y>50:
		count+=2
		y+=4
	x+=2
	print(count)

	
>>> list=["cake","Pie","tart","croissant"]
>>> list.pop(2)
'tart'
>>> list.remove("cake")
>>> list.append("Toffee")
>>> list.pop()
'Toffee'
>>> list.insert(1,"chocolates")
>>> print(list)
['Pie', 'chocolates', 'croissant']
>>> s="Hello"
>>> p="world"
>>> r"coder!"
'coder!'
>>> new=s+p+r
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    new=s+p+r
NameError: name 'r' is not defined
>>> print(new[10:17])