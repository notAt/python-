#coding:utf-8

import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

#append() 添加元素
#extend() 把列表中的元素一个一个拼接到另一个列表
#insert(下标, 元素) 插入
#count() 统计某个元素出现的次数
#index() 某个元素出现的位置
#del names[2]  删除
#names.remove('xiaohong') 删除指定元素
#names.pop() 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#names.sort(reverse=True) 倒叙排列
#enumerate(names) 列举列表的下标与元素

names = ['xiaohong', 'xiaoming', 'laowang']

names.append('dongGe')
a = ['aaa', 'bbb']
names.extend(a)  #['xiaohong', 'xiaoming', 'laowang', 'dongGe', 'aaa', 'bbb']
names.append(a)  #['xiaohong', 'xiaoming', 'laowang', 'dongGe', 'aaa', 'bbb', ['aaa', 'bbb']]
names.insert(0, 'hhe')
del names[2]
names.remove('xiaohong')
names.pop(2)
names.sort()
print(names)



for index,i in enumerate(names):
	names[index] = i+i

print(names)

