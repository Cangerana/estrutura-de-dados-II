class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        # conteudo
        self.value = value

        # Ponteiro
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        return f'''
                        -> Parent({self.parent.value if self.parent else None})
[{self.value:^6}]                -> Left({self.left.value if self.left else None})     [height -> {self.height}]
                        -> Right({self.right.value if self.right else None})'''
