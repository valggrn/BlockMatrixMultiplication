import sys
from matrix_utils import get_matrix_from_file, get_block, save_matrix_to_file, save_block_to_matrix
from numpy import dot
from block_coordinats import BlockCoordinats

def multipe_matrix(A, B):
    return dot(A, B)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError("Не достаточно аргументов")
    name = sys.argv[1]
    block_coord = {
        "11" : {"A" : [BlockCoordinats.BLOCK_11, BlockCoordinats.BLOCK_12], "B" : [BlockCoordinats.BLOCK_11, BlockCoordinats.BLOCK_21], "C" : BlockCoordinats.BLOCK_11},
        "12" : {"A" : [BlockCoordinats.BLOCK_11, BlockCoordinats.BLOCK_12], "B" : [BlockCoordinats.BLOCK_12, BlockCoordinats.BLOCK_22], "C" : BlockCoordinats.BLOCK_12},
        "21" : {"A" : [BlockCoordinats.BLOCK_21, BlockCoordinats.BLOCK_22], "B" : [BlockCoordinats.BLOCK_11, BlockCoordinats.BLOCK_21], "C" : BlockCoordinats.BLOCK_21},
        "22" : {"A" : [BlockCoordinats.BLOCK_21, BlockCoordinats.BLOCK_22], "B" : [BlockCoordinats.BLOCK_12, BlockCoordinats.BLOCK_22], "C" : BlockCoordinats.BLOCK_22},
    }
    block_number = sys.argv[2]
    blocks_number = block_coord[block_number]
    A = get_matrix_from_file(f"./matrix/{name}/A.npy")
    B = get_matrix_from_file(f"./matrix/{name}/B.npy")
    A_blocks = [get_block(A, number.value) for number in blocks_number["A"]]
    B_blocks = [get_block(B, number.value) for number in blocks_number["B"]]
    block = multipe_matrix(A_blocks[0], B_blocks[0]) + multipe_matrix(A_blocks[1], B_blocks[1])
    C = get_matrix_from_file(f"./matrix/{name}/C.npy")
    save_matrix_to_file(f"./matrix/{name}/C", save_block_to_matrix(C, block, blocks_number["C"].value))