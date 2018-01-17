#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

import os

#seek(offset, from) offset 偏移量 from方向：0：表示开头  1表示当前位置  2表示文件末尾 
#tell 当前偏移量 
# w+ 写读  先写后读 会清空之前有的东西  r+ 读写  先读后写  以读的模式打开能继续编辑
# w 文件写的操作  会先把文字写在内存里面  close（）的时候在写到硬盘  flush() 可以把东西强制写到硬盘
# os.rename(新名字，旧名字)  重命名文件名 
f = open('/Users/edz/Desktop/text.txt','w+')
f.write('woshiniba \n aslk;fja\njashkdfja\njakshfjk\n')
f.seek(0)
print(f.readlines())
print(f.tell())


