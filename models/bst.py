class BSTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class ItemBST:
    def __init__(self):
        self.root = None

    def insert(self, item):
        self.root = self._insert(self.root, item)

    def _insert(self, node, item):
        if node is None:
            return BSTNode(item)
        if item.name < node.item.name:
            node.left = self._insert(node.left, item)
        else:
            node.right = self._insert(node.right, item)
        return node

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if node is None:
            return None
        if name == node.item.name:
            return node.item
        elif name < node.item.name:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.item] + self._inorder(node.right)