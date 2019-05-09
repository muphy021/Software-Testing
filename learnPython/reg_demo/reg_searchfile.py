# -*- encoding: utf-8 -*-

'''
目的：从文件中查找关键字

使用：python能从文件中查找关键字的功能 - re正则

功能：1. 遍历文件夹和文件
     2. 与后缀无关: r'.+?(\.*)?'
     3. 文本文件: 与文件类型无关

学习：
1. 文件的操作，读取，
2. 正则表达式，查找文件及其内容
3. 列表保存

'''
import os
import re
import sys #获取命令行参数

'''
需要模块：sys
参数个数：len(sys.argv)
脚本名：    sys.argv[0]
参数1：     sys.argv[1]
参数2：     sys.argv[2]
'''

regtxt = r'.+?(\.*)?' #扫描文件,可以有后缀，也可以无后缀
# regcontent = r'.password.' #列出内容含有'*****'的文件
# regcontent = sys.argv[2]
regcontent = r'.password.'
class FileException(Exception):
    pass


def getdirlist(filepath, regcontent):
    """获取目录下所有的文件."""
    txtlist = [ ]  # 文件集合.
    txtre = re.compile(regtxt)
    needfile = [ ]  # 存放结果.

    for parent, listdir, listfile in os.walk(filepath):
        for files in listfile:
            # 获取所有文件.
            istxt = re.findall(txtre, files)
            filecontext = os.path.join(parent, files) # parent表示和file同级的目录
            # 获取非空的文件.
            if istxt:
                txtlist.append(filecontext)
                # 将所有的数据存放到needfile中.
                needfile.append(readfile(filecontext))
    if needfile == []:
        raise FileException("no file can be find!")
    else:
        validatedata = getvalidata(needfile)
        print(validatedata)
        print('total file %s , validate file %s.' % (len(txtlist), len(validatedata)))
        # print 'total file %s , validate file %s.' % (len(txtlist), len(needfile))

def getvalidata(filelist=[]):
    """过滤集合中空的元素."""

    valifile = []
    for fp in filelist:
        if fp != None:
            valifile.append(fp)
    return valifile

def readfile(filepath):
    """通过正则匹配文本中内容，并返回文本."""

    flag = False
    contentre = re.compile(regcontent)
    fp = open(filepath, 'r+') # 读写文件
    lines = fp.readlines() # 文件操作
    flines = len(lines)
    #逐行匹配数据.
    for i in range(flines):
        iscontent = re.findall(contentre, lines[i]) # 正则匹配
        # print(iscontent)
        if iscontent != []:
            fp.close()
            return filepath

if __name__ == "__main__":
    try:
        # assert sys.argv[1] == None
        # getdirlist(sys.argv[1], sys.argv[2])
        getdirlist("/Path/XXX/", "password")
    except :
        print("Your enter is null, please re-run the script with dir which you want to search")





