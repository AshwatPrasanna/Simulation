import os
import subprocess
from multiprocessing import Pool

def calculate_hnum(n):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    executable = os.path.join(script_dir, "process")
    result = subprocess.run([executable, str(n)], capture_output=True, text=True)
    hnum = int(result.stdout.strip())
    return hnum

def main():
    with Pool(processes=96) as pool:
        n_values = range(31)  # n values from 0 to 30
        hnum_values = pool.map(calculate_hnum, n_values)

    for n, hnum in zip(n_values, hnum_values):
        print(f"hNum for {n}: {hnum}")

# main() to be called to run the program; it might be required to ensure that it runs on the main thread

 