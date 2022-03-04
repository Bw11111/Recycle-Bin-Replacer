import os
parent_dir = ""
ff = input("Enter Name Of Bin:\n")
directory = ff + ".{645FF040-5081-101B-9F08-00AA002F954E}"

mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)