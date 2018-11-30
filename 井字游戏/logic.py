def print_square():
    # 0表示空白位置，1表示O， 2表示X
    # 打印井字图
    for line in square:
        lines = ""
        for s in line:    
            if s==0:
                lines +="- "
            elif s ==1:
                lines +="O "
            else:
                lines +="X "
        print (lines)

def set_XY(who, x, y):
    square[y][x] = 1 if who == "O" else 2
    # if who=="O":
    #     square[Y][X] = 1
    # else:
    #     square[Y][X] = 2

def input_XY(who):
    while True:
        input_xy = input(f"输入player {who}坐标，逗号分割：")
        temp = input_xy.split(",") # X -> temp[0], Y -> temp[1] 
        X = int(temp[0])
        Y = int(temp[1])
        
        # 判断是否这个坐标已经被占
        if square[Y][X] != 0:
            print("该位置已被占,请重新输入：")
        else:
            set_XY(who, X, Y)
            print_square()
            return


def judge_win(who:int):
    win = False
    # 横
    for i in range(3):
        # print("==", i)
        if square[i][0] == who and square[i][1] == who and square[i][2] == who:
            win = True

    # 竖
    for i in range(3):
        # print("--",square[:2][i])
        if square[0][i] == who and square[1][i] == who and square[2][i] == who:
            win = True

    # 斜
    if (square[0][0] == who and square[1][1] == who and square[2][2] == who) \
        or (square[2][0] == who and square[1][1] == who and square[0][2] == who):
        win = True

    return win

square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

