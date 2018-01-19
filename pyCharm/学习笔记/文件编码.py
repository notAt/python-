# Unicode 每个字母和中文都占2个字节 16位
# utf-8 字母为1个字节 中文为3个字节

'''
    python2 GBK需要转换为UTF-8格式流程
1.首先通过编码【decode】转换为Unicode编码
2.然后通过解码【encode】转换为UTF-8的编码

    python3 可以直接转
'''

s = '你好'
s_to_gbk = s.encode('gbk')
print(s_to_gbk)