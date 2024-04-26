def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
numbers=[8,7,6,5,4,3,2,1]
print("the original list:",numbers)
bubble_sort(numbers)
print("the sorted list:",numbers)