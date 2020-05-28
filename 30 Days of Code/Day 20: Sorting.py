n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap=0
for i in range(len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            swap+=1
            a[j+1],a[j]=a[j],a[j+1]
# Write Your Code Here
print("Array is sorted in %s swaps."%swap)
print("First Element: %s"%a[0])
print("Last Element: %s"%a[-1])
