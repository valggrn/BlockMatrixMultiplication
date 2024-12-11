import sys
from work_files import get_matrix, save_matrix
import logging
from numpy import dot
from block_numbers import BlockNumber

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def multipe_matrix(A, B):
    return dot(A, B)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError("Not enough arguments.")
    name = sys.argv[1]
    indices = {
        "11" : {"A" : [BlockNumber.BLOCK_11, BlockNumber.BLOCK_12], "B" : [BlockNumber.BLOCK_11, BlockNumber.BLOCK_21]},
        "12" : {"A" : [BlockNumber.BLOCK_11, BlockNumber.BLOCK_12], "B" : [BlockNumber.BLOCK_12, BlockNumber.BLOCK_22]},
        "21" : {"A" : [BlockNumber.BLOCK_21, BlockNumber.BLOCK_22], "B" : [BlockNumber.BLOCK_11, BlockNumber.BLOCK_21]},
        "22" : {"A" : [BlockNumber.BLOCK_21, BlockNumber.BLOCK_22], "B" : [BlockNumber.BLOCK_12, BlockNumber.BLOCK_22]},
    }
    block_number = sys.argv[2]
    blocks_number = indices[block_number]
    A = [get_matrix(f"./blocks/{name}/A/{number.value}.npy") for number in blocks_number["A"]]
    B = [get_matrix(f"./blocks/{name}/B/{number.value}.npy") for number in blocks_number["B"]]
    logging.info("The blocks got")
    block = multipe_matrix(A[0], B[0]) + multipe_matrix(A[1], B[1])
    save_matrix(f"./blocks/{name}/C/{block_number}", block)
    logging.info(f"The block with number {name} calculated and saved")