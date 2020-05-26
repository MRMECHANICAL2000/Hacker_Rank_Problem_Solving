hour=int(input())
minutes=int(input())
words=["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",  
            "seventeen", "eighteen", "nineteen",  
            "twenty", "twenty one", "twenty two",  
            "twenty three", "twenty four",  
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine","thirty"]
if minutes>30:
    hour+=1
    minutes=60-minutes
    if minutes==0:
        print("{} o' clock".format(words[hour-1]))
    elif minutes<10:
        print("{} minutes to {}".format(words[minutes],words[hour]))
    elif minutes<15:
        print("{} minutes to {}".format(words[minutes],words[hour]))
    elif minutes==15:
        print("quarter to {}".format(words[hour]))
    elif minutes<30:
        print("{} minutes to {}".format(words[minutes],words[hour]))

else:
    if minutes==0:
        print("{} o' clock".format(words[hour]))
    elif minutes<10:
        print("{} minute past {}".format(words[minutes],words[hour]))
    elif minutes<15:
        print("{} minutes past {}".format(words[minutes],words[hour]))
    elif minutes==15:
        print("quarter past {}".format(words[hour]))
    elif minutes<30:
        print("{} minutes past {}".format(words[minutes],words[hour]))
    elif minutes==30:
        print("half past {}".format(words[hour]))
