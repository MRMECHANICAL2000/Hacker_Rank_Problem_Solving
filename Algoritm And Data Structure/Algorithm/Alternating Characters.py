# using list comprehension
def alternating_string(x):
    print(sum([1 for i in range(len(x)-1,0,-1) if x[i]==x[i-1]]))
            
if __name__ == '__main__':
    for _ in range(int(input())):
        x=input()
        alternating_string(x)
#using loop
def alternating_string(x):
    remove=0
    for i in range(len(x)-1,0,-1):
        if x[i]==x[i-1]:
            remove+=1
    print(remove)

if __name__ == '__main__':
    for _ in range(int(input())):
        x=input()
        alternating_string(x)
