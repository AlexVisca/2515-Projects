import random


class Maze:
    """
    Creates a maze class
    """
    def __init__(self, filename):
        self._file = filename

    @property
    def linelist(self):
        with open(self._file, 'r+') as f:
            l = f.readlines()
            f.close()

            line_list = []
            for i in l:
                line = i.strip('\n')
                line_list.append(line)
        return line_list

    def check(self, line_number, column_number):
        if self.linelist[line_number][column_number] == " ":
            return True
        else:
            return False

    def display(self):
        for i in self.linelist:
            print(i)

    def find_random_spot(self):
        random1 = random.randint(1, 21)
        random2 = random.randint(1, 21)
        tup_le = (random1, random2)
        return tup_le


def main():
    amaze = Maze("maze.txt")
    amaze.check(0, 3)
    amaze.display()
    amaze.find_random_spot()


if __name__ == '__main__':
    main()
