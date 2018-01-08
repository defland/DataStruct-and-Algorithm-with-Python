# coding:utf-8
# Deque.py

# 用列表来实现一个list结构


class Node:

    def __init__(self, initdata):

        self.data = initdata  # 链表节点的数据
        self.next = None  # 链表节点的下一个地址

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext



