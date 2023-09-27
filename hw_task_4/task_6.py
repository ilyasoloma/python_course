import numpy as np
import re
class Analys:
    def __init__(self, path):
        self.path = path
        self.data = []

    def read_file(self):
        self.data = np.genfromtxt(self.path, delimiter=' ', dtype=str)
        print(self.data)

    def Finder(self, regex):
        return re.findall(r'\w{2}', ' '.join(self.data))

analys = Analys('input.txt')
analys.read_file()

reg = r'\w{2}'

print(analys.Finder(reg))