class BinarySearchTree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def add_node(self, val):
        if self.val > val:
            if self.left:
                self.left.add_node(val)
            else:
                self.left = BinarySearchTree(val)

        elif self.val < val:
            if self.right:
                self.right.add_node(val)
            else:
                self.right = BinarySearchTree(val)

    def search(self, val):
        if self.val == val:
            return True

        if self.val > val and self.left is not None:
            return self.left.search(val)
        elif self.val < val and self.right is not None:
            return self.right.search(val)
        else:
            return False

    def find_min(self):
        if self.left is None:
            return self.val

        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.val

        return self.right.find_max()

    def sum_of_tree(self, val=0) -> int:
        if self.left is not None:
            val += self.left.sum_of_tree()
        if self.right is not None:
            val += self.right.sum_of_tree()
        return self.val + val

    def delete_node(self, val):
        if self.val > val:
            if self.left:
                self.left = self.left.delete_node(val)
        elif self.val < val:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                
                # self.val = self.right.find_min()
                # self.right = self.right.delete_node(self.val)
                self.val = self.left.find_max()
                self.right = self.left.delete_node(self.val)

        return self

    def pre_order_traversal(self):
        print(self.val, end=', ')
        if self.left is not None:
            self.left.pre_order_traversal()
        if self.right is not None:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()
        print(self.val, end=', ')
        if self.right is not None:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()
        if self.right is not None:
            self.right.in_order_traversal()
        print(self.val, end=', ')


def build_tree(elements: list):
    root = BinarySearchTree(elements[0])

    for ele in elements[1:]:
        root.add_node(ele)

    return root


if __name__ == '__main__':
    elements = [15, 12, 27, 7, 14, 20, 88, 23, 42, 5]
    root = build_tree(elements)

    root.pre_order_traversal()
    print()
    root.in_order_traversal()
    print()
    root.post_order_traversal()
    print()

    # --------------------------- SEARCH ----------------------------- #
    print(root.search(7))
    print(root.search(42))
    print(root.search(999))

    # --------------------------- MATH OPE ----------------------------- #
    print("Max Element:", root.find_max())
    print("Min Element:", root.find_min())
    print("Sum Element:", root.sum_of_tree())

    # --------------------------- DELETION ----------------------------- #
    # LEAF NODE DELETION
    print("\ndelete 5")
    root.delete_node(5)
    root.in_order_traversal()
    print()

    # NODE WITH ONE CHILD
    print("\ndelete 20")
    root.delete_node(20)
    root.in_order_traversal()
    print()

    # NODE WITH TWO CHILD
    print("\ndelete 27")
    root.delete_node(27)
    root.in_order_traversal()
    print()

    # DUPLICATE NODE
    print("\ndelete 201")
    root.delete_node(201)
    root.pre_order_traversal()
    print()
