import sys
# classes and code for maze
class Node:
    def __init__(self,state,parent,action):
        self.state = state 
        self.parent = parent 
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self,node):
        self.frontier.append(node)

    def contain_state(self,state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty(self):
            raise Exception ("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier =  self.frontier[:-1]
            return node
    
class QueueFrontier(StackFrontier):
    
    def remove(self):
        if self.empty():
            raise Exception ("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class Maze:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        # Validate start and end
        if contents.count('S') != 1:
            raise Exception("Maze must have exactly one start point 'S'")
        if contents.count('E') != 1:
            raise Exception("Maze must have exactly one end point 'E'")

        # Read maze into a list
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        self.start = None
        self.end = None
        self.letters = {}

        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    char = contents[i][j]
                except IndexError:
                    char = ' '
                if char == 'S':
                    self.start = (i, j)
                    row.append(False)
                elif char == 'E':
                    self.end = (i, j)
                    row.append(False)
                elif char == '#':
                    row.append(True)
                elif char.isalpha():
                    self.letters[char] = (i, j)
                    row.append(False)
                else:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.walls[i][j]:
                    print('#', end='')
                elif (i, j) == self.start:
                    print('S', end='')
                elif (i, j) == self.end:
                    print('E', end='')
                elif self.solution and (i, j) in self.solution:
                    print('*', end='')
                else:
                    letter = [k for k, v in self.letters.items() if v == (i, j)]
                    print(letter[0] if letter else ' ', end='')
            print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)
        explored = set()

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()
            if node.state == self.end:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                cells.reverse()
                actions.reverse()
                self.solution = cells
                return

            explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contain_state(state) and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    