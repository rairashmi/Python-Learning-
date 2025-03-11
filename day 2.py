Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2 + 3
5
x = 2
x + 3
5
y = 3
X = Y
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X = Y
NameError: name 'Y' is not defined. Did you mean: 'y'?
x + y
5
x = 9
x + y
12
x
9
abc
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
x + 10
19
19 + y
22
_ + y
25
name = 'youtube'
name
'youtube'
name + 'rocks'
'youtuberocks'
name 'rocks'
SyntaxError: invalid syntax
name[0]
'y'
name[6]
'e'
name[8]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name[8]
IndexError: string index out of range
name[-1]
'e'
name[-2]
'b'
name[-7]
'y'
name[0:2]
'yo'
name[1:4]
'out'
name [1:]
'outube'
name[:4]
'yout'
name[3:10]
'tube'
name[0:3] ='my'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[0:3] ='my'
TypeError: 'str' object does not support item assignment
'my' + name[3:]
'mytube'
myname = ' Rashmi Rai'
len(myname)
11
Type "help", "copyright", "credits" or "license()" for more informationType "help", "copyright", "credits" or "license()" for more information.
SyntaxError: invalid syntax




11
11

List ----
SyntaxError: invalid syntax
name = [25,12,36,95,14]
nums
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    nums
NameError: name 'nums' is not defined
nums = [ 25,12,36,95,14]
nums
[25, 12, 36, 95, 14]
nums[0]
25
nums[4]
14
nums[2:]
[36, 95, 14]
nums [-1]
14
nums [-5]
25
names = ['Rashmi','kiran', 'Navin']
names
['Rashmi', 'kiran', 'Navin']
values = [9.5, 'Rashmi', 25]
mil = [nums, names]
mil
[[25, 12, 36, 95, 14], ['Rashmi', 'kiran', 'Navin']]
nums.append(45)
nums
[25, 12, 36, 95, 14, 45]
nums.insert(2,77)
nums
[25, 12, 77, 36, 95, 14, 45]
nums.remove(14)
nums
[25, 12, 77, 36, 95, 45]
nums.pop(1)
12
nums
[25, 77, 36, 95, 45]
[25, 77, 36, 95, 45]
[25, 77, 36, 95, 45]
nums.pop()
45
del nums[2:]
nums
[25, 77]
nums.extend([29,12,14,36])
nums
[25, 77, 29, 12, 14, 36]
min(nums)
12
max(nums)
77
sum(nums)
193
nums.short()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    nums.short()
AttributeError: 'list' object has no attribute 'short'. Did you mean: 'sort'?
nums
[25, 77, 29, 12, 14, 36]
nums.sort()
nums
[12, 14, 25, 29, 36, 77]


Tuple & set
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    Tuple & set
NameError: name 'Tuple' is not defined. Did you mean: 'tuple'?



tup = (21,36,14,25)
tup
(21, 36, 14, 25)
tup[1]
36
tup[1] - 33
3
tup[1]= 33
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    tup[1]= 33
TypeError: 'tuple' object does not support item assignment
s = {22,25,14,21,5}
s
{5, 21, 22, 25, 14}
s = {25,14,98,63,75,98}
s
{98, 25, 75, 14, 63}
s[2]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
nums = [25, 36,95,14,12,26]
nums.remove(95,14,12)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    nums.remove(95,14,12)
TypeError: list.remove() takes exactly one argument (3 given)
nums
[25, 36, 95, 14, 12, 26]
nums = [25,36,95,14,12,26]
nums
[25, 36, 95, 14, 12, 26]
nums.remove(95,14,12)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    nums.remove(95,14,12)
TypeError: list.remove() takes exactly one argument (3 given)
nums
[25, 36, 95, 14, 12, 26]
del[95,14,12]
SyntaxError: cannot delete literal
del[2,3,4]
SyntaxError: cannot delete literal
del nums[95,14,12]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    del nums[95,14,12]
TypeError: list indices must be integers or slices, not tuple
>>> nums.remove[95,14,12]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    nums.remove[95,14,12]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> del [2:4]
SyntaxError: invalid syntax
>>> del [2 : 4]
SyntaxError: invalid syntax
>>> del nums [2 : 4]
>>> nums
[25, 36, 12, 26]
>>> Dictionary in python
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    Dictionary in python
NameError: name 'Dictionary' is not defined
>>> 
>>> data = {1:'rashmi',2:'Navin', 4:'Harsh'}
>>> data
{1: 'rashmi', 2: 'Navin', 4: 'Harsh'}
>>> data[4]
'Harsh'
>>> data[1]
'rashmi'
>>> data[3]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    data[3]
KeyError: 3
>>> data.get(1)
'rashmi'
>>> data.get(3)
>>> print (data.get(3))
None
>>> data.get(1,'Not found')
'rashmi'
>>> data.get(3,'Not found')
'Not found'
>>> keys = ['Rashmi','Navin','Harsh']
>>> values = ['Python','Java','JS']
