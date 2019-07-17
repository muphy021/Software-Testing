# -*- encoding: utf-8 -*-

'''
练习对文件的写操作
'''

import os

current_path = os.path.dirname(__file__)
print(current_path)

with open("test.txt", 'w+', encoding='utf8') as write_file:
    write_file.write("This is 测试 text file"+os.linesep) # os.linesep是添加换行符

with open("test.txt", 'ab+') as write_file_b:
    write_file_b.writelines((("确认是否为多行"+os.linesep).encode('utf-8'), ("确认这个是第二行"+os.linesep).encode('utf-8')))

