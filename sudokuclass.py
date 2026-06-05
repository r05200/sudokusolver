class GameState:
    def __init__(self, grid):
        self.grid = grid
        self.children = []
        self.parent = None
        self.is_leaf = self.is_leaf()
    
    def set_grid(self, grid):
        self.grid = grid
    def add_children(self, child_node):
        if child_node is None:
            return ValueError("Child node cannot be none")
        child_node.add_parent(self)
        self.children.append(child_node)
    def add_parent(self, parent_node):
        self.parent = parent_node
    def get_depth(self):
        if self.is_root():
            return 0
        return self.parent.get_depth() + 1
    def is_leaf(self):
        return len(self.children) == 0
    def is_root(self):
        return self.parent is None
            



        
            


