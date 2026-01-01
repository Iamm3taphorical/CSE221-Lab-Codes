import sys
# use fast input for competitive programming
input = sys.stdin.readline

# read number of words
n = int(input())

# read all words into list W
W = []
i = 0
while i < n:
    W.append(input().strip())   # strip newline and store word
    i += 1

# adjacency list for directed edges between letters 'a'..'z'
g = [[] for i in range(26)]
# indegree array for letters (used for topological sorting)
ind = [0] * 26
# pres[i] = 1 if letter (i+'a') appears at least once in input
pres = [0] * 26

# mark which letters actually appear in all words
i = 0
while i < n:
    w = W[i]               # current word
    j = 0
    ln = len(w)            # length of word
    while j < ln:
        pres[ord(w[j]) - 97] = 1     # mark letter as present
        j += 1
    i += 1

# build letter ordering constraints from consecutive words
i = 0
valid = 1                  # assume ordering is valid initially
while i + 1 < n:
    a = W[i]               # first word
    b = W[i + 1]           # second word (must come after)

    p = 0
    la = len(a)
    lb = len(b)

    # find first index p where characters differ
    while p < la and p < lb and a[p] == b[p]:
        p += 1

    # if second word is prefix of first word → invalid dictionary order
    if p == lb and la > lb:
        valid = 0
        break

    # if differing characters found, create directed edge a[p] → b[p]
    if p < la and p < lb:
        u = ord(a[p]) - 97      # convert letter to 0–25 index
        v = ord(b[p]) - 97
        g[u].append(v)          # u must come before v
        ind[v] += 1             # increase indegree of v

    i += 1

# if invalid ordering detected earlier, print -1
if valid == 0:
    print(-1)
    sys.exit(0)

# create a min-heap using a Python list (kept sorted manually)
heap = []
sz = 0

# add all letters that appear and have indegree 0
i = 0
while i < 26:
    if pres[i] == 1 and ind[i] == 0:
        heap.append(i)
        sz += 1
    i += 1

# sort to simulate min-heap behavior (smallest letter first)
heap.sort()

# list to hold final topological order of letters
ans = []

# run modified Kahn’s Algorithm with lexicographically smallest selection
while sz > 0:
    u = heap[0]          # take smallest available letter
    ans.append(u)
    heap.pop(0)          # remove it from heap
    sz -= 1

    nbrs = g[u]          # neighbors (letters depending on u)
    j = 0
    ln = len(nbrs)
    while j < ln:
        v = nbrs[j]
        ind[v] -= 1      # remove dependency
        # if v now has indegree 0, add to heap
        if ind[v] == 0:
            heap.append(v)
            sz += 1
            # maintain sorted order by shifting new element left
            k = sz - 1
            while k > 0 and heap[k] < heap[k - 1]:
                tmp = heap[k]
                heap[k] = heap[k - 1]
                heap[k - 1] = tmp
                k -= 1
        j += 1

# if topological sort result doesn't include all present letters → cycle exists
if len(ans) != sum(pres):
    print(-1)
else:
    out = []
    i = 0
    ln = len(ans)
    # convert numeric letter indices back to characters
    while i < ln:
        out.append(chr(ans[i] + 97))
        i += 1
    print("".join(out))