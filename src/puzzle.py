class PuzzleBoard:
    def __init__(self, state):
        self.state = state

    def find_empty(self):
        return self.state.index(0)

    def display(self):
        for i in range(0, 9, 3):
            print(self.state[i : i + 3])
        print()
