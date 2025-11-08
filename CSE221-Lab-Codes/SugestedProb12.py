import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def get_inorder(pre, post):
    if not pre:
        return []
    root = pre[0]
    if len(pre) == 1:
        return [root]

    left_root = pre[1]
    k = post.index(left_root) 

    left_size = k + 1

    left_pre = pre[1:1+left_size]
    right_pre = pre[1+left_size:]

    left_post = post[:left_size]
    right_post = post[left_size:-1]

    left = get_inorder(left_pre, left_post)
    right = get_inorder(right_pre, right_post)

    return left + [root] + right


n = int(input())

preorder = list(map(int, input().split()))

postorder = list(map(int, input().split()))

result = get_inorder(preorder, postorder)

print(*result)