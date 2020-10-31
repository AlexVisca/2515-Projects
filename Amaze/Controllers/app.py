from Amaze.Models import Maze


class App:
    """Application Controller"""
    def __init__(self, filename=None):
        self._maze = Maze.load_all_from_file(filename)
