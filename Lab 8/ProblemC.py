import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    
    edges.sort()
    
    # Union-Find
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Build MST using Kruskal's
    mst_cost = 0
    mst_edges = []
    non_mst_edges = []
    mst_edge_count = 0
    
    for w, u, v in edges:
        if union(u, v):
            mst_cost += w
            mst_edges.append((u, v, w))
            mst_edge_count += 1
        else:
            non_mst_edges.append((u, v, w))
    
    # Check if MST exists (graph is connected)
    if mst_edge_count != N - 1:
        print(-1)
        return
    
    # Build adjacency list for MST
    adj = defaultdict(list)
    for u, v, w in mst_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Function to find max edge weight on path from src to dst in MST
    def find_max_edge(src, dst):
        # BFS/DFS to find path and max edge
        visited = [False] * (N + 1)
        stack = [(src, 0)]  # (node, max_edge_so_far)
        visited[src] = True
        parent_info = {src: (None, 0)}  # node -> (parent, edge_weight)
        
        while stack:
            node, max_w = stack.pop()
            if node == dst:
                # Trace back to find max edge
                max_edge = 0
                curr = dst
                while parent_info[curr][0] is not None:
                    max_edge = max(max_edge, parent_info[curr][1])
                    curr = parent_info[curr][0]
                return max_edge
            
            for neighbor, weight in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent_info[neighbor] = (node, weight)
                    stack.append((neighbor, max(max_w, weight)))
        
        return -1  # Should not happen in a connected MST
    
    # Find second best MST
    second_best = float('inf')
    
    for u, v, w in non_mst_edges:
        max_edge = find_max_edge(u, v)
        if max_edge < w:  # Strictly greater MST cost
            candidate = mst_cost - max_edge + w
            second_best = min(second_best, candidate)
    
    # Also consider replacing MST edges with other edges of same weight
    # For edges with same weight, we need to check if there's an alternative
    # This handles the case where multiple MSTs exist with same cost
    
    # Check all edges (including those that could form alternative MSTs)
    for i, (u1, v1, w1) in enumerate(mst_edges):
        for u2, v2, w2 in non_mst_edges:
            if w2 == w1:
                # Check if swapping creates a valid tree with same cost
                # We need MST without edge (u1,v1) and with edge (u2,v2)
                # Reset union-find
                parent2 = list(range(N + 1))
                rank2 = [0] * (N + 1)
                
                def find2(x):
                    if parent2[x] != x:
                        parent2[x] = find2(parent2[x])
                    return parent2[x]
                
                def union2(x, y):
                    px, py = find2(x), find2(y)
                    if px == py:
                        return False
                    if rank2[px] < rank2[py]:
                        px, py = py, px
                    parent2[py] = px
                    if rank2[px] == rank2[py]:
                        rank2[px] += 1
                    return True
                
                # Add all MST edges except (u1, v1)
                count = 0
                for j, (a, b, c) in enumerate(mst_edges):
                    if i != j:
                        union2(a, b)
                        count += 1
                
                # Try to add edge (u2, v2)
                if union2(u2, v2):
                    count += 1
                    if count == N - 1:
                        # Valid alternative MST with same cost - not second best
                        pass
    
    if second_best == float('inf'):
        print(-1)
    else:
        print(second_best)

solve()
