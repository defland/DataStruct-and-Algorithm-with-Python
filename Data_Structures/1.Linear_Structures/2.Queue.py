# coding:utf-8
# Queue.py

import threading
import time


class Queue:
    def __init__(self, maxsize=100):
        self.items = []
        self.maxsize = maxsize

    def isEmpty(self):  # 为空
        return self.items == []

    def enqueue(self, item):  # 顶部新增
        self.items.insert(0, item)

    def dequeue(self):  # 顶部删除
        return self.items.pop()

    def size(self):
        return len(self.items)  # 大小，高度

    def show(self):
        print(self.items)
        return True

    def get_maxsize(self):  # 获取队列最大长度
        return self.maxsize


# 约瑟夫问题的处理

def josephus(arr=[], k=1):
    q = Queue()
    # 放入queue
    for name in arr:
        q.enqueue(name)
        q.show()

    # 开始循环，直到queue只剩一个人
    while q.size() > 1:
        # 轮转k次
        for i in range(k):
            x = q.dequeue()
            print('turn %s ' % x)
            q.enqueue(x)  # 把头部的人放入尾部
        print('this turn end ')
        print('del %s' % q.dequeue())  # 头部玩家角色取出死亡，queue剩下玩家继续循环
        q.show()

    print(q.size())
    return q.dequeue  # 这是最后一名玩家
#
# 生产者/消费者模型
#


q = Queue()


def producer(name):  # 生产者
    count = 1
    while True:
        q.enqueue("model number:%s" % count)
        print("[%s] make new phone : %s " % (name, count))
        count += 1
        time.sleep(0.2)
        if q.size() == q.get_maxsize():  # 生产者放入速度快，队列满了
            print('queue is full ,waiting...')
            time.sleep(1)


def consumer(name):  # 消费者
    while True:
        if q.isEmpty():  # 消费者取出速度快，队列空了
            print('queue is empty ,waiting...')
            time.sleep(3)
        print("[%s] buy new phone number [%s]..." % (name, q.dequeue()))
        time.sleep(1)


def start_model():
    producerx = threading.Thread(target=producer, args=('producerX',))
    c1 = threading.Thread(target=consumer, args=('c1',))
    c2 = threading.Thread(target=consumer, args=('c2',))

    producerx.start()
    c1.start()
    c2.start()


if __name__ == "__main__":

    # 测试 queue对象和方法
    # s=Queue()
    # print(s.isEmpty())
    # s.enqueue(9)
    # s.enqueue(10100)
    # print(s.size())
    # print s.dequeue()
    # print s.dequeue()
    # print(s.isEmpty())

    # 测试约瑟夫问题
    # print josephus(['test','skdas','dfadfe','yangg','jielun','adfeaja'],5)

    # 生产者和消费者模型
    start_model()
