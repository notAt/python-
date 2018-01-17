# coding=utf-8

#集合去重 无序的
# set()创建一个集合


#discard(4) 存在直接删除 不会报错 
s = {1,2,3,4}
s.discard()

iphone7 = {'old_driver', 'rain', 'alex', 'jack'}
iphone8 = {'shanshan', 'jack', 'alex', 'old_boy'}
  
#交集  {'jack', 'alex'}
 iphone8 & iphone7
 iphone8.intersection(iphone7)

 #差集  {'rain', 'old_driver'}
 iphone7 - iphone8
 iphone7.difference(iphone8)

 #并集 {'rain', 'shanshan', 'alex', 'old_boy', 'jack', 'old_driver'}
 iphone7 | iphone8
 iphone7.union(iphone8)

 #对称差集 {'rain', 'shanshan', 'old_boy', 'old_driver'}
 iphone7.symmetric_difference(iphone8)
 iphone7 ^ iphone8


 #是否相交
 iphone7.isdisjoint(iphone8)

 #是否包含其他集合
iphone8.issuperset(iphone7)
iphone8 >= iphone7

#是否被其他集合包含
iphone8.issubset(iphone7)
iphone8 <= iphone7
