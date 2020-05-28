#using splitting
if __name__ == '__main__':
    n = int(input())
    m=(str(bin(n))[2:]).split("0")
    print(len(max(m)))

#Using Iteration
"""
if __name__ == '__main__':
    n = int(input())
    m=str(bin(n))[2:]
    maxcount=0
    for i in range(len(m)):
        if m[i]=="1":
            count=1
            for j in range(i+1,len(m)):
                if m[j]=="1":
                    count+=1
                    continue
                break
            if count>maxcount:
                maxcount=count
    print(maxcount)
"""
