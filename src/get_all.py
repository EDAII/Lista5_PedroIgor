from src import rb_tree
def get_all(tree:rb_tree.Node, lista=[]):
    try:
        lista.append(tree)

        lista.append(tree.left)
        lista.append(tree.right)

        lista.append(tree.left.left)
        lista.append(tree.left.right)
        lista.append(tree.right.left)
        lista.append(tree.right.right)

        lista.append(tree.left.left.left)
        lista.append(tree.left.left.right)
        lista.append(tree.left.right.left)
        lista.append(tree.left.right.right)
        lista.append(tree.right.left.left)
        lista.append(tree.right.left.right)
        lista.append(tree.right.right.left)
        lista.append(tree.right.right.right)
    except:
        return lista

    return lista
