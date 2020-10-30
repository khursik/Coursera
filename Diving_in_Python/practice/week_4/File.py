import os
import tempfile


class File:

    def __init__(self, filepath):
        self.filepath = filepath
        self.next_line_index = 0
        self.data = []
        self.line_count = 0
        
        if not os.path.exists(filepath):
            with open(filepath, 'w+'):
                pass
    
    def read_lines_from_file(self):
        with open(self.filepath, "r") as f:
            self.data = f.readlines()
            self.line_count = len(self.lines)

    def write(self, string):
        with open(self.filepath, 'w') as f:
            f.write(string)
        self.read_lines_from_file()

    def __add__(self, obj):
        n =  open('new_file.txt', 'w+')
        f1 = open(self.filepath)
        f2 = open(obj.filepath)
        for line in f2.readlines():
            n.write(line)
        for line in f1.readlines():
            n.write(line)
        f1.close()
        f2.close()
        n.close()
        new_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        return File(new_path)

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_line_index >= self.line_count:
            raise StopIteration
        else:
            line = self.lines[self.next_line_index]
            self.next_line_index += 1
            return line

    def __str__(self):
        return os.path.abspath(self.filepath)