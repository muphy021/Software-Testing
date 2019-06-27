# -*- encoding: utf-8 -*-
import random
print(dir(list)) #列出list可用的方法
print(dir(tuple))

# 使用字典
test_dic={}
test_dic["Math"]=100
test_dic["English"]=99

print(test_dic)
print(test_dic["English"])


if "Math" in test_dic:
    print("The score of Math is " + str(test_dic["Math"]))
else:
    print("There is no math.")
print(dir(dict))


dic_items = list(test_dic.items()) #获取所有的key-values对
print(dic_items)

# practice
first_case = tuple()
first_case = input("please enter some strings: ")

print(first_case)
inc_tuple = first_case*3
print(inc_tuple)

case2 = [1, 2, 4, 5, 7, 8, 9]
case2_copy = case2[3:5]
print(case2_copy+case2)

case3=input("enter one integer: ")
print(random.sample(range(1, 100), int(case3)))


# 控制流程