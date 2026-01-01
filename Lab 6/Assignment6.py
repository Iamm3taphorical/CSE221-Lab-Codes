import sys
# use fast input because constraints can be large
input = sys.stdin.readline

# maximum number for which we precompute primes and prime factors
MAX = 5000

# is_p[i] = 1 means i is prime, 0 means composite
is_p = [1] * (MAX + 1)
is_p[0] = is_p[1] = 0     # 0 and 1 are not primes

# run Sieve of Eratosthenes to find all primes up to MAX
i = 2
while i * i <= MAX:       # only need to check primes up to sqrt(MAX)
    if is_p[i]:           # if i is still marked prime
        j = i * i         # start marking multiples from i^2
        while j <= MAX:
            is_p[j] = 0   # mark composite
            j += i        # next multiple
    i += 1                # move to next number

# create list of prime factors for each number from 0..MAX
pf = [[] for _ in range(MAX + 1)]

# compute distinct prime factors for each number by trial division
n = 2
while n <= MAX:
    x = 2
    # check all possible divisors up to sqrt(n)
    while x * x <= n:
        if n % x == 0:            # x divides n
            if is_p[x]:           # if x is prime, add as factor
                pf[n].append(x)
            y = n // x            # complementary divisor
            # add complementary divisor only if distinct, prime, and not equal to n
            if y != x and is_p[y] and y != n:
                pf[n].append(y)
        x += 1
    n += 1

# read number of test cases
T = int(input())

for _ in range(T):
    # read start (s) and target (t)
    s, t = map(int, input().split())

    # if start and target are same, zero moves needed
    if s == t:
        print(0)
        continue

    # dist[x] = minimum steps to reach x, initialize as unvisited
    dist = [-1] * (MAX + 1)

    # queue for BFS
    q = [0] * (MAX + 1)
    f = 0   # front pointer
    b = 0   # back pointer

    # initialize BFS from s
    dist[s] = 0
    q[0] = s
    b = 1

    res = -1   # stores final result (steps to reach t)

    # BFS loop
    while f < b:
        u = q[f]      # current node
        f += 1

        # try adding each prime factor of current number u
        for p in pf[u]:
            nxt = u + p   # new number after move

            # valid move: must not exceed t and not visited before
            if nxt <= t and dist[nxt] == -1:
                dist[nxt] = dist[u] + 1

                # if we reached the target, store result and break
                if nxt == t:
                    res = dist[nxt]
                    break

                # otherwise, enqueue next state
                q[b] = nxt
                b += 1

        # if we already found the target, stop BFS
        if res != -1:
            break

    # print answer (or -1 if unreachable)
    print(res)