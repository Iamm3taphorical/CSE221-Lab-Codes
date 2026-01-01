import heapq
import sys

def dijkstra(start_node, adj_list, n_var):
    INF = 10**18
    dist = [INF] * n_var
    dist[start_node] = 0

    pq = []
    heapq.heappush(pq, (0, start_node))

    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist > dist[node]:
            continue

        for nxt, wgt in adj_list[node]:
            nd = cur_dist + wgt
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return dist


def where_to_meet():
    data = sys.stdin.read().split()
    idx = 0

    n_var = int(data[idx]); idx += 1
    m_var = int(data[idx]); idx += 1
    a_var = int(data[idx]) - 1; idx += 1
    b_var = int(data[idx]) - 1; idx += 1

    adj_list = [[] for _ in range(n_var)]

    i_var = 0
    while i_var < m_var:
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        adj_list[u].append((v, w))
        i_var += 1

    dist_a = dijkstra(a_var, adj_list, n_var)
    dist_b = dijkstra(b_var, adj_list, n_var)

    INF = 10**18
    best_time = INF
    best_node = -1

    i_var = 0
    while i_var < n_var:
        if dist_a[i_var] != INF and dist_b[i_var] != INF:
            meet_time = max(dist_a[i_var], dist_b[i_var])
            if meet_time < best_time or (meet_time == best_time and i_var < best_node):
                best_time = meet_time
                best_node = i_var
        i_var += 1

    if best_node == -1:
        print(-1)
    else:
        print(best_time, best_node + 1)
