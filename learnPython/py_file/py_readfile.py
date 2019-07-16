# -*- encoding: utf-8 -*-
'''
test python's file operation for reading file.
'''

import os

# print(os.getcwd())
# file_path = os.getcwd() + "\\os_path.py"


# print(os.path.dirname(__file__)) #当前文件所在路径
current_file_path = os.path.dirname(__file__)
file_path = os.path.join(current_file_path, "os_path.py")
print(file_path)

open_file = open(file_path, 'r', True)

while True:
    content = open_file.readline()
    if not content:
        break
    print(content)

