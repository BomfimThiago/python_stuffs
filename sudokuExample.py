import numpy as np

sudoku = np.array([
    5, 3, 0, 0, 7, 0, 0, 0, 0,
    6, 0, 0, 1, 9, 5, 0, 0, 0,
    0, 9, 8, 0, 0, 0, 0, 6, 0,
    8, 0, 0, 0, 6, 0, 0, 0, 3,
    4, 0, 0, 8, 0, 3, 0, 0, 1,
    7, 0, 0, 0, 2, 0, 0, 0, 6,
    0, 6, 0, 0, 0, 0, 2, 8, 0,
    0, 0, 0, 4, 1, 9, 0, 0, 5,
    0, 0, 0, 0, 8, 0, 0, 7, 9
]).reshape([9, 9])
# Para resolver um sudoku não podemos ter números iguais na mesma linha, coluna ou quadrante.

# Retirar linha do sudoku [n,:] onde n é o número da linha, pode ser de 0 a 8
print('Linha', sudoku[5,:])

# Retirar coluna do sudoku [:, n] onde n é o número da coluna, pode ser de 0 a 8
print('Coluna', sudoku[:, 5])

# Retirar quadrante
def quadrant(sudoku, x, y):
    xx = x // 3
    yy = y // 3
    return sudoku[xx*3 : (xx + 1)*3, yy*3:(yy+1)* 3]
print(sudoku[5,:])


increase_end_datetime  = False if not stop_time or not start_time or stop_time < start_time else False
if(increase_end_datettime)
