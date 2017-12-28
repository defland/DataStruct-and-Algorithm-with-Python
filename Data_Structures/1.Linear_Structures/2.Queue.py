# coding:utf-8
# Queue.py
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # 为空
        return self.items == []

    def enqueue(self, item): # 顶部新增
        self.items.insert(0,item)

    def dequeue(self): # 顶部删除
        return self.items.pop()

    def size(self):
        return len(self.items) # 大小，高度
    def show(self):
        print(self.items)


# 约瑟夫问题的处理

def josephus(arr=[],k=1):
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
            print('turn %s ' % x )
            q.enqueue(x) # 把头部的人放入尾部
        print('this turn end ')
        print('del %s' % q.dequeue()) # 头部玩家角色取出死亡，queue剩下玩家继续循环
        q.show()

    print(q.size())
    return q.dequeue # 这是最后一名玩家


if __name__ == "__main__":

    # s=Queue()
    # print(s.isEmpty())
    # s.enqueue(9)
    # s.enqueue(10100)
    # print(s.size())
    # print s.dequeue()
    # print s.dequeue()
    # print(s.isEmpty())
    
    print josephus(['test','skdas','dfadfe','yangg','jielun','adfeaja'],5)