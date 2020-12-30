import os

mkdir_p = lambda filepath: os.makedirs(filepath) if not os.path.exists(filepath) else False
isfile =  os.path.isfile
