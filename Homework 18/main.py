import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_leaves(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.key, end=' ')
            self._print_leaves(node.left)
            self._print_leaves(node.right)

    def print_leaves(self):
        self._print_leaves(self.root)
        print()


def add_edges(graph, node, pos, x=0, y=0, level=1):
    if node is not None:
        pos[node.key] = (x, y)
        if node.left:
            graph.add_edge(node.key, node.left.key)
            add_edges(graph, node.left, pos, x - 1 / 2 ** level, y - 1, level + 1)
        if node.right:
            graph.add_edge(node.key, node.right.key)
            add_edges(graph, node.right, pos, x + 1 / 2 ** level, y - 1, level + 1)


bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(9)
bst.insert(6)
bst.insert(12)
bst.insert(4)
bst.insert(1)
bst.insert(8)
bst.insert(59)


print("Leaf nodes:")
bst.print_leaves()

graph = nx.DiGraph()
pos = {}
add_edges(graph, bst.root, pos)

plt.figure(figsize=(8, 6))
nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', edge_color='gray', font_size=10)
plt.show()