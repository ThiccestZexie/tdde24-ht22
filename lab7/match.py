"""Lab 7A"""

db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to',
                  'computer', 'science']],
       ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using',
                  'python', 'and', 'c++']],
       ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993]]]


def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif isinstance(pattern[0],list):
        return match(seq[0],pattern[0])
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False


def test_match_1():
    """simple matching test"""
 

def search(pattern,db):
    """Returns a list of all sequences in the database that match the pattern"""
    return [seq for seq in db if match(seq, pattern)]


def test_search_1(pattern,db):
    """Checks if lists from the database has been sorted out, True means it works as intended"""

#test_match_1()


"""Lab 7B"""

"""Deluppgift 1"""

def empty_tree_fn():
    return 0

def leaf_fn(key):
    return key**2

def inner_node_fn(key, left_value, right_value):
    return key + left_value


def traverse(tree, inner_node, leaf, empty_tree):

    if isinstance(tree,list):

        if tree == []:
            return empty_tree()

        return inner_node(tree[1],traverse(tree[0], inner_node, leaf, empty_tree),traverse(tree[2], inner_node, leaf, empty_tree))

    elif isinstance(tree,int):
        return leaf(tree)


"""Deluppgift 2"""



"""Deluppgift 3"""

def tree_size(tree):

    def inner_node(key, left_value, right_value):
        return left_value + right_value + 1

    def leaf(key):
        return 1

    def empty_tree():
        return 0

    return traverse(tree, inner_node, leaf, empty_tree)


def test():
    pattern = [['författare', '&'], ['titel', ['--', 'python', '--']], ['år', '&']]
    seq = [['författare', ['steve', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']]

    assert((tree_size([]))) == 0 # Returns 3 should return 0

    assert(tree_size([[],1,[]])) == 1

    assert(tree_size([[1, 2, []], 4, [[], 5, 6]])) == 5
    
    assert traverse([[1, 2, []], 4, [[], 5, 6]], inner_node_fn, leaf_fn, empty_tree_fn) == 7

    assert traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn) == 43 

    assert search(pattern,db)==db
    

    #return match(seq,pattern)
    print(search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']],db))

test()