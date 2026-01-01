import heapq
import sys

def shortest_path_task():
    data = sys.stdin.read().strip().split()
    idx = 0

    n_var = int(data[idx]); idx += 1
    m_var = int(data[idx]); idx += 1
    s_var = int(data[idx]) - 1; idx += 1
    d_var = int(data[idx]) - 1; idx += 1

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

    adj_list = [[] for _ in range(n_var)]
    i_var = 0
    while i_var < m_var:
        adj_list[u_list[i_var]].append((v_list[i_var], w_list[i_var]))
        i_var += 1

    INF = 10**18
    dist = [INF] * n_var
    parent = [-1] * n_var

    pq = []
    dist[s_var] = 0
    heapq.heappush(pq, (0, s_var))

    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist > dist[node]:
            continue

        for nxt, wgt in adj_list[node]:
            new_dist = cur_dist + wgt
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                parent[nxt] = node
                heapq.heappush(pq, (new_dist, nxt))

    if dist[d_var] == INF:
        print(-1)
        return

    path = []
    cur = d_var
    while cur != -1:
        path.append(cur + 1)
        cur = parent[cur]

    path.reverse()

    print(dist[d_var])
    print(" ".join(map(str, path)))
