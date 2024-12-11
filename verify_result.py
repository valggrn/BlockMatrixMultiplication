import sys
from work_files import get_matrix
from numpy import dot, allclose
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Not enough arguments.")
    name = sys.argv[1]
    A = get_matrix(f"./source/{name}/A.npy")
    B = get_matrix(f"./source/{name}/B.npy")
    C = get_matrix(f"./result/{name}/C.npy")
    logging.info("The matrices got")
    new_C = dot(A, B)
    logging.info("The matrix got by multiplication")
    if allclose(C, new_C, atol=1e-10):
        print("Done")
    else:
        print("Wrong")