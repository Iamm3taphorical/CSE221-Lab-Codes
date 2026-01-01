import heapq
import sys

def parity_edges():
    data = sys.stdin.read().split()
    idx = 0

    n_var = int(data[idx]); idx += 1
    m_var = int(data[idx]); idx += 1

    adj_list = [[] for _ in range(n_var)]

    u_list = []
    v_list = []
    w_list = []

    i_var = 0
    while i_var < m_var:
        u_list.append(int(data[idx]) - 1)
        idx += 1
        i_var += 1

    i_var = 0
    while i_var < m_var:
        v_list.append(int(data[idx]) - 1)
        idx += 1
        i_var += 1

    i_var = 0
    while i_var < m_var:
        w_list.append(int(data[idx]))
        idx += 1
        i_var += 1

    i_var = 0
    while i_var < m_var:
        adj_list[u_list[i_var]].append((v_list[i_var], w_list[i_var]))
        i_var += 1

    INF = 10**18
    dist = [[INF, INF] for _ in range(n_var)]
    pq = []

    dist[0][0] = 0
    dist[0][1] = 0
    heapq.heappush(pq, (0, 0, -1))

    while pq:
        cur_dist, node, last_par = heapq.heappop(pq)

        for nxt, wgt in adj_list[node]:
            par = wgt % 2
            if last_par != -1 and par == last_par:
                continue

            nd = cur_dist + wgt
            if nd < dist[nxt][par]:
                dist[nxt][par] = nd
                heapq.heappush(pq, (nd, nxt, par))

    ans = min(dist[n_var - 1])
    print(ans if ans != INF else -1)
