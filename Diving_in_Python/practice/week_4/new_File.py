import os
import tempfile


class File:

    flag = 0
    sch = 1

    def __init__(self, filepath):
        self.filepath = filepath
        self.cur_position = 0
        
        if not os.path.exists(filepath):
            with open(filepath, 'w+'):
                pass
    
    def read(self):
        with open(self.filepath, 'r') as f:
            return f.read()

    def write(self, string):
        with open(self.filepath, 'w') as f:
            f.write(string)

    def __add__(self, obj):
        if flag == 1:
            sch += 1


        n = open('new_file'+str(sch)+'.txt', 'w+')
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
        flag = 1
        return File(new_path)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.filepath, 'r') as f:
            f.seek(self.cur_position)
            line = f.readline()
            if not line:
                self.cur_position = 0
                raise StopIteration
            self.cur_position = f.tell()
            return line

    def __str__(self):
        return os.path.abspath(self.filepath)