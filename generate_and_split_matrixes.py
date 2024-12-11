import sys
from work_files import save_matrix
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_matrix(size):
    logging.info(f"Generating matrix of size {size}x{size}")
    return np.random.rand(size, size)

def split_matrix_by_blocks(name, matrix):
    half = matrix.shape[0] // 2
    matrix_11 = matrix[:half, :half]
    matrix_12 = matrix[:half, half:]
    matrix_21 = matrix[half:, :half]
    matrix_22 = matrix[half:, half:]
    blocks = [matrix_11, matrix_12, matrix_21, matrix_22]
    block_names = ["11", "12", "21", "22"]
    for i, block in enumerate(blocks):
        save_matrix(f"./blocks/{name}/{block_names[i]}", block)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError("Not enough arguments. Please provide the name and size of the matrices.")
    name = sys.argv[1]
    size = int(sys.argv[2])
    logging.info(f"Starting matrix generation and splitting for {name} with size {size}")
    A = generate_matrix(size)
    B = generate_matrix(size)
    save_matrix(f"./source/{name}/A", A)
    save_matrix(f"./source/{name}/B", B)
    logging.info("Matrix generated and saved")
    split_matrix_by_blocks(f"{name}/A", A)
    split_matrix_by_blocks(f"{name}/B", B)
    logging.info("Matrix splitted by blocks and the block saved")