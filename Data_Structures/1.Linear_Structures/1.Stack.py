# coding:utf-8
# Stack.py
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # 为空
        return self.items == []

    def push(self, item): # 顶部新增
        self.items.append(item)

    def pop(self): # 顶部删除
        return self.items.pop()

    def peek(self): # 查询顶部元素的值
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items) # 大小，高度

# 用来做括号匹配的测试
def symmetry(str):
    s = Stack()
    balance_flag = True
    for character in str:
        if character == '{':
            # 左{放入stack
            s.push(character)
        else:
            if s.isEmpty(): # 例如{{}}}},渠道
                balance_flag = False
                break
            # 右} 开始判断,遇到1个就弹出
            if character == "}":
                s.pop()
    if balance_flag == True and s.isEmpty():
        return True
    else:
        return False



if __name__ == "__main__":

    # s=Stack()

    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size())
    # print(s.isEmpty())
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())

    print symmetry("{{{}}")