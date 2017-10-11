# # 三目
# flag = 1
# num = 1 if flag else 0
#
# # set
# persons1 = set()
# persons1.add(1)
# persons1.add('zp')
#
# persons2 = set()
# persons2.add(1)
#
# xx = persons1.difference(persons2)
#
# # copy
#
# import copy
#
# a = {'name': 1}
# b = copy.deepcopy(a)
#
# a['name'] = 2
#
#
# def func(*args, **kwargs):
#     print(args, kwargs)
#
#
# class A(object):
#     def __init__(self):
#         self.xx = 0
#
#
# def convert_to_dic(obj):
#     d = {}
#     d.update(obj.__dict__)
#     return d
#
#
# a = A()
# a.xx = 12
#
# setattr(a, 'age', 1)
#
# import json
# from functools import reduce
#
#
# def xx(x):
#     return str(x) + ','
#
#
# def yy(x, y):
#     return x + y
#
#
# re = reduce(yy, [1, 2, 3, 4, 5, 6])
# print(re)

# re = filter(lambda x: x > 20, [1, 2, 4, 10, 32])
# print(list(re))

#
# class A(object):
#     pass
#
#
# a = A()
# a.name = 1
#
# print(a.name)

# datas = [1, 2, 3, 4, 5, 6, 7, 8]
#
# a, *b, c = datas
# print(b)

# datas = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# a, *b, c = datas
# print(b)

# datas = [
#     ('a', 1, 2, 3, 4, 5),
#     ('b', 3, 4, 5),
#     ('d', 6, 7, 8)
# ]
#
# for tag, *data in datas:
#     print(tag, data)


# def func(a, b, fun):
#     return fun(a) + fun(b)
#
#
# fun = abs
# print(func(1, 2, fun))
#
#
# def func(*args):
#     def sum():
#         ax = 0
#         for i in args:
#             ax += i
#         return ax
#
#     return sum
#
#
# print(
#     func(*[1, 2, 3])()
# )

# data = [1, 2, 3, 4, 5]
#
# re = filter(lambda x: x % 2 == 0, data)
# print(type(re))
# print(list(re))
# print(data)


# data = [1, 4, -5, 3, 2]
# re = sorted(data)
# print(re)
#
# re = sorted(data, key=abs)
# print(re)
#
# print(data)


# def sum_lazy(*args):
#     def my_sum():
#         re = 0
#         for i in args:
#             re += i
#         return re
#
#     return my_sum
#
#
# data = [1, 2, 3]
# func = sum_lazy(*data)
# re = func()
# print(re)

#
# def log(func):
#     def wrapper(a, b):
#         print('call this func')
#         func(a, b)
#
#     return wrapper
#
#
# def log(text):
#     def decorator(func):
#         def wrapper(a, b):
#             print('call this func ' + text)
#             func(a, b)
#
#         return wrapper
#
#     return decorator
#
#
# @log
# def sum_data(a, b):
#     print(a + b)
#
#
# @log('xx')
# def sum_data(a, b):
#     print(a + b)
#
#
# sum_data(1, 2)
#
# class Person(object):
#     def __init__(self):
#         self._name = 'person'
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#
# person = Person()
# person.name = 'xp'
# print(person.name)


# from  enum import Enum
#
# Month = Enum('星期', ('星期一', '星期二'))
#
# print(Month.星期一, Month.星期一.name, Month.星期一.value)
#
#
# class MyWeekDay(Enum):
#     星期一 = 0
#     星期二 = 1
#
#
# print(MyWeekDay.星期一, MyWeekDay.星期一.name, MyWeekDay.星期一.value)

# from types import MethodType
#
#
# class Person(object):
#     __slots__ = ('name', 'age')
#     pass
#
#
# person = Person()
#
#
# def show_name(self):
#     print(self.name)
#
#
# person.name = 'Pen'  # 动态的绑定属性
# person.show_name = MethodType(show_name, person)  # 动态的绑定方法
#
# print(person.name)
# person.show_name()


# class MyData(object):
#     def __init__(self, num):
#         self.a = 0
#         self.num = num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.a < self.num:
#             self.a += 1
#             return self.a
#         else:
#             raise StopIteration()
#
#     def __getitem__(self, item):
#         tmp = 0
#         if item <= self.num:
#             for r in range(item):
#                 tmp += 1
#             return tmp
#         else:
#             raise KeyError
#
#
# data = MyData(10)
#
# for i in data:
#     print(i)
#
# print(data[1])

#
# def show_name(self, name):
#     print(name)
#
#
# Person = type('Person', (object,), {'show_name': show_name})
#
# person = Person()
# person.show_name('Pen')


# from io import StringIO
#
# string_io = StringIO()
# string_io.write('hello')
# re = string_io.getvalue()  # write 进去后只能通过getvalue 来获取值
#
# string_io = StringIO('word')
# re = string_io.read()  # 初始化的通过read 获取值
#
# print(re)
#
# import os
#
# print('Process {0} start'.format(os.getpid()))
# pid = os.fork()
#
# if pid == 0:
#     print('I am Child Process:{0} My Parent is {1}'.format(os.getpid(), os.getppid()))
# else:
#     print('I am Parent Process:{0} My Child is {1}'.format(os.getpid(), pid))
#
#
# from multiprocessing import Process
# import os
#
#
# def run_proc(name):
#     print('I am Child{2} Process:{0} My Parent is {1}'.format(os.getpid(), os.getppid(), name))
#
#
# print('I am Parent Process:{0} '.format(os.getpid()))
# p = Process(target=run_proc, args=('test',))
# print('Child process will start.')
# p.start()
# p.join()
# print('Child process end.')


# from multiprocessing import Pool
# import os, time, random


# def long_time_task(name):
#     print('{0} run :{1}'.format(os.getpid(), name))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#
#     print('{0} run :{1} s'.format(os.getpid(), str(end - start)))
#
#
# print('I am Parent Process:{0} '.format(os.getpid()))
#
# p = Pool(4)
# for i in range(10):
#     p.apply_async(long_time_task, args=(i,))
# print('waiting')
# p.close()
# p.join()
# print('done')

# from multiprocessing import Process, Queue
# import os, time, random
#
#
# def write(data):
#     print('{0} write '.format(os.getpid()))
#     for value in ['a', 'b', 'c']:
#         data.put(value)
#         time.sleep(random.random())
#
#
# def read(data):
#     print('{0} read '.format(os.getpid()))
#     while True:
#         print(data.get(True))
#
#
# data = Queue()
# w = Process(target=write, name='write', args=(data,))
# r = Process(target=read, name='read', args=(data,))
#
# w.start()
# r.start()
#
# w.join()  # 等待结束
# r.terminate()  # 因为是死循环 所以强制结束


# import threading
# import random
#
# re = 0
# lock = threading.Lock()
#
#
# def long_time_task():
#     global re
#     print('{} thread running'.format(threading.current_thread().name))
#     for i in range(1000000):
#         ran = random.random()
#
#         lock.acquire()
#         re += ran
#         re -= ran
#         lock.release()
#
#
# print('{} main running'.format(threading.current_thread().name))
# t1 = threading.Thread(target=long_time_task)
# t2 = threading.Thread(target=long_time_task)
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print('Done {0}'.format(re))

# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
#
#     data = b''.join(buffer)
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))

# record = ('Pen', 18, 182, (1992, 11, 9))
#
# name, *_, (year, *_) = record
#
# print(name, year)


# from collections import deque
#
#
# def search(lines, pattern, history=2):
#     previous_lines = deque(maxlen=history)
#
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
#
#
# if __name__ == '__main__':
#     record = ['马孔多在下雨', '八月份下雨很正常啊', '苦寒之地']
#
#     for line, previous_lines in search(record, '下雨'):
#         print(line, previous_lines)

# from collections import deque
#
# previous_lines = deque()
#
# import heapq
#
# nums = [1, 2, 8, 4, 2, 6, 7, -1]
#
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))
#
# nums = [{'name': 'Pen', 'age': '18'}, {'name': 'Pn', 'age': '17'}, {'name': 'en', 'age': '19'}]
# print(heapq.nlargest(1, nums, key=lambda s: s['age']))
# print(heapq.nsmallest(1, nums, key=lambda s: s['age']))
#
# nums = [1, 2, 8, 4, 2, 6, 7, -1]
# heapq.heapify(nums)
# print(nums)
#
# print(min(nums))
# print(max(nums))


# a = {'name': {'zp', 'zp', 'Pen'}}
# b = {'name': ['zp', 'zp', 'Pen']}
#
# print(a)
# print(b)


# a = {
#     'x': 1,
#     'y': 2,
#     'z': 3
# }
#
# b = {
#     'y': 1,
#     'z': 2,
#     'w': 3
# }
#
# # 相同的键
# same_keys = a.keys() & b.keys()
# print(same_keys)
#
# # a中有的 b 中没有的键
# diff_keys = a.keys() - b.keys()
# print(diff_keys)

from operator import itemgetter
from itertools import groupby

d = [
    {
        'name': 'pen',
        'age': 18
    },
    {
        'name': 'en',
        'age': 18
    },
    {
        'name': 'n',
        'age': 17
    },

]

print(sorted(d, key=itemgetter('age', 'name')))  # 先age排序 再按 name排序

for i, items in groupby(d, key=itemgetter('age')):
    print('age:{0}'.format(i))
    for item in items:
        print(item)