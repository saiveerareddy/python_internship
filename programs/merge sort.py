def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_arr=arr[:mid]
    r_arr=arr[mid:]
    l_arr=mergeSort(l_arr)
    r_arr=mergeSort(r_arr)
    return l_arr+r_arr
def merge(mergeSort,l_arr,r_arr):
    new=[]
    i,j=0,0
    while i<len(l_arr) and j<len(r_arr):
        if l_arr[i]<=r_arr[j]:
            new.append(l_arr[i])
            i=i+1
        else:
            new.append(r_arr[j])
            j=j+1
    new.extend[i:]
    new.extend[j:]
    return new



arr=list(map(int,input().split()))

