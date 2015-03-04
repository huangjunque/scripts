#encoding=utf8
import pickle

class Node(object):
    """
    一个所有结点都可知它所连通的其它结点的简单有向图。
    """
    def __init__(self, name):
        self.name = name
        self.connections = []
        return

    def add_edge(self, node):
        "创建两个结点之间的一条边。"
        self.connections.append(node)
        return

    def __iter__(self):
        return iter(self.connections)

def preorder_traversal(root, seen=None, parent=None):
    """产生器（Generator ）函数通过一个先根遍历（preorder traversal）生成（yield）边。"""
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        for (parent, subnode) in preorder_traversal(node, seen, root):
            yield (parent, subnode)
    return

def show_edges(root):
    "打印图中的所有边。"
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print '%5s -> %2s (%s)' % (parent.name, child.name, id(child))

# 创建结点。
root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')

# 添加边。
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print 'ORIGINAL GRAPH:'
show_edges(root)

# 腌渍和反腌渍该图来创建
# 一个结点集合。
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print
print 'RELOADED GRAPH:'
show_edges(reloaded)
