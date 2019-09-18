#!/usr/bin/env python3

varlist = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

#Mean
mean = (sum(varlist)/len(varlist))
print("Mean is " + str(mean))

#Median 
x = len(varlist)
varlist.sort()
if x % 2 == 0:
            median = ((varlist[x//2] + varlist[x//2 -1]) /2)
else:
            median = varlist[x//2]

print("Median is " + str(int(median)))

#Mode




