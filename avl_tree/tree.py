from node import Node


class AVLTree:
    def __init__(self, value=None):
        self.root = Node(value) if value else None

    def is_empty(self):
        return not bool(self.root)

    def in_order(self):
        return print('Tree is empty!') if self.is_empty() else self._in_order(self.root)

    def pre_ordem(self):
        return print('Tree is empty!') if self.is_empty() else self._pre_ordem(self.root)

    def pos_order(self):
        return print('Tree is empty!') if self.is_empty() else self._pos_order(self.root)

    def _pre_ordem(self, node=None):
        if node and self.is_empty:
            print(node)
            self._pre_ordem(node.left)
            self._pre_ordem(node.right)

    def _in_order(self, node=None):
        if node and self.is_empty:
            self._in_order(node.left)
            print(node)
            self._in_order(node.right)

    def _pos_ordem(self, node=None):
        if node and self.is_empty:
            self._pos_order(node.left)
            self._pos_order(node.right)
            print(node)

    def insert(self, value):
        node = Node(value)
        if self.is_empty():
            self.root = node
        else:
            parent = self.root
            while True:
                # insert in left side
                if value < parent.value:
                    if parent.left:
                        parent = parent.left
                    else:
                        node.parent = parent
                        parent.left = node
                        break
                # insert in right side
                else:
                    if parent.right:
                        parent = parent.right
                    else:
                        node.parent = parent
                        parent.right = node
                        break
            self.update_height(parent)

    def rotations(self, node):
        # simple left rotation
        if self.get_balance(node) == 2 and self.get_balance(node.right) == 1:
            self.left_rotate(node)
        # simple right rotation
        elif self.get_balance(node) == -2 and self.get_balance(node.left) == -1:
            self.right_rotate(node)
        # right left rotations
        elif self.get_balance(node) == 2 and self.get_balance(node.right) == -1:
            self.right_rotate(node.right)
            self.left_rotate(node)
        # left right  ratation
        elif self.get_balance(node) == -2 and self.get_balance(node.left) == 1:
            self.left_rotate(node.left)
            self.right_rotate(node)

    def left_rotate(self, parent, balance=True):
        child = parent.right
        child.parent = parent.parent

        if self.root is parent:
            self.root = child
        else:
            if self.is_left(parent):
                parent.parent.left = child
            else:
                parent.parent.right = child

        parent.parent = child
        parent.right = child.left

        child.left = parent

        if parent.right:
            parent.right.parent = parent

        if balance:
            self.update_height(parent, False)

    def right_rotate(self, parent, balance=True):
        child = parent.left
        child.parent = parent.parent

        if self.root is parent:
            self.root = child
        else:
            if self.is_left(parent):
                parent.parent.left = child
            else:
                parent.parent.right = child

        parent.parent = child
        parent.left = child.right

        child.right = parent

        if parent.left:
            parent.left.parent = parent

        if balance:
            self.update_height(parent, False)

    def remove(self, value):
        node = self.search(value)
        if node:
            self._remove(node)
        else:
            print(f'Node [ {value} ] isen\'t in tree!')

    def _remove(self, node, balance=True):
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
        if balance:
            self.update_height(child)
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

    def is_left(self, node):
        return node.parent.left is node

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if node:
            return self.get_height(node.right) - self.get_height(node.left)
        else:
            return 0

    def update_height(self, node, balance=True):
        while node:
            node.height = 1 + \
                max(self.get_height(node.left),
                    self.get_height(node.right))

            if abs(self.get_balance(node)) == 2 and balance:
                self.rotations(node)

            node = node.parent

    def max_left(self, node, remove=True):
        max = node.left
        while max.right:
            max = max.right

        if remove:
            self._remove(max, False)
        return max

    def recursion_remove(self):
        count = 0
        while not self.is_empty():
            node = self.root
            print('='*50 + f'\nremoving -> {node}\n' + '='*50)
            self.remove(node.value)
            count += 1
        print(count)


if __name__ == '__main__':
    from random import randint
    tree = AVLTree()
    nodes = [randint(0, 1000) for _ in range(100)]
    # nodes = [16, 9, 0, 9, 12]
    for value in nodes:
        tree.insert(value)
    print(nodes)
    tree.in_order()

    # tree.recursion_remove()
