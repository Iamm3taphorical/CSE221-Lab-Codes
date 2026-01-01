import heapq
import sys

def minimize_danger():
    data = sys.stdin.read().split()
    idx = 0

    n_var = int(data[idx]); idx += 1
    m_var = int(data[idx]); idx += 1

    adj_list = [[] for _ in range(n_var)]

    i_var = 0
    while i_var < m_var:
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3

        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
        i_var += 1

    INF = 10**18
    danger = [INF] * n_var
    danger[0] = 0

    pq = []
    heapq.heappush(pq, (0, 0))

    while pq:
        cur_danger, node = heapq.heappop(pq)
        if cur_danger > danger[node]:
            continue

        for nxt, wgt in adj_list[node]:
            nd = max(cur_danger, wgt)
            if nd < danger[nxt]:
                danger[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    result = []
    i_var = 0
    while i_var < n_var:
        if danger[i_var] == INF:
            result.append("-1")
        else:
            result.append(str(danger[i_var]))
        i_var += 1

    print(" ".join(result))
