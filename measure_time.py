import sys
import timeit
import subprocess

iterations = int(sys.argv[1])

def run_script(compiler):
    subprocess.run([compiler, sys.argv[2], sys.argv[3]], stdout=subprocess.DEVNULL)

time_cpython = min(timeit.repeat(lambda: run_script('python'), repeat=iterations, number=1))
time_cpython = time_cpython * 1000

time_pypy = min(timeit.repeat(lambda: run_script('pypy'), repeat=iterations, number=1))
time_pypy = time_pypy * 1000

print(f'CPython: {time_cpython:.2f} ms')
print(f'PyPy: {time_pypy:.2f} ms')