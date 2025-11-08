
data_var = input()
nodes_var = int(data_var)


inorder_var = list(map(int, input().split()))

postorder_var = list(map(int, input().split()))

def preorder_traversal_var(inorder_list_var, postorder_list_var):

    if len(inorder_list_var) == 0:

        return []

    root_var = postorder_list_var[-1]
    

    index_var = inorder_list_var.index(root_var)
    

    left_inorder_var = inorder_list_var[:index_var]

    right_inorder_var = inorder_list_var[index_var + 1:]
    
    left_postorder_var = postorder_list_var[:index_var]

    right_postorder_var = postorder_list_var[index_var : len(postorder_list_var) - 1]
    

    left_preorder_var = preorder_traversal_var(left_inorder_var, left_postorder_var)
    right_preorder_var = preorder_traversal_var(right_inorder_var, right_postorder_var)
    
    return [root_var] + left_preorder_var + right_preorder_var


preorder_var = preorder_traversal_var(inorder_var, postorder_var)


print(*preorder_var)
