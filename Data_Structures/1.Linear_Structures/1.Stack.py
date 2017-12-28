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

if __name__ == "__main__":

    s=Stack()

    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())