from .helper import *
from .pracdeviltable import pracdevilTable

class Experiment():
    def __init__(self, name, date, mans_path="./mans/",
            image_path="./img/", data_path="./data/"):

        #set vars
        self.name = name
        self.date = date # parse date
        self.mans_path = mans_path
        self.image_path = image_path
        self.data_path = data_path
        self.tables = {}
        self.manuals = []
        self.images = []

        # make folders
        mkdir_p(self.mans_path)
        mkdir_p(self.image_path)
        mkdir_p(self.data_path)

    def plot(self, table_, col_x, col_y):
        pass

    def table(self, name, table_headers):
        tlb = pracdevilTable(table_headers, self.data_path)
        self.tables[name] = tlb
        return tlb

    def mans(self, *manuals):
        for manual in manuals:
            # verify
            self.manuals.append(manual)

    def imgs(self, *images):
        for image in images:
            # verify
            self.images.append(image)
