table = list(range(1, 10))
print(" ")
print("---" * 16)
print("   Добро пожаловать в игру '\033[95mКрестики Нолики\033[0;0m'!  ")
print("---" * 16, "\n")


def pole(table):
    print("-" * 13)
    for i in range(3):
        print("|", table[0+i*3], "|", table[1+i*3], "|", table[2+i*3], "|")
        print("-" * 13)

def igrok(player_key):
    valid = False
    while not valid:
        player_answer = input(" " + player_key + " Введите свой ход в ячейку под номером: ")
        try:
            player_answer = int(player_answer)
        except:
            print("Вы уверенны что ввели правильное число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(table[player_answer-1]) not in "XO"):
                table[player_answer-1] = player_key
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Error")

def check_win(table):
    win_position = ((0, 1, 2), (3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))
    for each in win_position:
        if table[each[0]] == table[each[1]] == table[each[2]]:
            return table[each[0]]
    return False

def igra(table):
    counter = 0
    win = False
    while not win:
        pole(table)
        print(" ")
        if counter % 2 == 0:
            igrok("\033[93mX\033[0;0m")
        else:
            igrok("\033[91mO\033[0;0m")
        counter +=1
        if counter > 4:
            tmp = check_win(table)
            if tmp:
                print("---" * 15)
                print("\n " + tmp, " Одержал победу!!!\n")
                win = True
                break
        if counter == 9:
            print("Ничья")
            break
    pole(table)
igra(table)
