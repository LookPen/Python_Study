#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : heap.py
# @Author: Pen
# @Date  : 9/19/17 11:00 AM
# @Desc  : heapq  模块

import heapq


def push_pop_replace():
    nums = [2, 1, 4, 6, 3]

    heapq.heapify(nums)
    print(heapq.heappushpop(nums, 0))  # 0 将0 push 后 堆中最小的是0  所以弹出的还是0

    print(heapq.heapreplace(nums, 0))  # 1 push前堆中最小值为1 所以先将1 弹出 再将0 push


def merge():
    nums1 = [2, 3, 6, 7, 0]
    nums2 = [2, 1, 4, 6, 8]
    heapq.heapify(nums1)
    heapq.heapify(nums2)
    merge = heapq.merge(nums1, nums2)
    first, *_ = merge
    print(first)


def test():
    import heapq

    nums = [1, 2, 8, 4, 2, 6, 7, -1]

    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    nums = [{'name': 'Pen', 'age': '17'}, {'name': 'Pn', 'age': '17'}, {'name': 'en', 'age': '19'}]
    print(heapq.nlargest(2, nums, key=lambda s: s['age'] + s['name']))
    print(heapq.nsmallest(2, nums, key=lambda s: s['age'] + s['name']))


class Priority:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


if __name__ == '__main__':
    # push_pop_replace()
    # merge()
    # test()

    q = Priority()
    q.push('zoo', 1)
    q.push('bar', 5)
    q.push('spam', 4)
    q.push('grok', 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())