
for i in range(0, E*2, 2):
    u, v = arr[i], arr[i+1]
    G[u].append(v)
    G[v].append(u)

