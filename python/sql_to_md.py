# coding=utf-8

'''
  sql 文件生成 md 表格
'''

import sys
import re

args = sys.argv

print(args)

if len(args) == 0:
    print("请指定sql文件地址")

sql_file = open(str(args[1]), mode='r', encoding='utf-8')

re1 = re.compile("\`(.*)\`")
re2 = re.compile("\'(.*)\'\,")

index = 0
for line in sql_file:
    if index == 0:
        print("表：%s" % re1.search(line).group(0))
    else:
        comment = re2.search(line)
        commentStr = ''
        if comment:
            commentStr = comment.group(0)
        print("%s|%s" % (re1.search(line).group(0), commentStr))
    index = index+1
