data_var = input()

nodes_var = int(data_var)


inorder_var = list(map(int, input().split()))

preorder_var = list(map(int, input().split()))

def postorder_traversal_var(inorder_list_var, preorder_list_var):
    
    if len(inorder_list_var) == 0:

        return []
    
    root_var = preorder_list_var[0]
    

    index_var = inorder_list_var.index(root_var)
    

    left_inorder_var = inorder_list_var[:index_var]

    right_inorder_var = inorder_list_var[index_var + 1:]
    
    left_preorder_var = preorder_list_var[1 : index_var + 1]

    right_preorder_var = preorder_list_var[index_var + 1 :]
    
    left_postorder_var = postorder_traversal_var(left_inorder_var, left_preorder_var)

    right_postorder_var = postorder_traversal_var(right_inorder_var, right_preorder_var)
    
    return left_postorder_var + right_postorder_var + [root_var]


postorder_var = postorder_traversal_var(inorder_var, preorder_var)

print(*postorder_var)
