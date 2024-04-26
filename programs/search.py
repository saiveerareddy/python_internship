def search(self,key):
    current=self.head
    count=0
    while current:
        count=count+1
        if current.data==key:
            print("data found at position",count)
            count=-1
            break
        current=current.next
    if count!=0:
        print("data not found")