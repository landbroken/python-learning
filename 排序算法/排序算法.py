'''
冒泡排序

重复走访过要排序的序列，一次比较两个元素，如果他们的顺序错误就将他们进行交换，一次冒上来的是最小的，其次是第二小。

时间复杂度：O(n^2)

空间复杂度:O(1)

稳定性：稳定
'''
def BubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
                data[j+1] , data[j] = data[j] , data[j+1]

'''
选择排序

选择排序相比冒泡排序不稳定，时间复杂度也是。选择排序没趟都会产生最小值，它不是相邻元素的比较而是在该元素设置一个索引i。
然后与数组的其他元素依次比较（除了上一个索引值），直到找到小于该元素（索引j）时交换两元素，
接着继续从i索引（此时已经不是原来的数值）值与索引j+1值比较。重复上述比较过程……简单的原理图如下：

冒泡是相邻元素比较，选择不是相邻元素比较
'''
def SelectionSort(data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[j]<data[i]:
                data[i] , data[j] = data[j] , data[i]

'''
快速排序

快速排序流程：
(1) 从数列中挑出一个基准值。
(2) 将所有比基准值小的摆放在基准前面，所有比基准值大的摆在基准的后面(相同的数可以到任一边)；在这个分区退出之后，该基准就处于最终它应该在的地方。
(3) 递归地把"基准值前面的子数列"和"基准值后面的子数列"进行排序。

快速排序的时间复杂度在最坏情况下是O(N2)，平均的时间复杂度是O(N*lgN)。
'''               
def QuickSort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key =left
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= lists[key]:#如果右边比基准小，停下
            right -= 1
        while left < right and lists[left] <= lists[key]:#如果左边比基准大，停下
            left += 1
        lists[right],lists[left]=lists[left],lists[right]#交换现在的左右值
    lists[right] ,lists[key]=lists[key],lists[right] #left和right汇合后和基准交换
    print("QuickSort交换过程")
    print_data(data)#交换过程
    QuickSort(lists, low, left - 1)
    QuickSort(lists, left + 1, high)
    return lists


'''
直接插入排序

1. 初始时，a[0]自成1个有序区，无序区为a[1..n-1]。令i=1
2. 将a[i]并入当前的有序区a[0…i-1]中形成a[0…i]的有序区间。
3. i++并重复第二步直到i==n-1。排序完成。

直接插入排序的时间复杂度是O(N2)。
假设被排序的数列中有N个数。遍历一趟的时间复杂度是O(N)，需要遍历多少次呢？N-1！因此，直接插入排序的时间复杂度是O(N2)。
'''
def InsertionSort(data):
    for i in range(1,len(data)):
        key=data[i]
        j=i-1
        while j>=0:
            if data[j]>key:
                data[j+1]=data[j]
                data[j]=key
            j-=1
'''
希尔排序

是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。分组的插入排序

j-=gap第一次交换数据后，看它是后面的数否还小于前面的数

如2 3 1 5 9 6这个序列以1位步长的话
一次交换后2 1 3 5 9 6此时j指向第二个数，i指向第三个数 
所以交换后应该用j-gap往前查看是否前面的更小
'''

def ShellSort(data):
    gap=int(len(data)/2) #排序的分组
    while gap>0:
        for i in range(gap,len(data)):
            j=i-gap
            while data[j]>data[i] and j >=0:
                data[j],data[i]=data[i],data[j]
                j-=gap
                i-=gap
        gap=int(gap/2)

'''
归并排序

先拆分，后合并
'''
def MergeSort(ls):
    if len(ls)<2:
        return ls
    mid = len(ls) >> 1 #相当于除2取整
    left = MergeSort(ls[:mid])

    right = MergeSort(ls[mid:])
    return merge(left,right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

'''打印函数'''
def print_data(data):
    for i in data:
        print(i,end=' ')
    print() 


'''测试代码'''
#BubbleSort
data=[5,9,7,2,3,1,6]
BubbleSort(data)
print("BubbleSort: ")
print_data(data)
#SelectionSort
data=[5,9,7,2,3,1,6]
SelectionSort(data)
print("SelectionSort: ")
print_data(data)
#QuickSort
print("QuickSort: ")
data=[5,9,7,2,3,1,6]
QuickSort(data,0,len(data)-1)
print_data(data)
#InsertionSort
print("InsertionSort: ")
data=[5,9,7,2,3,1,6]
InsertionSort(data)
print_data(data)
#ShellSort
print("ShellSort: ")
data=[5,9,7,2,3,1,6]
ShellSort(data)
print_data(data)
#MergeSort
data=[5,9,7,2,3,1,6]
data=MergeSort(data)
print("MergeSort: ")
print_data(data)
