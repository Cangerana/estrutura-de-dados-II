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
            parant = self.root
            while True:
                if value < parant.value:
                    if parant.left:
                        parant = parant.left
                    else:
                        node.parant = parant
                        parant.left = node
                        break
                else:
                    if parant.right:
                        parant = parant.right
                    else:
                        node.parant = parant
                        parant.right = node
                        break

    def remove(self, value):
        if self.is_empty():
            print('Tree is empty!')
        else:
            node = self.root
            while True:
                if node.value == value:
                    self._remove(node)
                    break
                elif node.value < value:
                    if node.right:
                        node = node.right
                    else:
                        print(f'Node [{value:^6}] isent\'t in tree!')
                        break
                else:
                    if node.left:
                        node = node.left
                    else:
                        print(f'Node [{value:^6}] isent\'t in tree!')
                        break

    def _remove(self, node):
        parant = node.parant
        left = right = False

        if node.parant:
            if parant.value > node.value:
                left = True
            else:
                right = True

        if node.left and node.right:
            new_node = self.max_left(node)
            if node.left:
                node.left.parant = new_node
            node.right.parant = new_node

            new_node.parant = parant
            new_node.left = node.left
            new_node.right = node.right

        elif node.left:
            new_node = node.left
            new_node.parant = parant

        elif node.right:
            new_node = node.right
            new_node.parant = parant

        else:
            new_node = None

        if left:
            parant.left = new_node
        elif right:
            parant.right = new_node
        else:
            self.root = new_node

        del node

    def max_left(self, node, remove=True):
        max = node.left
        while max.right:
            max = max.right

        if remove:
            if max is not node.left:
                max.parant.right = None
            else:
                node.left = None
        return max

    def recursion_remove(self):
        count = 0
        while not self.is_empty():
            node = self.root
            print('='*50 + f'\nremoving -> {node}\n' + '='*50)
            count += 1
            self._remove(node)
            # self.pre_ordem()
        print(count)


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