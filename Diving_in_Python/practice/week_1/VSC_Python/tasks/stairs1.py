import sys

n = int(sys.argv[1])
for i in range(1, int(sys.argv[1])+1):
    print((2*n-(2*i-1)-1)*" "+(i-1)*"# "+"#")