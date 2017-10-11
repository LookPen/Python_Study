#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : str.py
# @Author: Pen
# @Date  : 9/20/17 10:03 AM
# @Desc  : 字符串相关处理


# import re
#
# line = 'zp, Pen;;;; zhou!   Jianli'
#
# # names = re.split(r'[,;!\s]*\s*', line)
# # print(names)  # ['zp', 'Pen', 'zhou', 'Jianli']
#
#
# print(line.startswith('zp'))
#
# print(line.startswith(('zp', 'z', 'p')))


# from fnmatch import fnmatch, fnmatchcase
#
# flag = fnmatch('peen', '*en')
# print(flag)  # True
#
# flag = fnmatch('peen', '?en')
# print(flag)  # Flase
#
# flag = fnmatch('peen123', '*en[0-9]*')
# print(flag)  # True

import re

# str = 'hello my name is Pen'
#
# if re.match(r'hello*', str):
#     print(True)
#
# datepat = re.compile(r'[h,m]')
#
# flags = [True if datepat.match(s) else False for s in str.split(' ')]
#
# print(flags)  # [True, True, False, False, False]

# str = 'hello my name is njk '
#
# matchs = re.match(r'(\sn.*?[\s])', str)
# if matchs:
#     for m in matchs:
#         print(m)

#
# str = 'today is 2017/9/11 other is 2017/10/11'
#
# match = re.match(r'(\d+)/(\d+)/(\d+)', str)
#
# re.sub(r'(\d+)/(\d+)/(\d+)', r'\2-\3-\1', str)
#
# print(str)


# str = 'Pen'

# str = str.ljust(20, '~')
# print(str)

# str = str.rjust(20, '~')
# print(str)

# str1 = format(str, '!>20')
# print(str1)
#
# str2 = format(str, '!<20')
# print(str2)
#
# str3 = format(str, '!^20')
# print(str3)



# str = 'my {name} is {0}'.format(18, name='age')
#
# print(str) #my age is 18

# import html
#
# s = '<p>haha</p>'
# print(s)
#
# print(html.escape(s))

from datetime import datetime

print(datetime.now())
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))