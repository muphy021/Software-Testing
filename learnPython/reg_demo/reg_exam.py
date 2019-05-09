# !/usr/bin/ python
# -*- encoding: utf-8 -*-

import re

'''
在文章中找出所有符合格式的电话号码和电子邮件地址


1. 先考虑框架
    从剪贴板获取文本；
    从中找出所有电话号码和E-mail地址；
    将结果粘贴到剪贴板；

2. 使用pyperclip模块复制和粘贴字符串。
3. 创建两个正则表达式，一个匹配电话号码，一个匹配email。
4. 要找到所有匹配，而不是第一次匹配。
5. 将匹配的字符串整理好格式，放在一个字符串中，用于粘贴。
6. 如果没有找到匹配，显示某种信息。

'''

phone_reg = re.compile(r'''
    \(?     # national code
    \+?
    \d{,4}
    \)?
    \-?
    \(?     # city code
    \+?
    \d{,4}
    \)?
    \-?
    \d{8,11} # telephone or mobile phone

''', re.VERBOSE)

test_phone_reg = phone_reg.findall(
    "Your phone number is (+86)-(028)-76313123 or +86-028-19247432 or +86-18732123123 or just 18712312312 or 028-12343412")
for number in test_phone_reg:
    print(number)

email_reg = re.compile(r'''
    (
    [a-zA-Z0-9._%+-]+ #username
    @ 
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4})
    )
''', re.VERBOSE)

test_email_reg = email_reg.findall(
    "This is my email: murphy-021@qq.com. I will confirm with your email: microsoft_098@outlook.com")

for mail in test_email_reg:
    print(mail)

# 匹配分组
groups_reg = re.compile(r'(\d{2})-(\d{3}-\d{4})')
test_groups_reg = groups_reg.search("The number is 86-123-4567")
print(test_groups_reg.group(0))
print(test_groups_reg.group(1))
print(test_groups_reg.group(2))

# 匹配开始字符和结束字符
number_match = re.compile(r'^\d{1,3}(,\d{3})*$')
test_number_match = number_match.search("12,123,123")

print(test_number_match.group())

#
match_names = re.compile(r"(([A-Z]+[a-zA-Z]*)+\sNakamo)")
test_match_names = match_names.findall(
    "Satoshi Nakamo, Alice Nakamo, RoboCop Nakamo, Mr. Nakamo, Nakamo, Satoshi nakamo, soku Nakamo")

for correct_name in test_match_names:
    print(correct_name)

# (Alice|Bob|Carol\seats|pets|throws\sapples|cats|baseballs$\.)
match_combine = re.compile(r"(Alice|Bob|Carol) (pets|eats|throws) (cats|apples|baseballs).", re.I)

sen_1 = "Alice eats apples."
sen_2 = "Bob pets cats."
sen_3 = "BOB EATS CATS."

sen_4 = "RoboCop eats apples."
sen_5 = "Carol eats 7 cats."
sen_6 = "Carol throws baseballs."

test_match_combine = match_combine.search(sen_3)
print(test_match_combine.group())

# 强口令
# 长度不少于8个字符，同时包含大小写，至少一位数字
# https://www.cnblogs.com/cexm/p/7737538.html
# https://www.html.cn/archives/8100


match_login = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,}')

test_match_login = match_login.search("A8D12dlfskasdfk阿道夫3tT")
if test_match_login == None:
    print("你输入的口令未达到要求")
else:
    print("输入口令成功:" + test_match_login.group())

# https://docs.python.org/3/library/re.html