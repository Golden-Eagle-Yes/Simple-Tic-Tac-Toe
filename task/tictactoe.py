def print_cells(cells_seq):
    print("---------")
    for i in range(9):
        if i == 0 or i == 3 or i == 6:
            print("|", end=' ')
        print(cells_seq[i], end=' ')
        if i == 2 or i == 5 or i == 8:
            print("|")
    print("---------")


cells = ' ' * 9
print_cells(cells)  # print cells before the change
winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
# count_x = cells.count('X')
# count_o = cells.count('O')
# if abs(count_x - count_o) >= 2:
#     print('Impossible')
#     exit()
#
# indexes_x = [i for i in range(9) if cells[i] == 'X']
# indexes_o = [i for i in range(9) if cells[i] == 'O']
#
# x_line = 0
# for sublist in winning_indexes:
#     ind_x = [value for value in indexes_x if value in sublist]
#     if ind_x == sublist:
#         x_line = 1
#         break
#
# o_line = 0
# for sublist in winning_indexes:
#     ind_o = [value for value in indexes_o if value in sublist]
#     if ind_o == sublist:
#         o_line = 1
#         break
#
# if count_x < 3 and count_o < 3 or (x_line != 1 and o_line != 1):
#     if '_' in cells:
#         print('Game not finished')
#     else:
#         print('Draw')
# elif x_line != o_line:
#     if x_line:
#         print('X wins')
#     else:
#         print('O wins')
# else:
#     print('Impossible')

i = 1
x_turn = True
while i:
    try:
        raw, column = [int(x) for x in input().split()]
        one_d_index = (raw - 1) * 3 + column - 1
    except ValueError:
        print('You should enter numbers!')
    else:
        if not(1 <= raw <= 3 and 1 <= column <= 3):
            print('Coordinates should be from 1 to 3!')
        elif cells[one_d_index] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            # changing the cells with newly added X or O
            cells_list = list(cells)
            if x_turn:
                cells_list[one_d_index] = 'X'
                cells = "".join(cells_list)
                print_cells(cells)
                x_turn = False
            else:
                cells_list[one_d_index] = 'O'
                cells = "".join(cells_list)
                print_cells(cells)
                x_turn = True
            # Check if there is a line for X or for O
            count_x = cells.count('X')
            count_o = cells.count('O')
            indexes_x = [i for i in range(9) if cells[i] == 'X']
            indexes_o = [i for i in range(9) if cells[i] == 'O']

            x_line = 0
            for sublist in winning_indexes:
                ind_x = [value for value in indexes_x if value in sublist]
                if ind_x == sublist:
                    x_line = 1
                    break

            o_line = 0
            for sublist in winning_indexes:
                ind_o = [value for value in indexes_o if value in sublist]
                if ind_o == sublist:
                    o_line = 1
                    break

            if count_x < 3 and count_o < 3 or (x_line != 1 and o_line != 1):
                if ' ' in cells:
                    pass
                else:
                    print('Draw')
                    i = 0  # To make sure the execution will exit from the while loop
                    break
            elif x_line != o_line:
                if x_line:
                    print('X wins')
                    i = 0  # To make sure the execution will exit from the while loop
                    break
                else:
                    print('O wins')
                    i = 0  # To make sure the execution will exit from the while loop
                    break

                # i = 0  # To make sure the execution will exit from the while loop
                # break  # Braking from the try loop


# print_cells(cells)  # print cells after the change
