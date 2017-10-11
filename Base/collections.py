#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : collections.py
# @Author: Pen
# @Date  : 9/19/17 1:57 PM
# @Desc  : collections 模块的使用(默认值字典/有序字典/计数器/命名元组/多字典映射)


from collections import defaultdict, OrderedDict, Counter, namedtuple, ChainMap


def default_dict():
    """
    自动实例化 value 对应的对象
    :return:
    """
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(1)

    print(d)

    d = dict()
    d.setdefault('a', []).append(1)

    print(d)


def ordered_dict():
    """
    有序的字典
    :return:
    """
    d = OrderedDict()
    d['ssa'] = 1
    d['asdf'] = 3
    d['ass'] = 4
    d['aaa'] = 5

    print([i for i in d])


def counter():
    """
    计数器
    :return:
    """
    d = ['a', 'a', 'c', 'c', 'c', 'b']
    count = Counter(d)
    print(count.most_common(2))


def named_tuple():
    """
    命名的元组
    :return:
    """
    Person = namedtuple('Person', ['name', 'age', 'sex'])

    pen = Person('pen', 18, 1)

    print(pen)
    print(pen.age)


def chain_map():
    """
    以便把所有映射对象当作一个对象单元来处理
    :return:
    """
    a = {'a': 1, 'b': 2}
    c = {'c': 1, 'd': 2}

    d = ChainMap(a, c)

    print(d.maps)
    print(list(d.keys()))
    print(list(d.values()))
    print(d['c'])

    # 使用new_child添加新字典
    dict3 = {'f': 5}
    new_chain = d.new_child(dict3)


if __name__ == '__main__':
    default_dict()
    ordered_dict()
    counter()
    named_tuple()
    chain_map()
