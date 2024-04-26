l=list(map(int,input("Enter a number: ").split(" ")))
key=int(input("Enter a number: "))
for i in range(len(l)):
    if key == l[i]:
        print(f"the key found in {i}th in list")
if key not in l:
    print(f"the key not in list")
