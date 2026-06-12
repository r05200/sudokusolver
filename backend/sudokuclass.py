#Node Class
class CurrentlyTried:
    def __init__(self, value=None, position=None, next_array=None):
        self.value = value
        self.position = position
        self.next_array = next_array
        self.prev = None
    # def __repr__(self):
    #     return str(self.value)


#Stack Class
class GameState:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def push(self, next_array=None, value=None, position=None):
        new_tried = CurrentlyTried(value=value, position=position, next_array=next_array)
        new_tried.prev = self.top
        self.top = new_tried
        self.size += 1
    
    def pop(self):
        if self.top is None:
            raise ValueError("Cannot pop from empty stack")
        pop_value = self.top.value
        self.top = self.top.prev
        self.size -= 1
        return pop_value

    def peek(self):
        if self.top is None:
            raise ValueError("Cannot peek empty stack")
        return self.top.value
    


            




        
            


