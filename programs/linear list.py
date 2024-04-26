l = list(map(int, input("Enter numbers separated by spaces: ").split()))
key = int(input("Enter a number to search: "))

for i in range(len(l)):
    if key == l[i]:
        print(f"The key {key} is found at index {i} in the list.")
        break
else:
    print(f"The key {key} is not in the list.")
