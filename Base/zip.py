# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zip.py
# @Author: Pen
# @Date  : 9/19/17 2:17 PM
# @Desc  :


def zip_dict():
    d = {'a': 1, 'b': 1, 'c': 2, 'd': 0}

    print(sorted(zip(d.values(), d.keys())))


if __name__ == '__main__':
    zip_dict()