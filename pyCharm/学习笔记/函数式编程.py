
#关键字必须在位置参数后面

# def test():
#     print('in the action')

'''
def test1(x,y,z):
    print(x)
    print(y)
    print(z)

def test2(*args):
    print(args)

def test3(**kwargs):
    print(kwargs)

test1(1,3, z = 2)

# test2(1,2,23,3,4,54,5,5,5)
test2(*[1,2,3,4,45,3,3,2,1])

# test3(name = 'hehe', age = 8, sex = 'f')
test3(**{'name':'hehe', 'age':8, 'sex':'f'})
'''

'''
   装饰器
 1.函数即'变量'
 2.高阶函数
 3.嵌套函数
'''

def logger(func):
    def war(*args, **kwargs):
        print('这是一个测试')
        return func(*args, **kwargs)
    return war

@logger
def test(a):
    print('This is test', a)


test(2)

