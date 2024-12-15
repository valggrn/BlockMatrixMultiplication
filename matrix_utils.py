import numpy as np
import os

def get_matrix_from_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Can't find the catalog of the file: {path}")
    return np.load(path)

def get_block(matrix, coord):
    block_size = matrix.shape[0] // 2
    row, column = coord
    start_row = block_size * row
    start_column = block_size * column
    return matrix[start_row:start_row + block_size, start_column:start_column + block_size]

def save_matrix_to_file(path, matrix):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.save(path, matrix)