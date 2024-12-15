import subprocess
import sys
import time 

start = time.time()
name = sys.argv[1]
size = int(sys.argv[2])
scripts = [
    {'script' : 'generate_matrices.py', 'params' : [name, size]},
    {'script' : 'block_multiplication.py', 'params' : [name, "11"]},
    {'script' : 'block_multiplication.py', 'params' : [name, "12"]},
    {'script' : 'block_multiplication.py', 'params' : [name, "21"]},
    {'script' : 'block_multiplication.py', 'params' : [name, "22"]},
    {'script' : 'verify_result.py', 'params' : [name]}
]

for script in scripts:
    argv = ["python", script['script']]
    for arg in script['params']:
        argv.append(str(arg))
    try:
        process = subprocess.run(argv, check=True)
    except subprocess.CalledProcessError:
        break

end = time.time()
print(f"{end - start} сек.")