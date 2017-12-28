#coding:utf-8

# 从大到小排序的选择排序例子。

def find_max(arr=[]):
    # 每一轮，找出一个最大值的位置并返回
    max_value = arr[0] # 默认最开始的元素为最大
    max_value_index = 0 # 最大值的索引位置
    
    for i in range(1,len(arr)):
        # 从i(1,2,3,4,5,6...下标位置和最大值比，如果更大就赋予最大值和下标) 
        if arr[i] > max_value: 
            max_value = arr[i]
            max_value_index = i 

    return max_value_index

def selection_sort(original_arr=[]):
    # 选择排序
    new_list = []
    for i in range(0,len(original_arr)):
        # 找出最大值，转到新的列表，然后从原始列表删除最大值
        max_value_index = find_max(arr=original_arr)
        new_list.append(original_arr[max_value_index])
        original_arr.pop(max_value_index)
    return new_list
    


if __name__=="__main__":

    original_arr = [94,32,13323,543,322,1,3232,43,0,1212]
    print original_arr
    print selection_sort(original_arr)
    
    """ output
        [94, 32, 13323, 543, 322, 1, 3232, 43, 0, 1212]
        [13323, 3232, 1212, 543, 322, 94, 43, 32, 1, 0]
    """