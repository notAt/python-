
#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。

#isinstance('a', str) 判断一个元素是否是str类型


g = (x * x for x in range(10))
next(g) 

def ceshi(n):
	L = [1]
	while len(L) < n+1:
		yield L
		# print(L)
		L.append(0)
		L = [L[i-1] + L[i] for i in range(len(L))]

for n in ceshi(10):
	print(n)

# ceshi(10)
print(range(2))