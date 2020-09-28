class Node:
    def __init__(self, value, parant=None, left=None, right=None):
        self.value = value
        self.parant = parant
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.value:^6}]'
