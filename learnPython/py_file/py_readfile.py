# -*- encoding: utf-8 -*-
'''
test python's file operation for reading file.
'''

import os

# print(os.getcwd())
file_path = os.getcwd() + "\\os_path.py"
print(file_path)

open_file = open(file_path, 'r', True, "utf-8")
try:
    while True:
        content = open_file.readline()
        if not content:
            break
        print(content, end=' ')
finally:
    open_file.close()
