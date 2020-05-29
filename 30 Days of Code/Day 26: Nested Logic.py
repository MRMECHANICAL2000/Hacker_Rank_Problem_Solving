fine=0
gd=[int(i) for i in input().split()]
dl=[int(i) for i in input().split()]
if gd[2]>dl[2]:
    fine+=10000
elif gd[1]>dl[1] and gd[2]==dl[2]:
    fine+=500*(gd[1]-dl[1])
elif gd[0]>dl[0] and gd[1]==dl[1] and gd[2]==dl[2]:
    fine+=15*(gd[0]-dl[0])
print(fine)
