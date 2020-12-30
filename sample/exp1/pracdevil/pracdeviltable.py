from .helper import *
import csv
import numpy as np

class pracdevilTable():

    def __init__(self, table_header, data_path):
        self.__maindict = {}
        self.data_path = data_path
        self.table_header = table_header

    def __setitem__(self, key, item):
        if key in self.__maindict.keys():
            self.__maindict[key] = item
        else:
            raise KeyError(f"Key \"{key}\" Not found!")

    def __getitem__(self, key):
        return self.__maindict[key]

    def load_data(self, filename):
        self.filename = filename
        filename = self.data_path + "/" +  filename

        for header in self.table_header:
            self.__maindict[header] = []

        if not isfile(filename):
            with open(filename, 'w') as f:
                f.write(",".join(self.table_header))
        else:
            with open(filename, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

                for indx, row in enumerate(spamreader):
                    if indx == 0:
                        if self.table_header != row:
                            raise ValueError("Header Mismatch!")
                    else:
                        for i, item in enumerate(row):
                            item = None if item == "" else item
                            self.__maindict[self.table_header[i]].append(item)

            for key in self.__maindict.keys():
                if  set(self[key]) == {None}:
                    self[key] = np.array(self[key], dtype=float)
                    continue

                # basic data parser
                str_data = " ".join(self[key])
                if str_data == "":
                    continue

                str_data = str_data.replace(" -", "")
                str_data = str_data.replace(" +", "")

                if str_data[0] == "+" or str_data[0] == "-":
                    str_data = str_data[1:-1]

                str_data = str_data.replace(" ", "")

                if str_data.isnumeric():
                    dtype_ = int
                elif str_data.replace('e', '').replace('.', '').isnumeric():
                    dtype_ = float
                else:
                    dtype_ = str

                self[key] = np.array(self[key], dtype=dtype_)

    def __repr__(self):
        return str(self.__maindict)

    def print(self, precision=2):
        # WIP
        separator = 1 * "\t"
        header_str = separator.join(self.table_header)
        print(header_str)
        print()

        for i in range(len(self[self.table_header[0]])):
            for j in range(len(self.table_header)):
                if self[self.table_header[j]][i] > 0:
                    print(" ", end="")
                print(format(self[self.table_header[j]][i], f".{precision}f"), end=separator)
            print()

    def reload(self):
        self.load_data(self.filename)
