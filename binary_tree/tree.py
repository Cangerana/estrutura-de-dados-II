from node import Node


class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value)

    def is_empty(self):
        return not bool(self.root) or not bool(self.root.value)

    def show(self):
        if self.is_empty():
            print('Tree is empty!')
        else:
            self._show(self.root)

    def _show(self, node):
        if node:
            print(node)
            self._show(node.left)
            self._show(node.right)

    def insert(self, value):
        node = Node(value)
        if self.is_empty():
            self.root = node
        else:
            parent = self.root
            while True:
                if value < parent.value:
                    if parent.left:
                        parent = parent.left
                    else:
                        node.parent = parent
                        parent.left = node
                        break
                else:
                    if parent.right:
                        parent = parent.right
                    else:
                        node.parent = parent
                        parent.right = node
                        break

    def remove(self, value):
        node = self.search(value)
        if node:
            self._remove(node)
        else:
            print(f'Node [ {value} ] isen\'t in tree!')

    def _remove(self, node):
        print(node.parent)
        parent = node.parent
        child = None

        # Have one child on left
        if node.left and not node.right:
            child = node.left
        # Have one child on right
        elif not node.left and node.right:
            child = node.right
        # Have two childs on left and right
        elif node.left and node.right:
            child = self.max_left(node)
            if node.left:
                child.left = node.left
            if node.right:
                child.right = node.right

        if child:
            child.parent = parent
            if child.left:
                child.left.parent = child

            if child.right:
                child.right.parent = child

        if parent:
            if self.is_left(node):
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child

        del node

# ------------- ==== TOOS ==== -------------#

    def search(self, value):
        node = self.root
        while node:
            if node.value == value:
                return node
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        return node

    def max_left(self, node, remove=True):
        max = node.left
        while max.right:
            max = max.right

        if remove:
            self._remove(max)
        return max

    def recursion_remove(self):
        count = 0
        while not self.is_empty():
            node = self.root
            print('='*50 + f'\nremoving -> {node}\n' + '='*50)
            self.remove(node.value)
            count += 1
        print(count)

    def is_left(self, node):
        return node.parent.left is node


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(18)
    tree.insert(14)
    tree.insert(13)
    tree.insert(25)
    tree.insert(27)
    tree.insert(24)
    tree.insert(14)
    tree.insert(17)
    tree.insert(15)
    tree.insert(12)
    tree.show()
    # tree.remove(18)
    # print('removed: 18')
    # tree.show()
    tree.recursion_remove()
