Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> shapes=[S,Z,I,O,J,L,T]
shape_color=[(o,255,0),(255,0,0),(0,255,255),(255,255,0),(255,165,0),(0,0,255),(128,0,128)]
bolk_size=30

class Piece:
    x=10
    y=20
    shape=0
    color=()
    rotation=0
    def_init_(self,column,row,shape):
        self.x=column
        self.y=row
        self.shape=shape
        self.color=shape_colors[shapes.index(shape)]
        self.rotation=0
        
SyntaxError: multiple statements found while compiling a single statement
>>> shapes=[S,Z,I,O,J,L,T]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    shapes=[S,Z,I,O,J,L,T]
NameError: name 'S' is not defined
>>> I=[['..0..',
    '..0..',
    '..0..',
    '..0..',
    '.....'],
   ['.....',
    '0000.',
    '.....',
    '.....',
    '.....']]
>>> o=[['.....',
    '.....',
    '.00..',
    '.00..',
    '.....']]
>>> J=[['.....',
    '.0...',
    '.....',
    '.....'],
   ['.....',
    '..0.',
    '..0..',
    '.....'],
   ['.....',
    '..0..',
    '.00..',
    '.....']]
>>> s=[['.....',
    '.....',
    '..00.',
    '.00..',
    '.....'],
   ['.....',
    '..0..',
    '..00.',
    '...0.',
    '.....']]
>>> Z=[['.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
   ['.....',
    '..0..',
    '.0...',
    '.....']]
>>> L=[['.....',
    '...0.',
    '.000.',
    '.....',
    '.....'],
   ['.....',
    '..0.',
    '..0..',
    '..00.',
    '.....'],
   ['.....',
    '.....',
    '.000.',
    '.0...',
    '.....'],
   ['.....',
    '.00..',
    '..0..',
    '..0..',
    '.....']]
>>> T=[['.....',
    '..0..',
    '.000.',
    '.....',
    '.....'],
   ['.....',
    '..0.',
    '..00.',
    '..0..',
    '.....'],
   ['.....',
    '.....',
    '.000.',
    '..0..',
    '.....'],
   ['.....',
    '..0..',
    '.00..',
    '..0..',
    '.....']]
>>> 
KeyboardInterrupt
>>> shapes=[S,Z,I,O,J,L,T]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    shapes=[S,Z,I,O,J,L,T]
NameError: name 'S' is not defined
>>> shapes=[s,Z,I,O,J,L,T]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    shapes=[s,Z,I,O,J,L,T]
NameError: name 'O' is not defined
>>> 
shapes=[s,Z,I,o,J,L,T]
>>> shape_color=[(o,255,0),(255,0,0),(0,255,255),(255,255,0),(255,165,0),(0,0,255),(128,0,128)]
>>> block_size=30
>>> class Piece:
	x=10
    y=20
    shape=0
    color=()
    rotation=0
    
SyntaxError: unindent does not match any outer indentation level
>>> class Piece:
	x=10
        y=20
        shape=0
        color=()
        rotation=0
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class Piece:
    x=10
    y=20
    shape=0
    color=()
    rotation=0
    def_init_(self,column,row,shape):
        self.x=column
        self.y=row
        self.shape=shape
        self.color=shape_colors[shapes.index(shape)]
        self.rotation=0

    
SyntaxError: invalid syntax
>>> class Piece:
    x=10
    y=20
    shape=0
    color=()
    rotation=0
    def_init_(self,column,row,shapes):
        self.x=column
        self.y=row
        self.shape=shape
        self.color=shape_colors[shapes.index(shape)]
        self.rotation=0
