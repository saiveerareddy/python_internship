def binarySearch(arr, low,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            left=mid+1
        else:
            right=mid-1
    return -1
numbers=[3,5,7,3,2,7]
target_number=2
print(binarySearch(numbers,0,target_number))
index=(binarySearch(numbers,0,target_number))

print(f"target number {target_number} is found at {index} index ")
