import numpy as np
from numba import jit,uint32,int32

def build_opt_table(opt_table,v,w):
    j = opt_table.shape[0]-1
    k = opt_table.shape[1]-1
    for j in range(j+1):
        for k in range(k+1):
            if j == 0:
                opt_table[j,k] = 0
            elif w[j-1] <= k:
                opt_table[j,k] = max(opt_table[j-1,k],v[j-1]+opt_table[j-1,k-w[j-1]])
            else:
                opt_table[j,k] = opt_table[j-1,k]
    return opt_table

def traceback(opt_table,j,k,w):
    taken = []
    for j in reversed(range(j+1)):
        if opt_table[j,k] == opt_table[j-1,k]:
            taken.append(0)
        else:
            taken.append(1)
            k -= w[j-1]
    taken = taken[::-1]
    del taken[0]
    return taken

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    j = int(firstLine[0])
    k = int(firstLine[1])

    v = []
    w = []

    for i in range(1, j+1):
        line = lines[i]
        parts = line.split()

        v.append(int(parts[0]))
        w.append(int(parts[1]))

    v = np.array(v,dtype=np.int32)
    w = np.array(w,dtype=np.int32)
    opt_table = np.zeros((j+1,k+1),dtype=np.int32)
    build_opt_table_fast = jit(int32[:,:](int32[:,:],int32[:],int32[:]))(build_opt_table)
    opt_table = build_opt_table_fast(opt_table,v,w)
    value = int(opt_table[j,k])
    taken = traceback(opt_table,j,k,w)

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print (solveIt(inputData))
    else:
        print ('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
