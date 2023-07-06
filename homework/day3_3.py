MazeSecond = []
Prouduce = 0
MazeCheck = []
BreakCheck = False
T = int(input())
for i in range(T):
    R, C = input().split(' ')
    print(MazeCheck)
    #---------------------------迷宮產生
    if Prouduce == 0:
        for RL in range(int(R)):
            Maze=[]
            for CL in list(input()):
                #print(RL)
                Maze.append(CL)
            MazeSecond.append(Maze)
    Prouduce = 1
    #---------------------------開始判斷
    # #=3, F=2, J=1, .=0
    while(1):
        for RCheck in range(int(R)):
            Check = [0] * int(C)
            MazeCheck.append(Check)
        for RL in range(int(R)):
            for CL in range(int(C)):
                match MazeSecond[RL][CL]:
                    case 'F':
                        if MazeCheck[RL][CL] == 0: #代表此輪沒改過
                            if (MazeSecond[RL-1][CL] == '.'):
                                    MazeSecond[RL-1][CL] = 'F'
                                    MazeCheck[RL-1][CL] = 1
                            elif (MazeSecond[RL-1][CL] == 'J'):
                                print('IMPOSSIBLE')
                                BreakCheck = not BreakCheck
                                break
                            if (MazeSecond[RL+1][CL] == '.'):
                                    MazeSecond[RL+1][CL] = 'F'
                                    MazeCheck[RL-1][CL] = 1
                            elif (MazeSecond[RL+1][CL] == 'J'):
                                print('IMPOSSIBLE')
                                BreakCheck = not BreakCheck
                                break
                            if (MazeSecond[RL][CL-1] == '.'):
                                    MazeSecond[RL][CL-1] = 'F'
                                    MazeCheck[RL-1][CL] = 1
                            elif (MazeSecond[RL][CL-1] == 'J'):
                                print('IMPOSSIBLE')
                                BreakCheck = not BreakCheck
                                break
                            if (MazeSecond[RL][CL+1] == '.'):
                                    MazeSecond[RL][CL+1] = 'F'
                                    MazeCheck[RL-1][CL] = 1
                            elif (MazeSecond[RL][CL+1] == 'J'):
                                print('IMPOSSIBLE')
                                BreakCheck = not BreakCheck
                                break
                    case 'J':
                        
            if BreakCheck:
                break
        MazeCheck.clear()
    print(list(MazeSecond))
    MazeSecond.clear()
    

    