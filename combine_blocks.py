import sys
from numpy import hstack, vstack
import logging
from work_files import get_matrix, save_matrix
from block_numbers import BlockNumber

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def combine_blocks(blocks):
    top = hstack((blocks[0], blocks[1]))
    bottom = hstack((blocks[2], blocks[3]))
    return vstack((top, bottom))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Not enough arguments.")
    name = sys.argv[1]
    blocks_number = [BlockNumber.BLOCK_11, BlockNumber.BLOCK_12, BlockNumber.BLOCK_21, BlockNumber.BLOCK_22]
    blocks = [get_matrix(f"./blocks/{name}/C/{number.value}.npy") for number in blocks_number]
    logging.info("The blocks got")
    C = combine_blocks(blocks)
    save_matrix(f"./result/{name}/C.npy", C)
    logging.info("The matrix combined and saved")