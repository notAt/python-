#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

# name = 'abcdesf'
# name[起始位置:结束位置:步长]
#------------------------字符串常见操作-------------------------------
#find() 查找字符串中的某个字符 返回 下标  下标为负数表示没有找到

#index() 跟find()一样，找不到会报异常

#rfind() rindex() 从右开始找

#count(‘a’) 字符串有多少个a

#replace('原字符'， ‘新字符’， 替换几次)

#split(' ', 2) 以空格来分隔 分隔两次 返回列表

#split() 没有参数，默认的空格 \t都会被分隔掉

#splitlines() 以换行符来分隔

#‘python’ is aStr  判断'python'和aStr内存地址是否相同

#‘python’ in aStr  判断aStr是否包含‘python’

#strip() 删除开头结尾的空格

#lstrip()  rstrip() 左右删除

#partition(str) 把字符串以str分割三部分，str前，str和str后 返回元祖 

#isalpha() 判断是否为纯字母

#isdigit() 判断纯数字

#isalnum() 判断是否为数字或字母或组合

#isspace() 判断是否只包含空格

#str.join() 把列表中的每个元素以str分隔连接

aStr = 'hello python and it castpython'
print(aStr.find('and'))

print(aStr.rfind('python'))

print(aStr.replace('py', 'Py', 2))

print(aStr.split(' ', 2))

print('python' in aStr)

a = b = "asdf"

print(a is b)

a = 'asdf\nsdf\nasdf\nndf'

print(a.splitlines())

print(aStr.isalpha())

print(aStr.isdigit())

print(aStr.isalnum())

c = "_"
myName = ['aaa', 'bbb', 'ccc']
print(c.join(myName))

if a == 'asdf' or b == 'asdf':
	print('hehe')

