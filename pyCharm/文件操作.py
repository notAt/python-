# f.write('姓名   地址  身高  年龄  电话\n')
# f.write('王心凌 上海   170   25   13137124750\n')
# f.write('哈哈 上海   170   25   13137124750\n')
# f.write('呵呵 上海   170   25   13137124750\n')
# f.write('嘟嘟 上海   170   25   13137124750\n')
# f.close()


f = open('兼职模特.txt', 'r+', encoding='utf-8')

old_name = '王心凌'
new_name= '罗志祥'

new_list = []

for line in f:
    if old_name in line:
        line = line.replace(old_name, new_name)

    new_list.append(line)


f.seek(0)
f.truncate(0)
f.writelines(new_list)


f.close()

