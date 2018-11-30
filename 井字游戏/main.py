

import logic

logic.print_square()

while True:
    logic.input_XY("O")
    if logic.judge_win(1):
        print("Player O, 你赢了！")
        break
    logic.input_XY("X")
    if logic.judge_win(2):
        print("Player X, 你赢了！")
        break
    # 判断是否胜利

    
