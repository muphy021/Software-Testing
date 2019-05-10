import os
import sys

print("current work dir 1 : " + os.getcwd())

mac_join_path = os.path.join("/", "root", "perl5")
print(mac_join_path)

os.chdir(mac_join_path)
print("current work dir 2 : " + os.getcwd())

os.makedirs("/test/makedirs")

'''
区分windows和linux、mac os上的斜杠
1. windows上使用的是倒斜杠\
2. linux、Mac OS上上使用的是正斜杠/
3. 可通过 Z 来记忆哪种是正斜杠
'''



search_path = sys.argv[1]
for current_dir, sub_dir, files in os.walk(search_path):
    if files == []:
        continue
    else:
        for filename in files:
            full_file = os.path.join(current_dir, filename)
            print (full_file)



