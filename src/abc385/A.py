a = [int(i) for i in input().split()]
a.sort()

if a[2] == a[0] + a[1] or a[0] == a[2]:
    print("Yes")
else:
    print("No")
