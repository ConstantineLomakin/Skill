from colorama import init
from colorama import Fore

init()

board = list(range(1, 10))


def draw_board(board):  # Функция игровой доски
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)


def take_input(player_token):  # Функция хода
    valid = False
    while not valid:
        player_answer = input('Введите номер ячейки для ' + player_token + ' ')
        try:
            player_answer = int(player_answer)
        except:
            print('Введите номер свободной ячейки')
            continue
        if 1 <= player_answer <= 9:
            if (str(board[player_answer - 1]) not in 'XO'):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print(Fore.LIGHTRED_EX)
                print('Ячейка уже занята')
                print(Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX)
            print('Введите номер ячейки от 1 до 9')
            print(Fore.RESET)


def check_win(board):  # Функция проверки победы
    win_code = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2))
    for each in win_code:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def game(board):  # Игра
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(Fore.LIGHTGREEN_EX)
                print(tmp, ' ПОБЕДИЛ!!!')
                break
        if counter == 9:
            print(Fore.LIGHTYELLOW_EX)
            print('НИЧЬЯ')
            break

    draw_board(board)

game(board)
