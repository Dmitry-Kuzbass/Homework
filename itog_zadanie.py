
print(' ' * 25, "Правила игры 'Крестики нолики'")
print('''           Игроки по очереди ставят на свободные клетки поля 3×3 знаки 
        (один всегда крестики, другой всегда нолики). Первый, выстроивший 
        в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, 
        выигрывает. Если игроки заполнили все 9 ячеек и оказалось, 
        что ни в одной вертикали, горизонтали или большой диагонали нет трёх 
        одинаковых знаков, партия считается закончившейся вничью. 
        Первый ход делает игрок, ставящий крестики.''')

board = [[" - " for _ in range(3)] for _ in range(3)]
# Пустое поле
def print_board(board):  # Функция печати игрового поля
    # Печать номера столбца
    print(" " * 19, end="")
    for col in range(len(board[0])):
        print(f'{col}', end="   ")
    print()
    # Печать игрового поля с номерами строк
    for inx, line in enumerate(board):
        print(" " * 15, inx, " ".join(line))

def victory_check(board): # Функция проверки победы
    # Проверка строк
    for line in board:
        if line[0] == line[1] == line[2] != " - ":
            return line[0]

    # Проверка столбцов
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != " - ":
            return board[0][column]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " - ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " - ":
        return board[0][2]

    return None

def no_moves(board):
    # Прверка на наличие хода
    for line in board:
        if " - " in line:
            return False
    return True

def x_and_o(): # Основная функцмя игры, ввод даннх, оценка состояния игры
    player1 = input('1 игрок играет за X, введите ваше имя: ')
    player2 = input('2 игрок играет за 0, введите ваше имя: ')
    current_player = " X "


    while True:
        print_board(board)
        # Ввод значения хода
        if current_player == " X ":
            line = int(input(f"Игрок {player1}, введите номер строки (0-2): "))
            column = int(input(f"Игрок {player1}, введите номер столбца (0-2): "))
        else:
            line = int(input(f"Игрок {player2}, введите номер строки (0-2): "))
            column = int(input(f"Игрок {player2}, введите номер столбца (0-2): "))

        if line > 2 or column > 2:
            # Проверяем корректность ввода данных
            print("Неверное значение, введите заново")
            continue
        if board[line][column] == " - ":
            # Проверка на занятость ячейки
            board[line][column] = current_player
        else:
            print("Данная клетка занята, введите другие данные.")
            continue

        victory = victory_check(board)
        if victory:
            # Оценка победы
            print_board(board)
            if current_player == ' X ':
                print(f"УРА! {player1} выиграл!")
            else:
                print(f"УРА! {player2} выиграл!")
            break

        if no_moves(board):
            # Прверка наличия хода
            print_board(board)
            print("Конец игры, ничья")
            break

        current_player = " O " if current_player == " X " else " X "
        # Смена игрока



x_and_o()


