#!/usr/bin/env python3

varlist = [1,2,3,['tom','dick','harry', [7,8,9]],4,5,6,['jean','susan','linda']]
def show():
    for i in varlist:
        if type(i) == list:
            for j in i:
                if type(j) == list:
                        for k in j:
                            print(k)
                else:
                    print(j)
        else:
             print(i)

show()





