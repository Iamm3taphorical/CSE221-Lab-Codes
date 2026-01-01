import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solve(inorder, post):
    if not inorder:
        return []

    root = post[-1]
    idx = inorder.index(root)

    left = solve(inorder[:idx], post[:idx])
    right = solve(inorder[idx+1:], post[idx:-1])

    return [root] + left + right

n = int(input())
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))

print(*solve(inorder, post))