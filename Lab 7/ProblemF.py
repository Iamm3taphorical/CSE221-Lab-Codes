import heapq
import sys

def second_shortest_path():
    data = sys.stdin.read().split()
    idx = 0

    n_var = int(data[idx]); idx += 1
    m_var = int(data[idx]); idx += 1
    s_var = int(data[idx]) - 1; idx += 1
    d_var = int(data[idx]) - 1; idx += 1

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
    dist1 = [INF] * n_var
    dist2 = [INF] * n_var

    dist1[s_var] = 0
    pq = []
    heapq.heappush(pq, (0, s_var))

    while pq:
        cur_dist, node = heapq.heappop(pq)

        for nxt, wgt in adj_list[node]:
            nd = cur_dist + wgt

            if nd < dist1[nxt]:
                dist2[nxt] = dist1[nxt]
                dist1[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

            elif dist1[nxt] < nd < dist2[nxt]:
                dist2[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    print(dist2[d_var] if dist2[d_var] != INF else -1)
