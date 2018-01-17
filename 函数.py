#coding:utf-8

import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")


‘’‘
 LEGB代表函数作用域的查找顺序：locals -> enclosing function -> globals -> __builtins__
 	locals 是函数内的名字空间，包括局部变量和形参
 	enclosing 外部嵌套函数的名字空间
 	globals 全局变量，函数定义所在模块的名字空间
 	__builtins__ 内置模块的名字空间
’‘’


def sum2num(num1, num2, num3=50):
	print(num1+num2+num3)

sum2num(165,38)


num = 100
#全局变量：如果想要在函数里面更改需要加 global进行声明
# *args 不定长参数，可以传多个
# **kwargs  关键字参数
def test1():
	global num
	print(num)
	num += 2
	print(num)


def test2(a,b,*args,**kwargs):
	print('='*30)
	print(a)
	print(b)
	print(args)
	print(kwargs)


test1()
# test2(11,22,33,44,55,66,mm=11)

list = [11,22,77]
dict = {'A':100, 'B':200}
test2(11,22,*list,**dict)

#---------------------------lambda匿名函数---------------------
#格式 lambda 参数：表达式
aaa = lambda a:a+1
print(aaa(6))

ary = [{'age':123, 'sorce':123}, {'age':13, 'sorce':2345}, {'age':12123, 'sorce':12}, {'age':234, 'sorce':14}]

ary.sort(key=lambda x:x['age'])
print(ary)

def calc(x, y):
		if x < y:
				return x*y
		else:
				return x/y	

func = lambda x,y: x*y if x < y else x/y
print(func(16,8))
