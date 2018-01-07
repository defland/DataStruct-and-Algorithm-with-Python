#coding:utf-8

# 从大到小排序的选择排序例子,另外一种实现方法。


def selection_sort(original_arr=[]):
    # 选择排序

    for i in range(0,len(original_arr)-1):
        max_index = i # 把本次循环的头个作为最大
        for j in range(i+1,len(original_arr)):
            if original_arr[max_index] < original_arr[j]:
                max_index = j
        original_arr[i],original_arr[max_index] = original_arr[max_index],original_arr[i]
    return original_arr


if __name__=="__main__":

    original_arr = [94,32,13323,543,322,1,3232,43,0,1212]
    print original_arr
    print selection_sort(original_arr)
    
    """ output
        [94, 32, 13323, 543, 322, 1, 3232, 43, 0, 1212]
        [13323, 3232, 1212, 543, 322, 94, 43, 32, 1, 0]
    """