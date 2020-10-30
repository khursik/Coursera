N = 3
a = [[i*N+j for j in range(N)][::1 if i % 2 == 0 else -1] for i in range(N)]
print(a[1][2])