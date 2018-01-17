# coding=utf-8

info = {"name":'heh'}

iphone7 = ['alex', 'rain', 'jack', 'old_driver']
iphone8 = ['alex', 'shanshan', 'jack', 'old_boy']

both_list = []

for name in iphone7:
    if name in iphone8:
        both_list.append(name)

print(both_list)