class ManagementTree:
    def __init__(self, name: str, des: str):
        self.name = name
        self.designation = des.upper()
        self.children = []
        self.parent = None

    def add_child(self, nodes):
        for node in nodes:
            self.children.append(node)
            node.parent = self

    def get_level(self) -> int:
        level = 0
        node = self
        while node.parent:
            level += 1
            node = node.parent

        return level

    def show_tree(self, label=None):
        if label == 'name':
            value = self.name
        elif label == 'designation' or label == 'des':
            value = self.designation
        else:
            value = self.name + '(' + self.designation + ')'

        spaces = '   ' * self.get_level()
        if self.parent:
            spaces += '|__'
        print(spaces + value)
        for child in self.children:
            child.show_tree(label)


def build_tree():
    root = ManagementTree('shiva', 'ceo')
    shudipto = ManagementTree('shudipto', 'fullstack')
    antro = ManagementTree('antro', 'backend')
    elsin = ManagementTree('elsin', 'frontend')
    tamil = ManagementTree('tamil', 'frontend trainee')
    sabari = ManagementTree('sabari', 'backend trainee')

    root.add_child([shudipto, antro, elsin])
    antro.add_child([sabari])
    elsin.add_child([tamil])

    print("full tree----->")
    root.show_tree('both')
    print("\n\nname only----->")
    root.show_tree('name')
    print("\n\ndesignation only----->")
    root.show_tree('des')


if __name__ == '__main__':
    build_tree()
