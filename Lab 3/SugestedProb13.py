import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solve(inorder, preorder):
    if not inorder:
        return []

    root = preorder[0]
    idx = inorder.index(root)

    left = solve(inorder[:idx], preorder[1:idx+1])
    right = solve(inorder[idx+1:], preorder[idx+1:])

    return left + right + [root]

n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

print(*solve(inorder, preorder))