import os
import subprocess
from multiprocessing import Pool

def calculate_hnum(n):
    executable = os.path.join(os.path.dirname(__file__), "process")
    result = subprocess.run([executable, str(n)], capture_output=True, text=True)
    hnum = int(result.stdout.strip())
    return hnum

def main():
    with Pool(processes=96) as pool:
        n_values = range(41)  # n values from 0 to 10
        hnum_values = pool.map(calculate_hnum, n_values)

    for n, hnum in zip(n_values, hnum_values):
        print(f"hNum for {n}: {hnum}")

