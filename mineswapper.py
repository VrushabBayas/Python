

def mineSwapper(bombs, row, col):

    feilds = [[0 for i in range(col)] for j in range(row)]
    print(feilds)

    for bomb in bombs:
        row_i = bomb[0]
        col_i = bomb[1]
        feilds[row_i][col_i] = -1
        for i in range(row_i-1, row_i+2):
            for j in range(col_i-1, col_i+2):
                if 0 <= i and i < row and 0 <= j and j < col and feilds[i][j] != -1:
                    feilds[i][j] += 1
    return feilds


if __name__ == "__main__":
    print(mineSwapper([[0, 1], [1, 0]], 3, 3))
