# -*- encoding: utf-8 -*-

'''
练习对文件的写操作
'''

import os

current_path = os.path.dirname(__file__)
print(current_path)

with open("test1.txt", 'w+', encoding='utf8') as write_file:
    write_file.write("This is 测试 text file"+os.linesep) # os.linesep是添加换行符

with open("test2.txt", 'ab+') as write_file_b:
    write_file_b.writelines((("确认是否为多行"+os.linesep).encode('utf-8'), ("确认这个是第二行"+os.linesep).encode('utf-8')))


with open("test1.txt", "r") as read_test1:
    content1 = read_test1.read()


with open("test2.txt", "r") as read_test2:
    content2 = read_test2.read()

content3 = content1 + content2

with open("test3.txt", "w+", encoding='utf8') as write_test3:
    write_test3.write(content3)


expect_path = os.path.join(current_path,"test")

if os.path.exists(expect_path):
    print("The path has exsisted: " + expect_path)
    os.removedirs(expect_path)
    print("The path is removed: " + expect_path)
else:
    os.mkdir(expect_path)
    print("create the path successfully: " + expect_path)


list_dir = os.listdir(current_path)
for item in list_dir:
    print(item)

