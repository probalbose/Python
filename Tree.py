class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Windows"))

    tablet = TreeNode("Tablet")
    tablet.add_child(TreeNode("iPad"))

    tv = TreeNode("Television")
    tv.add_child(TreeNode("Panasonic"))

    root.add_child(laptop)
    root.add_child(tablet)
    root.add_child(tv)


    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
    