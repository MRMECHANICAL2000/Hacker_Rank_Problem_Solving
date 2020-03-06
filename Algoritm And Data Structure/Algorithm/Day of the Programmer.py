year=int(input())
if year==1918:
    summ=46
elif (year%4==0):
    summ=60
    if year%100==0 and year>1918 and year%400!=0:
        summ=59
else:
    summ=59
for i in range(3,12):
    if i%2==0 and summ<256:
        summ=summ+30
    elif summ<256:
        summ=summ+31
    else:
        if i%2==0:
            summ=30-(summ-256)
        else:
            summ=31-(summ-256)
        break
    #print(summ)
print("{}.{}.{}".format(summ,str(i-1).rjust(2,"0"),year))