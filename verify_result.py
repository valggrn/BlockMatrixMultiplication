import sys
import os
from matrix_utils import get_matrix_from_file, save_matrix_to_file
from numpy import dot, allclose, vstack, hstack

def combine_blocks(blocks):
    top = hstack((blocks[0], blocks[1]))
    bottom = hstack((blocks[2], blocks[3]))
    return vstack((top, bottom))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Не достаточно аргументов")
    name = sys.argv[1]
    blocks = []
    for number in ["11", "12", "21", "22"]:
        blocks.append(get_matrix_from_file(f"./matrix/temp/{name}/C{number}.npy"))
        os.remove(f"./matrix/temp/{name}/C{number}.npy")
    A = get_matrix_from_file(f"./matrix/{name}/A.npy")
    B = get_matrix_from_file(f"./matrix/{name}/B.npy")
    C = combine_blocks(blocks)
    new_C = dot(A, B)
    if not allclose(C, new_C, atol=1e-10):
        raise ValueError("Матрицы не равны")
    else:
        save_matrix_to_file(f"./matrix/{name}/C.npy", C)