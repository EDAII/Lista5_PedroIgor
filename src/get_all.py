from src import rb_tree
nil = rb_tree.Node(None, 'NIL', None)
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
def teste(tree:rb_tree.Node, lista=[], to_visit = [], visited = []):
    if lista == []:
        lista.append(tree)
    if tree.left != nil:
        lista.append(tree.left)
        to_visit.append(tree.left)
    if tree.right != nil:
        lista.append(tree.right)
        to_visit.append(tree.right)
    for i in to_visit:
        t = to_visit[0]
        del to_visit[0]
        return teste(t, lista, to_visit, visited)
    p = tree.parent
    c = tree
    while True:
        print('c p:')
        print(c, p)
        if p == None:
            break
        else:
            c = p
            if p != nil:
                p = p.parent
    return lista
