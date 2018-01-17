#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

'''
高阶函数：既然变量可以指向函数，函数的参数能接收变量，
		那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

		函数本身也可以赋值给变量，：即：变量可以指向函数

map（）：接受两个参数，一个是函数，一个是Iterable（可迭代对象），map将传入的
		函数一次作用到序列的每个元素，并把结果作为新的Iterator返回
		python2 返回的是一个list  python3 返回的是一个Iterator
reduce(): reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
		  reduce把结果继续和序列的下一个元素做累积计算
		  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
filter()：接受一个函数和一个序列，根据返回值是True还是False决定保留还是丢弃
'''
#---------------------------高阶函数----------------
# print(abs(-10))
# f = abs
# print(f(-10))

# def add(x, y ,n):
# 	return n(x) + n(y)

# print(add(-5, -6, abs))

# --------------------------map例子------------------
# def f(x):
# 	return x * x

# r = map(f, [1,2,3,4,5,6,7,8,9])
# print(list(r))

#-------------------------reduce例子---------------------
from functools import reduce
# def fn(x, y):
# 	return x * 10 + y
#str也是一个序列，配合map()，可以写出把str转换为int函数
# def char2num(s):
# 	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	return digits[s]

# print(reduce(fn, [1,3,5,7,9]))
# print(reduce(fn, map(char2num, '13579')))

#整理成str2int的函数就是
DISGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return DISGITS[s]
	return reduce(fn, map(char2num, s))

print(str2int('12345'))

#利用lambda函数简化

def char2num(s):
	return DISGITS[s]

def str2int(s):
	return reduce(lambda x,y : x*10+y, map(char2num, s))

print(str2int('123567'))


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
	return name[0].upper() + name[1:].lower()

l = list(map(normalize, ['adam', 'LISA', 'barT']))
print(l)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(l):
	return reduce(lambda x, y: x * y, l)

print(prod([3,5,7,9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

def str2float(s):
    # i = len(s) - s.find('.') - 1
    l = list(s)
    i = len(l) - l.index('.') -1 
    l.remove('.')
    return reduce(fx, map(char2num, l)) * 0.1**i

def char2num(s):
    return DISGITS[s]

def fx(x, y):
	return x * 10 + y; 

print(str2float('3.14'))	


#------------------------filter()---------------------------------
def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd, [1,2,3,4,5,6,7,8])))

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty, ['a', '', 'b', None, 'c'])))


def is_palindrome(n):
	l = str(n)
	return l == l[::-1]

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# print(list(filter(is_palindrome, range(1,200))))


#----------------------------排序------------------------------------
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key=lambda x : x[0])
print(L2)
