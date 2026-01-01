import heapq
import sys

def beautiful_path():
    data = sys.stdin.read().split()
    idx = 0

    n_var = int(data[idx]); idx += 1
    m_var = int(data[idx]); idx += 1
    s_var = int(data[idx]) - 1; idx += 1
    d_var = int(data[idx]) - 1; idx += 1

    node_weight = []
    i_var = 0
    while i_var < n_var:
        node_weight.append(int(data[idx]))
        idx += 1
        i_var += 1

    adj_list = [[] for _ in range(n_var)]
    i_var = 0
    while i_var < m_var:
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        adj_list[u].append(v)
        i_var += 1

    INF = 10**18
    dist = [INF] * n_var
    dist[s_var] = node_weight[s_var]

    pq = []
    heapq.heappush(pq, (dist[s_var], s_var))

    while pq:
        cur_cost, node = heapq.heappop(pq)
        if cur_cost > dist[node]:
            continue

        for nxt in adj_list[node]:
            nd = cur_cost + node_weight[nxt]
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    if dist[d_var] == INF:
        print(-1)
    else:
        print(dist[d_var])
