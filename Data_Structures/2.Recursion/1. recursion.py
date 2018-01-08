# coding:utf-8

# 用递归替代for循环


# for
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


# recursion递归
def listsum_recursion(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum_recursion(numList[1:])


if __name__ == "__main__":

    print(listsum([2, 3, 4331, 322, 12]))
    print(listsum_recursion([2, 3, 4331, 322, 12]))
