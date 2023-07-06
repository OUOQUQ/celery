MaryTmp=[]
T = int(input())
for i in range(T):
    InputList=input().split(' ')
    n=int(InputList[0])

    InputLast = 0
    CountMary = 0
    Flag = 1
    for j in range(1, n+1):
        InputFirst = InputLast
        InputLast = int(InputList[j])
        if(Flag == 0):    #flag = 0 -> ">"
            if( InputFirst > InputLast):
                CountMary += 1
                Flag = 1
        else:    #flag = 1 -> "<"
            if( InputFirst < InputLast):
                CountMary += 1
                Flag = 0
    
    MaryTmp.append(CountMary)
for i in range(len(MaryTmp)):
    print(MaryTmp[i])