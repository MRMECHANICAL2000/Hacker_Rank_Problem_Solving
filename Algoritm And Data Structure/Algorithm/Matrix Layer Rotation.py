m,n,r=[int(i) for i in input().split()]
matrix=[]
for i in range(m):
    matrix.append(list(map(str,input().split())))

x=int(m/2)
y=int(n/2)

for a in range(0,x):
    for b in range(a,y):

        for _ in range(0,r%((m+n-2-(2*a+2*b))*2)):
            

            temp=matrix[a][b]    
            for i in range(a,n-b):
                for j in range(a+1,m-b):
                    matrix[j][i],temp=temp,matrix[j][i]

                break

            for i in range(m-b-1,a-1,-1):
                for j in range(a+1,n-b):
                    matrix[i][j],temp=temp,matrix[i][j]

                break
            for i in range(n-b-1,a-1,-1):
                for j in range(m-b-2,a-1,-1):
                    matrix[j][i],temp=temp,matrix[j][i]

                break
            for i in range(a,m-b):
                for j in range(n-b-2,a-1,-1):
                    matrix[i][j],temp=temp,matrix[i][j]

                break

        break
[print(" ".join(i)) for i in matrix]

            
    
    
    
