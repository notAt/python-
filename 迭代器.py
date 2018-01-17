#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

from collections import Iterable
from collections import Iterator

#isinstance('a', str) 判断一个元素是否是str对象
#可迭代对象为 Iterable isinstance([], Iterable) 判断列表是否为可迭代对象
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数

print(isinstance(iter([]), Iterator))
print(isinstance([], Iterable))