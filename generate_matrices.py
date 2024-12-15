import sys
from matrix_utils import save_matrix_to_file
import numpy as np

def generate_matrix(size):
    return np.random.rand(size, size)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError("Не достаточно аргументов")
    name = sys.argv[1]
    size = int(sys.argv[2])
    if size % 2 != 0:
        raise ValueError("Размер матриц должен быть кратен 2")
    A = generate_matrix(size)
    B = generate_matrix(size)
    save_matrix_to_file(f"./matrix/{name}/A.npy", A)
    save_matrix_to_file(f"./matrix/{name}/B.npy", B)