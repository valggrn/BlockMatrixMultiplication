import numpy as np
import os

def get_matrix(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Can't find the catalog of the file: {path}")
    return np.load(path)

def save_matrix(path, matrix):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.save(path, matrix)