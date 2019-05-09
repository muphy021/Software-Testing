# -*- encoding: utf-8 -*-

import re

# 分组( )

identify_group = re.compile(r'(\d{2,4}-)?(\d{11})')
identify_chn = identify_group.search('86-18343132123, 18332123211, 028-23123212, 085-12345413431')
print(identify_chn.group())

identify_all = identify_group.findall('86-18343132123, 18332123211, 028-23123212, 085-12345413431')
for phone_code in identify_all:
    print(phone_code)

# 管道 |
# 它的功能类似于程序中的"或"，只要有一个为true就返回

identify_grep = re.compile(r'Murphy(021|027)')
identify_021 = identify_grep.search("My nick name is Murphy021")
identify_027 = identify_grep.search(" and the other is Murphy027")
print(identify_021.group())
print(identify_027.group())


# 问号 ？
# 相当于是否存在，可以是<=1

identify_question_mark = re.compile(r'This is (my )?car.')
identify_include = identify_question_mark.search("This is my car.")
identify_exclude = identify_question_mark.search("This is car.")

print(identify_include.group())
print(identify_exclude.group())



# 星号 *
# 相当于出现>=0次

identify_star = re.compile(r"This is (your )*telephone")
identify_no = identify_star.search("This is telephone")
identify_1 = identify_star.search("This is your telephone")
identify_2 = identify_star.search("This is your your telephone")
print(identify_no.group(), identify_1.group(), identify_2.group())


# 加号 +
# 至少出现一次，相当于+1，>=1次

re_plus = re.compile(r'Bat(wo)+man')
plus1 = re_plus.search("You are Batwoman.")
print(plus1.group())
plus2 = re_plus.search("You are Batman, but I am Batwowoman")
print(plus2.group())





# 字符分类
'''
\d 0到9的任何数字
\D 除0到9以外的任何字符
\w 任何字母、数字或者下划线字符（可以认为是匹配"单词"字符）
\W 除字母、数字和下划线以外的任何字符
\s 空格、制表符或换行符（可以认为匹配空白字符）
\S 除空格、制表符和换行符以外的任何字符
'''
str_classify = re.compile(r'\d+\s\w+')
xmasReg = str_classify.findall('12 drummers, 11 pipers, 10 lords')
for str_name in xmasReg:
    print (str_name)


# 可以使用[ ]来定义自己的字符分类
# ^表示取非[ ]指定的字符
# -表示取值范围


# 插入字符^和美元字符$ 表示以XX开始，以YY结束
# 例如， ^\d+$表示匹配从开始到结束都必须是数字

wholeStringisNum = re.compile(r'^\d+$')
check_wholeStringisNum = wholeStringisNum.search("98734")

if (check_wholeStringisNum == None):
    print("Your entry is not the whole number.")
else:
    print("Your entry is " + check_wholeStringisNum.group())

# .表示通配符，它匹配除了换行之外的所有字符
atReg = re.compile(r"\w+.ese")
check_atReg = atReg.findall("I like Chinese. Do you like Chinese or Japanese? I know you would like to learn Engliese")
for atReg_name in check_atReg:
    print(atReg_name)


# compile中可以跟re.I来忽略大小写，可以用sub来替换指定的字符串
# re.VERBOSE可以忽略正则表达式字符串中的空白符和注释


# * 匹配所有字符
starReg = re.compile(r"A\s|A\w+?\s+?")
searchStar = starReg.findall("A is the first letter of Alpha table. Please check if it is the correct Apple .")
for match_star in searchStar:
    print(match_star)

