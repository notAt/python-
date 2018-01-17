# a 代表追加文件
# r 只读  w 只写 r+ 读写  追加的模式  写入文件在文件末尾  w+ 写读 先写在读  覆盖之前的文件 读取要移动指针位置  a+ 追加读
# rb 读取二进制文件 wb 写入二进制文件
# readlines() 返回列表  一行一个元素
# strip() 去掉空格 换行
# enumerate() 枚举列表 返回元祖（下标，元素）
# tell 当前读取位置
# seek 设置读取位置 不是所有的文件都可以移动的
# seekable 判断是否可以移动 读取位置
# flush() 把文件事实刷新到硬盘
# truncate() 没有参数为清空文件  truncate（10） 截断到第10个元素 从第0个元素开始 不会根据光标移动位置开始

# f = open('../测试文件', 'r', encoding='utf-8')

'''
for line,index in enumerate(f.readlines()):
    print(line, index)
'''

# for line in f:
#     print(line.strip())


import sys,time
'''
for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)
'''

with open('../测试文件', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
