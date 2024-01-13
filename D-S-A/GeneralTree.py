class TreeNode:
    def __init__(self, data):
        self.children = []
        self.data = data
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        level = 0
        node = self.parent
        while node:
            level += 1
            node = node.parent

        return level

    def show_tree(self):
        spaces = '   ' * self.get_level()
        if self.parent:
            spaces += '|__'
            
        print(spaces + self.data)
        for child in self.children:
            child.show_tree()


root = TreeNode('Electronics')
tv = TreeNode('TV')
mobile = TreeNode('Mobile')
laptop = TreeNode('Laptop')

root.add_child(tv)
root.add_child(mobile)
root.add_child(laptop)

tv.add_child(TreeNode('Samsung'))
tv.add_child(TreeNode('Sony'))
mobile.add_child(TreeNode('vivo'))
mobile.add_child(TreeNode('realme'))
laptop.add_child(TreeNode('Lenovo'))
dell = TreeNode('Dell')
laptop.add_child(dell)
dell.add_child(TreeNode('Dell ultra'))

root.show_tree()

print('level of tv :', tv.get_level())
print('level of root :', root.get_level())
print(f'level of {laptop.children[0].data} : {laptop.children[0].get_level()}')

