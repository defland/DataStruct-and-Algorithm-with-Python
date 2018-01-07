# coding:utf-8
# Deque.py


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # 为空
        return self.items == []

    def size(self):
        return len(self.items)  # 大小，高度

    def addFront(self, item):
        self.items.append(item)
        return True

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def show(self):
        print(self.items)

# 用来做括号匹配的测试


def symmetry(stri):
    # 放入str到deque中
    # 取出头尾判断是否对应
    # 直到deque最后为空
    d = Deque()
    for character in stri:
        d.addFront(character)
    d.show()

    balance_flag = True
    while balance_flag:
        # 开始判断
        if d.size() == 1:
            balance_flag = False
            break
        frist = d.removeFront()
        last = d.removeRear()
        if frist != '}' or last != '{':
            balance_flag = False
    return balance_flag


if __name__ == "__main__":

    # d = Deque()

    # d.addFront(100)
    # d.addFront('abc')

    # d.show()

    # d.addRear(300)
    # d.addRear("test")

    # d.show()

    # d.removeFront()
    # d.removeRear()
    # d.show()

    print(symmetry('{{}}}'))
