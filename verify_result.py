import sys
from matrix_utils import get_matrix_from_file
from numpy import dot, allclose

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Не достаточно аргументов")
    name = sys.argv[1]
    A = get_matrix_from_file(f"./matrix/{name}/A.npy")
    B = get_matrix_from_file(f"./matrix/{name}/B.npy")
    C = get_matrix_from_file(f"./matrix/{name}/C.npy")
    new_C = dot(A, B)
    if not allclose(C, new_C, atol=1e-10):
        raise ValueError("Матрицы не равны")