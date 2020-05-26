string=input()
length=int(input())
print((string.count("a"))*(int(length/len(string)))+string[:int(length%len(string))].count("a"))
