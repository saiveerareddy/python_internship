def insertion(l):
    n=len(l)
    for i in range(1,n):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j=j-1
            l[j+1]=key

l=[50,20,40,60]
insertion(l)
print(l)